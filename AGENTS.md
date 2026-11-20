# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Construcción de un pipeline de limpieza de datos reproducible**.

| | |
|---|---|
| Tema | Limpieza y transformación de datos para análisis |
| Nivel | advanced-l2 |
| Chapter | Ciencia de Datos — Científico |
| Especialidad | Cientifico de datos |
| Stack | Python / pandas |
| Patron arquitectonico | pipeline de procesamiento con capas de limpieza, transformación y validación |
| Tiempo estimado | 8 horas |

## Herramientas

- **Python**: Tecnologia del perfil del candidato: el reto se resuelve con ella.

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `notebooks/eda.ipynb con el analisis exploratorio`
- `src/data con la carga y el preprocesamiento`
- `src/features con la ingenieria de variables`
- `src/models con entrenamiento y evaluacion`
- `src/serve con la exposicion del modelo (inferencia)`
- `tests/ con validacion de metricas esperadas`

Dependencias:

- fastapi ==0.162.4
- uvicorn ==0.54.0
- pydantic ==2.14.3
- pytest ==9.2.0
- httpx ==0.28.1
- numpy ==2.5.5
- pandas ==3.1.1

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && python -m compileall -q app && python -c "import app"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && python -m compileall -q app && python -c "import app"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Identificación de problemas en los datos**: Clase DataQualityReporter que genera un informe estructurado con estadísticas de valores faltantes y atípicos.
- **Fase 2 — Tratamiento de valores faltantes y atípicos**: Conjunto de datos limpio con valores faltantes y atípicos tratados.
- **Fase 3 — Normalización de tipos de datos**: Conjunto de datos con tipos de datos normalizados.
- **Fase 4 — Documentación y validación del pipeline**: Informe con la documentación del pipeline y resultados de las pruebas.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `app/src/data/data_quality_reporter.py` — La pieza p1 (Detección de valores faltantes y atípicos con estadísticas descriptivas, fase f1) vive aqui: este archivo es su unico dueno (blueprint v2).
- [ ] `app/src/features/data_cleaner.py` — La pieza p2 (Tratamiento reproducible de valores faltantes y atípicos, fase f2) vive aqui: este archivo es su unico dueno (blueprint v2).
- [ ] `app/src/features/data_type_normalizer.py` — La pieza p3 (Normalización de tipos de datos con manejo de errores, fase f3) vive aqui: este archivo es su unico dueno (blueprint v2).
- [ ] `app/src/serve/pipeline_reporter.py` — La pieza p4 (Documentación reproducible de transformaciones con ejemplos, fase f4) vive aqui: este archivo es su unico dueno (blueprint v2).

## Mapa de fases

La **Fase 0** es clonar el repositorio, instalar dependencias y correr las pruebas de aceptacion: todas fallan porque la logica de cada pieza esta pendiente.

