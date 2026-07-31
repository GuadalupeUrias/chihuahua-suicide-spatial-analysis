# Metodología

> Estado: en construcción — se completa conforme avanza el análisis.

## 1. Fuente y alcance
- Numerador (casos): consolidado nacional `mexico-suicide-data-curation`
  (INEGI EDR 2019-2024, 49,918 registros, validado contra cifras oficiales).
- Denominador (población): CONAPO, "Reconstrucción y proyecciones de la
  población de los municipios de México 1990-2040" (pendiente de descargar
  e integrar).
- Filtro de entidad: Chihuahua (código `08`).

## 2. Decisión metodológica: residencia habitual, no lugar de ocurrencia

**Decisión:** el análisis usa `Ent_resid`/`Mun_resid` (residencia habitual de
la persona fallecida), no `Ent_ocurr`/`Mun_ocurr` (lugar donde ocurrió la
defunción).

**Evidencia que sustenta la decisión:**

| Filtro usado | Casos Chihuahua 2023 | Cifra de prensa (561) | Diferencia |
|---|---|---|---|
| `Ent_ocurr == '08'` | 512 | 561 | 8.7% |
| `Ent_resid == '08'` | 554 | 561 | **1.25%** |

**Justificación epidemiológica (más allá de la validación numérica):** los
denominadores poblacionales de CONAPO son estimaciones de dónde *vive* la
gente, no de dónde ocurren los hechos. Si el numerador (casos) se cuenta por
lugar de ocurrencia mientras el denominador (población) es por residencia,
las tasas municipales quedan distorsionadas — un municipio con más capacidad
de atención médica/forense puede "atraer" defunciones de personas que vivían
en otro municipio, inflando artificialmente su tasa sin reflejar mayor riesgo
real en su población residente. Usar residencia habitual en ambos lados
(numerador y denominador) es el estándar en epidemiología descriptiva y es
consistente con cómo el propio INEGI reporta sus cifras oficiales por
entidad.

## 3. Decisión metodológica: incertidumbre en tasas municipales

**Decisión:** granularidad anual (no agregación plurianual), con intervalo
de confianza 95% (Poisson exacto, vía relación chi-cuadrada) reportado junto
a cada tasa.

**Justificación:** agregar varios años en un solo periodo oculta la
variación temporal, que es parte de la pregunta de investigación. En vez de
sacrificar esa granularidad, se hace explícita la incertidumbre: un municipio
con tasa puntual alta pero IC muy ancho (ej. 3 casos en una población de
1,400) se reporta como tal — es evidencia real de que ese dato individual no
alcanza para una conclusión sólida, no un error a esconder con suavizado.

## 4. Exclusiones documentadas
- **1 registro con `Mun_resid == '999'`** (municipio no especificado, del
  total de 553 casos de Chihuahua 2019-2024) se excluye del análisis
  municipal por definición — no existe municipio al que asignarlo. Se
  mantiene en el dataset base para análisis a nivel estatal, pero se excluye
  al calcular tasas por municipio (ver `02_population_merge.ipynb`, sección
  5). Impacto: 0.18% del total, no afecta conclusiones agregadas.

## 5. Hallazgo: la Sierra Tarahumara concentra el riesgo, de forma persistente

**Definición de región:** 17 municipios (Balleza, Batopilas de Manuel Gómez
Morín, Bocoyna, Carichí, Chínipas, Guachochi, Guadalupe y Calvo, Guazapares,
Guerrero, Maguarichi, Morelos, Moris, Nonoava, Ocampo, Temósachic, Urique,
Uruachi), tomada de fuente académica citable (diagnóstico sociocultural de
la Sierra Tarahumara, ver `notebooks/04_indigenous_context.ipynb`).

**Resultado (`03_recurrence_analysis.ipynb`):**

| Región | Tasa agrupada 2019-2024 (por 100k) | Años en top 15 anual (de 6) |
|---|---|---|
| Sierra Tarahumara (17 municipios) | 31.1 | 2.82 promedio |
| Resto del estado (50 municipios) | 16.5 | 0.84 promedio |

Bocoyna, Balleza y Guerrero aparecen en el top 15 por tasa en **los 6 años**
del periodo, con intervalos de confianza que no se acercan a cero — evidencia
de patrón persistente, no fluctuación aleatoria de un solo año.

## 6. Hallazgo: la etnicidad NO explica la diferencia — refutación de una narrativa asumida

**Pregunta:** ¿la tasa más alta de la Sierra Tarahumara se explica porque su
población es mayoritariamente indígena?

**Resultado (`05_population_indigenous_comparison.ipynb`, fuente de
población: INPI, Censo 2020):**

| Región | % población indígena (real) | % casos con autoadscripción indígena | Razón casos/población |
|---|---|---|---|
| Sierra Tarahumara | 58.0% | 58.3% | **1.01** |
| Resto del estado | 7.0% | 6.1% | **0.87** |

**Interpretación:** la razón está esencialmente en 1.0 en ambas regiones —
**no hay sobrerrepresentación** de personas indígenas entre los casos de
suicidio más allá de lo que su propio peso poblacional explicaría. Esto
**refuta la narrativa implícita** en buena parte de la literatura y cobertura
mediática existente sobre suicidio en Chihuahua, que enmarca el fenómeno
como asociado a la identidad indígena en sí misma. La evidencia apunta en
cambio a un factor **estructural/regional** (aislamiento geográfico, acceso
a servicios de salud mental, dispersión poblacional, pobreza) como
explicación más plausible del patrón — no a la etnicidad como tal.

**Limitación:** 64% de los casos en Chihuahua tienen `Conindig` sin
especificar; la comparación de la sección de arriba se calculó solo sobre
casos con dato conocido. El % de "no especificado" es similar entre Sierra
(67.4%) y resto del estado (63.7%), lo que reduce la preocupación de sesgo
diferencial, pero sigue siendo una limitación a declarar explícitamente en
cualquier versión del artículo.

## 7. Pendiente
- Investigar qué factor estructural específico explica mejor la tasa
  elevada de la Sierra Tarahumara (aislamiento geográfico, acceso a
  servicios de salud mental, dispersión poblacional, pobreza) — siguiente
  fase de análisis.
- Definir si se reporta un ranking/mapa basado en la tasa puntual, el límite
  inferior del IC, o ambos con anotación explícita de incertidumbre.
- Evaluar si conviene un modelo de suavizado bayesiano empírico como análisis
  complementario (no sustituto) para la versión final del artículo.
