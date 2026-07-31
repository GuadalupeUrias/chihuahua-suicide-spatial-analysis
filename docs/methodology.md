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

## 3. Pendiente
- Integrar denominador poblacional CONAPO por municipio y año.
- Definir tratamiento de municipios con pocos casos/año (varianza alta en
  tasas con denominadores pequeños) — ver README, sección de decisión
  pendiente.
- Definir periodo de agregación final (anual vs. plurianual) según cómo se
  comporten los datos una vez calculadas las tasas.
