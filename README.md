# Suicidio a nivel municipal en Chihuahua (2019-2024)

Análisis cuantitativo, longitudinal y a nivel municipal del suicidio en
Chihuahua — la entidad con la tasa más alta de México desde al menos 2022
(16.4 por 100,000 hab. en 2024, casi el triple de la media nacional).

## Pregunta de investigación (borrador)

¿Cómo se distribuye espacial y temporalmente la mortalidad por suicidio entre
los municipios de Chihuahua (2019-2024), y qué municipios concentran el
riesgo más allá de lo explicado por su tamaño poblacional?

## Relación con el repositorio de curaduría

Este proyecto reutiliza el pipeline validado en
[`mexico-suicide-data-curation`](https://github.com/TU-USUARIO/mexico-suicide-data-curation)
(mismo autor). El dataset consolidado 2019-2024 (49,918 registros a nivel
nacional, validado contra cifras oficiales INEGI con 0.00%-0.98% de
diferencia) es el insumo de entrada aquí, filtrado a `Ent_ocurr == '08'`
(Chihuahua).

## Fuentes de datos

- **Numerador (casos de suicidio)**: INEGI, Estadísticas de Defunciones
  Registradas (EDR) 2019-2024, vía el pipeline de `mexico-suicide-data-curation`.
- **Denominador (población municipal)**: CONAPO, "Reconstrucción y
  proyecciones de la población de los municipios de México 1990-2040"
  (publicado 2024). https://www.gob.mx/conapo/documentos/reconstruccion-y-proyecciones-de-la-poblacion-de-los-municipios-de-mexico-1990-2040

## Decisión metodológica ya validada

Se usa `Ent_resid`/`Mun_resid` (residencia habitual), no `Ent_ocurr`/`Mun_ocurr`
(lugar de ocurrencia) — validado contra cifra de prensa 2023 (554 vs. 561
casos, 1.25% diff) y consistente con que el denominador poblacional de CONAPO
es por residencia. Detalle completo en [`docs/methodology.md`](docs/methodology.md).

## Decisión metodológica pendiente de definir

Municipios con pocos casos por año van a tener tasas muy inestables
(varianza alta en denominadores pequeños). Opciones a evaluar antes de
reportar resultados finales:
- Tasas trianuales o quinquenales en vez de anuales para municipios pequeños
- Intervalos de confianza explícitos (ej. Poisson) en vez de solo la tasa puntual
- Suavizado espacial (bayesiano empírico) si se justifica

_Documentar aquí la decisión final y su justificación una vez tomada._

## Estructura

```
data/raw/         Población municipal CONAPO (sin modificar)
data/processed/   Dataset de Chihuahua con tasas calculadas
docs/             Metodología, borrador del artículo
notebooks/        Pipeline de análisis
src/              Funciones reutilizables
```

## Estado

🚧 En construcción — fase de definición de datos y metodología.
