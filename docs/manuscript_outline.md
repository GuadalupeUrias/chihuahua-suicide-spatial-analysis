# Esqueleto del manuscrito — Suicidio en la Sierra Tarahumara, Chihuahua (2019-2024)

Estado: borrador de estructura. Completar secciones marcadas `[PENDIENTE]`.
No reemplaza methodology.md/quality_report.md — este documento es específico
para la redacción del artículo, ellos siguen siendo la fuente de verdad
metodológica del pipeline.

---

## Título de trabajo
"Exceso de mortalidad por suicidio en la Sierra Tarahumara, Chihuahua
(2019-2024): evidencia contra la hipótesis de sobrerrepresentación étnica"

`[PENDIENTE: ajustar según revista objetivo — algunas prefieren título más
descriptivo/neutro, otras aceptan título que anuncia el hallazgo]`

## Palabras clave (5-6)
Suicidio; mortalidad; Sierra Tarahumara; pueblos indígenas; determinantes
estructurales; Chihuahua, México

---

## Abstract (250-300 palabras, estructura IMRaD compacta)
- **Contexto (1-2 líneas):** Chihuahua encabeza las tasas de suicidio a
  nivel nacional en México; la Sierra Tarahumara, con alta población
  indígena rarámuri, suele señalarse como foco del problema.
- **Objetivo (1 línea):** cuantificar el exceso de mortalidad por suicidio
  en la Sierra Tarahumara vs. el resto del estado, y evaluar si la
  etnicidad explica ese exceso.
- **Métodos (2-3 líneas):** microdatos EDR/INEGI 2019-2024 (defunciones
  registradas, residencia habitual), denominadores CONAPO; razón de tasas
  exacta (Clopper-Pearson/binomial condicional); comparación de composición
  étnica de casos (Conindig) contra población indígena real (INPI, Censo
  2020).
- **Resultados (3-4 líneas):** RR = 3.03 (IC95%: 2.76-3.32; p<0.001),
  estable año con año (2.84-3.40). Composición étnica de casos (58.3%
  indígena) ≈ composición poblacional real (58.0%); razón 1.01, sin
  sobrerrepresentación.
- **Conclusión (1-2 líneas):** el exceso de mortalidad es regional, no
  étnico; señala factores estructurales (aislamiento geográfico, acceso a
  salud mental) como hipótesis a investigar, no la identidad indígena per se.

---

## 1. Introducción
1.1 Magnitud del problema en México/Chihuahua
　`[PENDIENTE: cifra nacional +25.6% acumulado 2019-2024 — decidir si entra
　aquí como contexto o se reserva para artículo separado, ver nota abajo]`
1.2 Marco dominante en la literatura: narrativa de "crisis de suicidio
　indígena" en regiones serranas/rurales de México
　`[PENDIENTE: revisión breve de 3-5 fuentes que sostienen esa narrativa —
　necesario para que el hallazgo tenga a qué contraponerse]`
1.3 Vacío/problema: la narrativa étnica rara vez se contrasta contra el
　denominador poblacional real — riesgo de conflatar concentración
　geográfica con causalidad étnica
1.4 Objetivo e hipótesis del estudio (explícitos, ya validados)

## 2. Métodos
2.1 Fuente de datos: EDR-INEGI 2019-2024, variable `Tipo_defun==3`
2.2 Definición geográfica: residencia habitual (`Ent_resid`/`Mun_resid`),
　justificación de por qué no ocurrencia (1.25% vs 8.7% diff vs. cifra de
　prensa 2023)
2.3 Denominadores poblacionales: CONAPO, proyecciones municipales
2.4 Definición de Sierra Tarahumara (17 municipios, fuente citable)
2.5 Análisis estadístico:
　　- Tasas anuales por 100k con IC 95% Poisson exacto
　　- Razón de tasas (RR) Sierra vs. resto, IC y prueba exactos
　　  (binomial condicional)
　　- Comparación de composición étnica de casos (Conindig) vs. población
　　  indígena real por municipio (INPI Censo 2020)
2.6 Limitaciones de los datos declaradas de antemano: Conindig es
　autoadscripción individual del caso, no variable poblacional; ~64% de
　casos sin dato de Conindig especificado `[VERIFICAR % exacto]`

## 3. Resultados
3.1 Tasas municipales 2019-2024 (tabla/mapa descriptivo)
3.2 Recurrencia: municipios que aparecen consistentemente en el top de
　tasas (03_recurrence_analysis)
3.3 **Resultado central:** RR Sierra vs. resto = 3.03 (IC95% 2.76-3.32,
　p<0.001), estabilidad anual 2.84-3.40 (tabla con los 6 años)
3.4 Composición étnica: 58.3% de casos indígenas en la sierra vs. 58.0%
　de población indígena real → razón 1.01, sin sobrerrepresentación
3.5 `[PENDIENTE: ¿agregar desglose por edad/sexo dentro de la sierra? —
　pendiente de decidir, no bloqueante para el esqueleto]`

## 4. Discusión
4.1 Interpretación del hallazgo central: el exceso de 3x es real,
　estadísticamente robusto y estable — no es artefacto de muestra pequeña
　ni de un año atípico
4.2 Por qué esto reta la narrativa dominante: si la etnicidad explicara el
　exceso, la razón casos/población debería ser notablemente >1, no ~1
4.3 Hipótesis estructurales alternativas a explorar en investigación futura
　(no se prueban aquí, se plantean): aislamiento geográfico, tiempo de
　acceso a servicios de salud mental, disponibilidad de medios letales,
　migración/desestructuración comunitaria
　`[PENDIENTE: ¿hay algún dato adicional disponible para al menos una
　proxy estructural, ej. tiempo/distancia a hospital? Si no, queda
　explícitamente como limitación + agenda futura]`
4.4 Comparación con literatura previa `[PENDIENTE: cotejar contra los 3-5
　estudios de 1.2]`

## 5. Limitaciones
- Diseño ecológico (tasas municipales, no modelo individual con
　covariables)
- Conindig con alto porcentaje no especificado
- Definición de Sierra Tarahumara basada en fuente académica citada, no en
　criterio administrativo oficial único `[VERIFICAR si existe definición
　oficial alterna, ej. CDI/INPI, y si difiere de la usada]`
- Referencia poblacional indígena es un corte 2020 aplicado a todo
　2019-2024 (supuesto de estabilidad demográfica de corto plazo)

## 6. Conclusión
Reafirmar: exceso robusto y estable, no explicado por composición étnica;
llamado a investigar determinantes estructurales regionales antes de seguir
usando el marco étnico como explicación por defecto.

## Declaraciones
- Disponibilidad de datos: repo público + DOI Zenodo del pipeline nacional
　(`10.5281/zenodo.21686584`); este repo (`chihuahua-suicide-spatial-analysis`)
　`[PENDIENTE: decidir si también se registra en Zenodo antes de someter]`
- Conflicto de interés: `[PENDIENTE]`
- Financiamiento: `[PENDIENTE]`

---

## Nota abierta: ¿el hallazgo nacional (+25.6%, sin caída pandémica) va aquí o aparte?
No se resuelve en este esqueleto. Si se integra, iría como párrafo de
contexto en 1.1, sin desviar el foco del artículo (que es Chihuahua/Sierra).
Si se separa, este artículo puede someterse antes sin esperar ese análisis.
Recomendación operativa: dejarlo fuera de este manuscrito y tratarlo como
pieza de portafolio/artículo independiente — evita atar el sometimiento de
este artículo a trabajo pendiente no relacionado con la pregunta central.
