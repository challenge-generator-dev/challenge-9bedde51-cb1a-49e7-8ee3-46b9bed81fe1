# Construcción de un pipeline de limpieza de datos reproducible

El equipo de análisis de datos necesita mejorar la calidad de los datos del tablero comercial. Tu tarea es preparar un conjunto de datos real para análisis, tratando valores faltantes y atípicos, normalizando tipos y documentando las transformaciones de forma reproducible.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Limpieza y transformación de datos para análisis |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Stack

- **Lenguaje:** Python
- **Framework:** pandas
- **Version:** 3.13

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Tener el proyecto base del reto funcionando en tu máquina: clonar el repositorio, instalar las herramientas y verificar que compila y arranca antes de empezar a practicar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Instala las herramientas para ejecutar el proyecto: Python 3.10+ y pip.
- Clona el repositorio del reto (el enlace viene en la entrega del reto y en la sección "Repositorio del Proyecto" del PDF) y ábrelo en tu IDE.
- Instala las dependencias y compila ejecutando `pip install -r requirements.txt && python -m compileall -q app && python -c "import app"` en la raíz del repositorio.
- Confirma que el comando termina sin errores: el proyecto arranca y sus pruebas corren.
- Ubica los archivos de práctica: son los que contienen `TODO(reto)` (búscalos en el repositorio). Lee el README.md y el AGENTS.md antes de empezar.

**Entregable:** El proyecto compila/arranca sin errores con `pip install -r requirements.txt && python -m compileall -q app && python -c "import app"`.

<details>
<summary>Pistas de conocimiento</summary>

- Los archivos con `TODO(reto)` son el ejercicio: el resto del repositorio ya está resuelto y no hace falta tocarlo.
- Si el comando de verificación falla, revisa la versión de las herramientas instaladas antes de modificar código.
- AGENTS.md describe el reto, el comando de verificación y las reglas del repositorio.

</details>

### Fase 1: Identificación de problemas en los datos

**Objetivo:** Detectar y documentar valores faltantes y atípicos en el conjunto de datos.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Implementa la pieza p1 en el componente app (capa core).
- El informe debe ser generado por un método exclusivo de la pieza y validado con casos de aceptación.
- Incluye al menos 4 casos de aceptación (2 de error/borde) para la pieza.

**Entregable:** Clase DataQualityReporter que genera un informe estructurado con estadísticas de valores faltantes y atípicos.

<details>
<summary>Pistas de conocimiento</summary>

- Métodos para detectar valores faltantes y atípicos en pandas.

</details>

### Fase 2: Tratamiento de valores faltantes y atípicos

**Objetivo:** Aplicar técnicas para tratar valores faltantes y atípicos en el conjunto de datos.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Elige y aplica técnicas para tratar los valores faltantes y atípicos identificados en la fase anterior.
- Documenta las técnicas utilizadas y los resultados obtenidos.

**Entregable:** Conjunto de datos limpio con valores faltantes y atípicos tratados.

<details>
<summary>Pistas de conocimiento</summary>

- Técnicas comunes para tratar valores faltantes y atípicos en pandas.

</details>

### Fase 3: Normalización de tipos de datos

**Objetivo:** Normalizar los tipos de datos en el conjunto de datos para asegurar consistencia.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica y normaliza los tipos de datos en el conjunto de datos.
- Documenta las transformaciones realizadas.

**Entregable:** Conjunto de datos con tipos de datos normalizados.

<details>
<summary>Pistas de conocimiento</summary>

- Métodos para normalizar tipos de datos en pandas.

</details>

### Fase 4: Documentación y validación del pipeline

**Objetivo:** Documentar las transformaciones realizadas y validar el pipeline de limpieza.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Documenta todas las transformaciones realizadas en un informe.
- Crea pruebas para validar que el pipeline de limpieza funciona como se espera.
- Ejecuta las pruebas y documenta los resultados.

**Entregable:** Informe con la documentación del pipeline y resultados de las pruebas.

<details>
<summary>Pistas de conocimiento</summary>

