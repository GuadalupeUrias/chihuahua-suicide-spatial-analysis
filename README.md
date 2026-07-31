# Suicidio a nivel municipal en Chihuahua (2019-2024)

Análisis cuantitativo, longitudinal y a nivel municipal del suicidio en
Chihuahua — la entidad con la tasa más alta de México desde al menos 2022
(16.4 por 100,000 hab. en 2024, casi el triple de la media nacional).

## Hallazgos principales

1. **La Sierra Tarahumara concentra el riesgo de forma persistente**: tasa
   agrupada 2019-2024 de 31.1 por 100k, el doble que el resto del estado
   (16.5). Tres municipios (Bocoyna, Balleza, Guerrero) aparecen en el top 15
   estatal por tasa en los 6 años del periodo — patrón sostenido, no ruido
   de un solo año.
2. **La etnicidad no explica la diferencia** — hallazgo que refuta una
   narrativa asumida en la literatura existente. El % de casos con
   autoadscripción indígena en la Sierra Tarahumara (58.3%) es
   prácticamente idéntico al % real de población indígena de esa región
   (58.0%, Censo 2020) — razón 1.01, sin sobrerrepresentación. El patrón
   apunta a un factor estructural/regional (aislamiento, acceso a salud),
   no a la identidad étnica en sí misma.

Detalle completo y metodología en [`docs/methodology.md`](docs/methodology.md).

## Pregunta de investigación (borrador)

¿Cómo se distribuye espacial y temporalmente la mortalidad por suicidio entre
los municipios de Chihuahua (2019-2024), y qué municipios concentran el
riesgo más allá de lo explicado por su tamaño poblacional?

## Relación con el repositorio de curaduría

Este proyecto reutiliza el pipeline validado en
[`mexico-suicide-data-curation`](https://github.com/TU-USUARIO/mexico-suicide-data-curation)
(mismo autor). El dataset consolidado 2019-2024 (49,918 registros a nivel
nacional, validado contra cifras oficiales INEGI con 0.00%-0.98% de
diferencia) es el insumo de entrada aquí, filtrado a `Ent_resid == '08'`
(Chihuahua, por residencia habitual — ver decisión metodológica abajo).

## Fuentes de datos

- **Numerador (casos de suicidio)**: INEGI, Estadísticas de Defunciones
  Registradas (EDR) 2019-2024, vía el pipeline de `mexico-suicide-data-curation`.
- **Denominador (población municipal)**: CONAPO, "Reconstrucción y
  proyecciones de la población de los municipios de México 1990-2040"
  (publicado 2024). https://www.gob.mx/conapo/documentos/reconstruccion-y-proyecciones-de-la-poblacion-de-los-municipios-de-mexico-1990-2040
- **Población indígena por municipio**: INPI, "Población indígena
  autoadscrita por municipio" (muestra censal 2020).
  https://www.inpi.gob.mx/indicadores2020/

## Decisión metodológica ya validada

Se usa `Ent_resid`/`Mun_resid` (residencia habitual), no `Ent_ocurr`/`Mun_ocurr`
(lugar de ocurrencia) — validado contra cifra de prensa 2023 (554 vs. 561
casos, 1.25% diff) y consistente con que el denominador poblacional de CONAPO
es por residencia. Detalle completo en [`docs/methodology.md`](docs/methodology.md).

## Decisión metodológica: incertidumbre en tasas municipales

Se mantiene granularidad **anual** (no se agregan varios años en un solo
periodo), pero cada tasa se reporta junto con su **intervalo de confianza
95% (Poisson exacto)**. Municipios con pocos casos muestran tasas puntuales
altas pero intervalos muy anchos — eso se interpreta como evidencia de
incertidumbre real, no se oculta ni se suaviza artificialmente. Ver
`docs/methodology.md` y `notebooks/02_population_merge.ipynb`, sección 5b.

## Estructura

```
data/raw/         Población municipal CONAPO e INPI, sin modificar
data/processed/   Datasets de Chihuahua, tasas y comparaciones calculadas
docs/             Metodología, borrador del artículo
notebooks/
  01_filter_chihuahua.ipynb                Filtrar casos de Chihuahua (por residencia)
  02_population_merge.ipynb                Unir población CONAPO, calcular tasas + IC Poisson
  03_recurrence_analysis.ipynb             Recurrencia municipal y tasa agrupada 2019-2024
  04_indigenous_context.ipynb              Composición indígena de los casos (Conindig)
  05_population_indigenous_comparison.ipynb Comparar composición de casos vs. población real (Censo 2020)
src/              Funciones reutilizables
```

## Estado

🔬 Análisis exploratorio completo (notebooks 01-05). Hallazgos principales
documentados arriba y en `docs/methodology.md`. Siguiente fase: investigar
qué factor estructural específico (aislamiento, acceso a salud) explica
mejor la tasa elevada de la Sierra Tarahumara.