| Fase | Pieza (skill) | Archivo:simbolo | Criterios | Prueba | Comando |
|------|---------------|-----------------|-----------|--------|---------|
| f1 — Identificación de problemas en los datos | Detección de valores faltantes y atípicos con estadísticas descriptivas | `app/src/data/data_quality_reporter.py:DataQualityReporter` | El informe generado contiene estadísticas de valores faltantes por columna.; El informe identifica valores atípicos usando el método IQR.; El informe maneja datasets vacíos o con columnas no numéricas sin fallar.; El informe valida que el dataset de entrada tenga el esquema esperado. | `tests/acceptance/test_f1.py` | `python -m pytest -q tests/acceptance/test_f1.py` |
| f2 — Tratamiento de valores faltantes y atípicos | Tratamiento reproducible de valores faltantes y atípicos | `app/src/features/data_cleaner.py:DataCleaner` | Los valores faltantes en columnas numéricas se imputan con la mediana.; Los valores faltantes en columnas categóricas se imputan con la moda.; Los valores atípicos se tratan con capping usando percentiles 5 y 95.; El pipeline falla con un error descriptivo si el dataset no tiene el esquema esperado. | `tests/acceptance/test_f2.py` | `python -m pytest -q tests/acceptance/test_f2.py` |
| f3 — Normalización de tipos de datos | Normalización de tipos de datos con manejo de errores | `app/src/features/data_type_normalizer.py:DataTypeNormalizer` | Las columnas numéricas se convierten a float64.; Las columnas categóricas se convierten a category.; Las fechas se parsean a datetime64[ns].; El pipeline falla con un error descriptivo si una columna no puede ser convertida al tipo esperado.; El pipeline maneja datasets con columnas duplicadas renombrándolas automáticamente. | `tests/acceptance/test_f3.py` | `python -m pytest -q tests/acceptance/test_f3.py` |
| f4 — Documentación y validación del pipeline | Documentación reproducible de transformaciones con ejemplos | `app/src/serve/pipeline_reporter.py:PipelineReporter` | El pipeline genera un reporte de transformaciones aplicadas en formato Markdown.; El reporte incluye ejemplos de datos antes/después de cada transformación.; Las pruebas validan que el pipeline preserva el número de filas del dataset original.; Las pruebas verifican que el pipeline maneja datasets con esquemas desconocidos sin fallar.; El pipeline registra warnings para columnas con alta cardinalidad en variables categóricas. | `tests/acceptance/test_f4.py` | `python -m pytest -q tests/acceptance/test_f4.py` |

## Pruebas de aceptacion y ubicacion de la logica

Las pruebas de aceptacion (columna "Prueba" de la tabla) son de **solo lectura**: definen que significa "listo". No las edites, no las borres y no les agregues `skip`; lo que se resuelve es el codigo de cada pieza.

La logica de cada pieza va en su archivo; no la muevas a otro.

## Restricciones del pedido

| Restriccion | Donde se cumple | Estado |
|-------------|-----------------|--------|
| Usa pandas a diario pero sus notebooks no son reproducibles | chequeo estatico (code): exige `def`, `class`, `import pandas`; prohibe `# In[`, `get_ipython` | Verificada |

## Lo que falta y tenes que completar

Referencias no verificadas para: .py. El analisis estatico no cubre esos lenguajes: que no se haya listado nada NO garantiza que no haya referencias colgando. Corre el comando de verificacion para encontrarlas.

### 1. Referencias colgando (1)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `app/src/models/schemas.py` — `DataQualityReporter.get`
      Se invoca `get` sobre `DataQualityReporter`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Presentes (13)

- `requirements.txt`
- `app/src/data/data_loader.py`
- `app/src/models/schemas.py`
- `app/src/data/data_quality_reporter.py`
- `app/src/features/data_cleaner.py`
- `app/src/features/data_type_normalizer.py`
- `app/src/serve/pipeline_reporter.py`
- `tests/acceptance/test_f1.py`
- `tests/acceptance/test_f2.py`
- `tests/acceptance/test_f3.py`
- `tests/acceptance/test_f4.py`
- `app/src/serve/main.py`
- `app/reports/data_quality_report.md`

### Capas del patron declarado

Son las capas que la propuesta arquitectonica plantea, marcadas segun existan hoy en el repo. Orientan donde poner el codigo nuevo; no son una condicion para compilar.

- `src/data` (ausente)
- `src/features` (ausente)
- `src/models` (ausente)
- `src/serve` (ausente)
- `tests` (presente)
- `reports` (ausente)

## Verificacion

```bash
pip install -r requirements.txt && python -m compileall -q app && python -c "import app"
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **pipeline de procesamiento con capas de limpieza, transformación y validación**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Análisis de datos, Tecnología Python, Advanced L2
- Brecha que el reto ataca: Prepara un conjunto de datos real para análisis: trata valores faltantes y atípicos, normaliza tipos y documenta las transformaciones de forma reproducible.
- Mision: Mejorar la calidad de los datos del tablero comercial

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