- Métodos para crear y ejecutar pruebas en pandas.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es un pipeline de limpieza de datos y por qué es importante?
- **paraQueSirve**: ¿Para qué sirve tratar valores faltantes y atípicos en un conjunto de datos?
- **comoSeUsa**: ¿Cómo se aplican técnicas de normalización de tipos de datos en pandas?
- **erroresComunes**: ¿Cuáles son los errores comunes al tratar valores faltantes y atípicos?
- **queDecisionesImplica**: ¿Qué decisiones implica la creación de un pipeline de limpieza reproducible?

## Criterios de Evaluacion

- Identificación correcta de valores faltantes y atípicos.
- Aplicación efectiva de técnicas para tratar valores faltantes y atípicos.
- Normalización correcta de tipos de datos.
- Documentación clara y completa del pipeline de limpieza.
- Creación y ejecución exitosa de pruebas para validar el pipeline.

## Mapa de fases

La **Fase 0** es clonar el repositorio, instalar dependencias y correr las pruebas de aceptacion: todas fallan porque la logica de cada pieza esta pendiente.

| Fase | Pieza (skill) | Archivo:simbolo | Criterios | Prueba | Comando |
|------|---------------|-----------------|-----------|--------|---------|
| f1 — Identificación de problemas en los datos | Detección de valores faltantes y atípicos con estadísticas descriptivas | `app/src/data/data_quality_reporter.py:DataQualityReporter` | El informe generado contiene estadísticas de valores faltantes por columna.; El informe identifica valores atípicos usando el método IQR.; El informe maneja datasets vacíos o con columnas no numéricas sin fallar.; El informe valida que el dataset de entrada tenga el esquema esperado. | `tests/acceptance/test_f1.py` | `python -m pytest -q tests/acceptance/test_f1.py` |
| f2 — Tratamiento de valores faltantes y atípicos | Tratamiento reproducible de valores faltantes y atípicos | `app/src/features/data_cleaner.py:DataCleaner` | Los valores faltantes en columnas numéricas se imputan con la mediana.; Los valores faltantes en columnas categóricas se imputan con la moda.; Los valores atípicos se tratan con capping usando percentiles 5 y 95.; El pipeline falla con un error descriptivo si el dataset no tiene el esquema esperado. | `tests/acceptance/test_f2.py` | `python -m pytest -q tests/acceptance/test_f2.py` |
| f3 — Normalización de tipos de datos | Normalización de tipos de datos con manejo de errores | `app/src/features/data_type_normalizer.py:DataTypeNormalizer` | Las columnas numéricas se convierten a float64.; Las columnas categóricas se convierten a category.; Las fechas se parsean a datetime64[ns].; El pipeline falla con un error descriptivo si una columna no puede ser convertida al tipo esperado.; El pipeline maneja datasets con columnas duplicadas renombrándolas automáticamente. | `tests/acceptance/test_f3.py` | `python -m pytest -q tests/acceptance/test_f3.py` |
| f4 — Documentación y validación del pipeline | Documentación reproducible de transformaciones con ejemplos | `app/src/serve/pipeline_reporter.py:PipelineReporter` | El pipeline genera un reporte de transformaciones aplicadas en formato Markdown.; El reporte incluye ejemplos de datos antes/después de cada transformación.; Las pruebas validan que el pipeline preserva el número de filas del dataset original.; Las pruebas verifican que el pipeline maneja datasets con esquemas desconocidos sin fallar.; El pipeline registra warnings para columnas con alta cardinalidad en variables categóricas. | `tests/acceptance/test_f4.py` | `python -m pytest -q tests/acceptance/test_f4.py` |

## Pruebas de aceptacion

Las pruebas de aceptacion (columna "Prueba" de la tabla) son de **solo lectura**: definen que significa "listo". No las edites, no las borres y no les agregues `skip`; lo que se resuelve es el codigo de cada pieza.

## Restricciones del pedido

| Restriccion | Donde se cumple | Estado |
|-------------|-----------------|--------|
| Usa pandas a diario pero sus notebooks no son reproducibles | chequeo estatico (code): exige `def`, `class`, `import pandas`; prohibe `# In[`, `get_ipython` | Verificada |

## Herramientas

- **Python**: Tecnologia del perfil del candidato: el reto se resuelve con ella.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && python -m compileall -q app && python -c "import app"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
