"""
Funciones de limpieza y analisis reutilizables para el pipeline de
chihuahua-suicide-spatial-analysis.

Convenciones del proyecto:
- Docstrings y comentarios en espanol.
- Las funciones retornan dict o DataFrame; no imprimen directamente
  (el notebook decide que mostrar).
- Los nulos NUNCA se imputan; se preservan como NaN explicito y se
  reportan en el dict de salida (principio ya aplicado en el resto
  del pipeline).
"""

import pandas as pd
from scipy.stats import chisquare

MESES_NOMBRE = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
    7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre',
    11: 'Noviembre', 12: 'Diciembre',
}

# Codigo que usa INEGI en el catalogo EDR para "mes no especificado"
CODIGO_MES_NO_ESPECIFICADO = 99


def preparar_mes_ocurrencia(df, columna_mes='Mes_ocurr'):
    """
    Convierte la columna de mes de ocurrencia a entero y separa los
    registros con mes valido (1-12) de los no especificados (codigo 99
    de INEGI) o nulos.

    Parametros
    ----------
    df : DataFrame
        Debe contener la columna indicada en `columna_mes`.
    columna_mes : str
        Nombre de la columna con el mes de ocurrencia (default: 'Mes_ocurr').

    Retorna
    -------
    dict con:
        - 'df_valido': DataFrame filtrado a mes valido (1-12), con nueva
          columna entera 'mes'.
        - 'n_total': total de registros de entrada.
        - 'n_validos': registros con mes 1-12.
        - 'n_no_especificado': registros con codigo 99.
        - 'n_nulo': registros con NaN en la columna de mes.
    """
    n_total = len(df)
    mes_num = pd.to_numeric(df[columna_mes], errors='coerce')

    mask_nulo = mes_num.isna()
    mask_no_esp = mes_num == CODIGO_MES_NO_ESPECIFICADO
    mask_valido = mes_num.between(1, 12)

    df_valido = df.loc[mask_valido].copy()
    df_valido['mes'] = mes_num.loc[mask_valido].astype(int)

    return {
        'df_valido': df_valido,
        'n_total': n_total,
        'n_validos': int(mask_valido.sum()),
        'n_no_especificado': int(mask_no_esp.sum()),
        'n_nulo': int(mask_nulo.sum()),
    }


def test_estacionalidad_mensual(df, columna_mes='Mes_ocurr'):
    """
    Prueba chi-cuadrado de bondad de ajuste para uniformidad mensual de
    casos de suicidio. H0: los casos se distribuyen uniformemente entre
    los 12 meses del anio (sin patron estacional).

    Nota metodologica: esta es una prueba de uniformidad simple, no un
    modelo de series de tiempo con temperatura como covariable (a
    diferencia de Fernandez-Lopez et al., 2021). Sirve como primer
    acercamiento descriptivo/inferencial, no reemplaza un modelo
    estacional completo.

    Parametros
    ----------
    df : DataFrame
        Casos ya filtrados (ej. Chihuahua, residencia habitual).
    columna_mes : str
        Nombre de la columna con el mes de ocurrencia.

    Retorna
    -------
    dict con:
        - 'tabla_mensual': DataFrame con casos observados, esperados y
          porcentaje de exceso/deficit por mes.
        - 'chi2': estadistico chi-cuadrado.
        - 'p_value': p-value de la prueba.
        - 'meses_pico': lista de los 3 meses con mayor exceso porcentual
          sobre lo esperado, ordenados de mayor a menor.
        - 'calidad_datos': dict con conteos de registros validos/excluidos
          (ver preparar_mes_ocurrencia).
    """
    prep = preparar_mes_ocurrencia(df, columna_mes)
    df_valido = prep['df_valido']

    casos_por_mes = (
        df_valido['mes']
        .value_counts()
        .reindex(range(1, 13), fill_value=0)
        .sort_index()
    )
    total = casos_por_mes.sum()
    esperado = total / 12

    chi2_stat, p_value = chisquare(f_obs=casos_por_mes.values)

    tabla = pd.DataFrame({
        'mes': [MESES_NOMBRE[m] for m in range(1, 13)],
        'mes_num': range(1, 13),
        'casos_observados': casos_por_mes.values,
        'casos_esperados': round(esperado, 2),
        'exceso_pct': ((casos_por_mes.values - esperado) / esperado * 100).round(1),
    })

    meses_pico = (
        tabla.sort_values('exceso_pct', ascending=False)
        .head(3)['mes']
        .tolist()
    )

    return {
        'tabla_mensual': tabla,
        'chi2': round(float(chi2_stat), 3),
        'p_value': float(p_value),
        'meses_pico': meses_pico,
        'calidad_datos': {
            'n_total': prep['n_total'],
            'n_validos': prep['n_validos'],
            'n_no_especificado': prep['n_no_especificado'],
            'n_nulo': prep['n_nulo'],
        },
    }
