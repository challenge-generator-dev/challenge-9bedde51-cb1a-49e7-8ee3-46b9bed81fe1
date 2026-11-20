# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener el proyecto completo y arrancable. Guarda los archivos que te devuelva en la
carpeta del repo, respetando exactamente las rutas.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `app/src/data/data_quality_reporter.py` — La pieza p1 (Detección de valores faltantes y atípicos con estadísticas descriptivas, fase f1) vive aqui: este archivo es su unico dueno (blueprint v2).
- `app/src/features/data_cleaner.py` — La pieza p2 (Tratamiento reproducible de valores faltantes y atípicos, fase f2) vive aqui: este archivo es su unico dueno (blueprint v2).
- `app/src/features/data_type_normalizer.py` — La pieza p3 (Normalización de tipos de datos con manejo de errores, fase f3) vive aqui: este archivo es su unico dueno (blueprint v2).
- `app/src/serve/pipeline_reporter.py` — La pieza p4 (Documentación reproducible de transformaciones con ejemplos, fase f4) vive aqui: este archivo es su unico dueno (blueprint v2).

## Herramientas

- **Python**: Tecnologia del perfil del candidato: el reto se resuelve con ella.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `app/src/models/schemas.py` — `DataQualityReporter.get`: Se invoca `get` sobre `DataQualityReporter`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

### Referencias no verificadas

Referencias no verificadas para: .py. El analisis estatico no cubre esos lenguajes: que no se haya listado nada NO garantiza que no haya referencias colgando.

## Como saber que terminaste

```bash
pip install -r requirements.txt && python -m compileall -q app && python -c "import app"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Análisis de datos, Tecnología Python, Advanced L2

### Brecha de conocimiento
Prepara un conjunto de datos real para análisis: trata valores faltantes y atípicos, normaliza tipos y documenta las transformaciones de forma reproducible.

### Misión / candidato
Mejorar la calidad de los datos del tablero comercial

### Reto
- Tema: Limpieza y transformación de datos para análisis
- Seniority: advanced-l2
- Tipo: practical
- Título: Construcción de un pipeline de limpieza de datos reproducible
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Identificación de problemas en los datos — objetivo: Detectar y documentar valores faltantes y atípicos en el conjunto de datos. — entregable (NO resolver): Clase DataQualityReporter que genera un informe estructurado con estadísticas de valores faltantes y atípicos.
- Fase 2: Tratamiento de valores faltantes y atípicos — objetivo: Aplicar técnicas para tratar valores faltantes y atípicos en el conjunto de datos. — entregable (NO resolver): Conjunto de datos limpio con valores faltantes y atípicos tratados.
- Fase 3: Normalización de tipos de datos — objetivo: Normalizar los tipos de datos en el conjunto de datos para asegurar consistencia. — entregable (NO resolver): Conjunto de datos con tipos de datos normalizados.
- Fase 4: Documentación y validación del pipeline — objetivo: Documentar las transformaciones realizadas y validar el pipeline de limpieza. — entregable (NO resolver): Informe con la documentación del pipeline y resultados de las pruebas.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (entrega de archivos).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Entrega de archivos
Entregá cada archivo con su ruta completa, respetando exactamente la estructura de rutas
indicada por los marcadores: un bloque por archivo, precedido por su ruta. No generes ZIPs
ni archivos adjuntos.
La entrega debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: Entregá los archivos completos al finalizar. No preguntes si el usuario
quiere recibirlos. Simplemente entregalos; No debes desplegar en el chat el resumen de lo que arreglaste, solo entregá los archivos.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del último archivo entregado
No preguntes si el usuario quiere los archivos: simplemente entregalos siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
fastapi==0.162.4
uvicorn==0.54.0
pydantic==2.14.3
pytest==9.2.0
httpx==0.28.1
numpy==2.5.5
pandas==3.1.1

// === ARCHIVO: app/src/data/data_loader.py ===
"""
Módulo responsable de cargar datos desde fuentes externas.
La validación de calidad y de tipos se delega a las piezas de dominio correspondientes.
"""

import logging

import pandas as pd

from app.src.data.data_quality_reporter import DataQualityReporter
from app.src.models.schemas import DataSchema

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataLoader:
    """
    Carga datos desde archivos CSV, Excel o SQL y verifica el esquema mínimo.
    """

    def __init__(self, source_path: str, source_type: str = 'csv'):
        """
        Inicializa el cargador con la ruta y el tipo de fuente.

        Args:
            source_path: Ruta o conexión a la fuente de datos.
            source_type: Tipo de fuente ('csv', 'excel', 'sql').
        """
        self.source_path = source_path
        self.source_type = source_type
        self._data = None
        self._reporter = DataQualityReporter()

    def load_data(self):
        """
        Carga los datos desde la fuente y realiza la validación inicial.

        Returns:
            DataFrame cargado y validado.

        Raises:
            FileNotFoundError: Si la fuente no existe.
            ValueError: Si el tipo de fuente no es soportado o faltan columnas.
            pd.errors.EmptyDataError: Si la fuente está vacía.
        """
        try:
            if self.source_type == 'csv':
                self._data = pd.read_csv(self.source_path)
            elif self.source_type == 'excel':
                self._data = pd.read_excel(self.source_path)
            elif self.source_type == 'sql':
                raise NotImplementedError("La carga desde SQL requiere configuración adicional")
            else:
                raise ValueError(f"Tipo de fuente no soportado: {self.source_type}")

            if self._data.empty:
                raise pd.errors.EmptyDataError("La fuente de datos está vacía")

            logger.info(f"Datos cargados exitosamente desde {self.source_path}")
            return self._validate_initial_schema()

        except FileNotFoundError:
            logger.error(f"Archivo no encontrado: {self.source_path}")
            raise
        except Exception as e:
            logger.error(f"Error al cargar datos: {str(e)}")
            raise

    def _validate_initial_schema(self):
        """
        Valida las columnas requeridas y delega la verificación de tipos
        al generador de reportes de calidad.

        Returns:
            DataFrame validado.

        Raises:
            ValueError: Si faltan columnas requeridas.
        """
        try:
            required_columns = DataSchema.get_required_columns()
            missing_columns = [col for col in required_columns if col not in self._data.columns]

            if missing_columns:
                raise ValueError(f"Columnas requeridas faltantes: {missing_columns}")

            report = self._reporter.generate_report(self._data)
            for col, count in report.get('invalid_types', {}).items():
                logger.warning(f"Columna {col} tiene {count} valores fuera del tipo esperado")

            return self._data

        except Exception as e:
            logger.error(f"Error en validación de esquema: {str(e)}")
            raise

    def get_sample_data(self, n: int = 5):
        """
        Obtiene una muestra de los datos cargados.

        Args:
            n: Número de filas a retornar.

        Returns:
            Muestra de las primeras filas.
        """
        if self._data is None:
            raise ValueError("Datos no cargados. Llame primero a load_data()")
        return self._data.head(n)

    def get_data_summary(self) -> dict:
        """
        Genera un resumen estadístico básico de los datos cargados.

        Returns:
            dict con forma, columnas, tipos, valores faltantes y descripción.
        """
        if self._data is None:
            raise ValueError("Datos no cargados. Llame primero a load_data()")

        return {
            'shape': self._data.shape,
            'columns': list(self._data.columns),
            'dtypes': self._data.dtypes.to_dict(),
            'missing_values': self._data.isnull().sum().to_dict(),
            'describe': self._data.describe(include='all').to_dict()
        }

// === ARCHIVO: app/src/models/schemas.py ===
"""
Módulo que define los esquemas de datos para validación y tipado.
Incluye modelos Pydantic para validación de registros y definiciones de tipos esperados.
"""

from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class DataSchema:
    """
    Clase estática que define los esquemas y tipos esperados para los datos.
    """

    @staticmethod
    def get_required_columns() -> list[str]:
        """
        Retorna la lista de columnas requeridas en el conjunto de datos.

        Returns:
            list[str]: Nombres de columnas requeridas.
        """
        return [
            'customer_id',
            'transaction_date',
            'amount',
            'product_category',
            'payment_method'
        ]

    @staticmethod
    def get_column_types() -> dict[str, str]:
        """
        Retorna el tipo esperado para cada columna.

        Returns:
            dict[str, str]: Mapeo de columna a tipo esperado.
        """
        return {
            'customer_id': 'str',
            'transaction_date': 'datetime',
            'amount': 'float',
            'product_category': 'str',
            'payment_method': 'str'
        }

    @staticmethod
    def get_column_descriptions() -> dict[str, str]:
        """
        Retorna descripciones de cada columna para documentación.

        Returns:
            dict[str, str]: Mapeo de columna a descripción.
        """
        return {
            'customer_id': 'Identificador único del cliente',
            'transaction_date': 'Fecha y hora de la transacción',
            'amount': 'Monto de la transacción en moneda local',
            'product_category': 'Categoría del producto comprado',
            'payment_method': 'Método de pago utilizado'
        }


class TransactionRecord(BaseModel):
    """
    Modelo Pydantic para validación individual de registros de transacciones.
    """
    customer_id: str = Field(..., description="Identificador único del cliente")
    transaction_date: datetime = Field(..., description="Fecha y hora de la transacción")
    amount: float = Field(..., gt=0, description="Monto de la transacción (debe ser positivo)")
    product_category: str = Field(..., description="Categoría del producto")
    payment_method: str = Field(..., description="Método de pago")

    @field_validator('product_category')
    @classmethod
    def validate_product_category(cls, v: str) -> str:
        """Valida que la categoría del producto esté en la lista permitida."""
        valid_categories = ['electronics', 'clothing', 'groceries', 'furniture', 'other']
        if v.lower() not in valid_categories:
            raise ValueError(f'Categoría no válida: {v}')
        return v.lower()

    @field_validator('payment_method')
    @classmethod
    def validate_payment_method(cls, v: str) -> str:
        """Valida que el método de pago esté en la lista permitida."""
        valid_methods = ['credit_card', 'debit_card', 'cash', 'bank_transfer', 'mobile_payment']
        if v.lower() not in valid_methods:
            raise ValueError(f'Método de pago no válido: {v}')
        return v.lower()


class DataQualityReport(BaseModel):
    """
    Modelo para reportar métricas de calidad de datos.
    """
    total_records: int
    missing_values: dict[str, int]
    duplicate_records: int
    invalid_types: dict[str, int]
    outliers: dict[str, dict[str, int | float]]

    @field_validator('total_records')
    @classmethod
    def validate_total_records(cls, v: int) -> int:
        """Valida que el total de registros sea positivo."""
        if v <= 0:
            raise ValueError('El total de registros debe ser positivo')
        return v


def validate_dataframe_schema(df) -> bool:
    """
    Valida un DataFrame completo contra el esquema esperado.
    La verificación de tipos se delega al generador de reportes de calidad.

    Args:
        df: Datos tabulares a validar.

    Returns:
        bool: True si cumple el esquema, False en caso contrario.
    """
    try:
        required_columns = DataSchema.get_required_columns()
        if not all(col in df.columns for col in required_columns):
            return False

        # Importación diferida para evitar dependencias circulares entre capas de datos.
        from app.src.data.data_quality_reporter import DataQualityReporter

        report = DataQualityReporter().generate_report(df)
        return not report.get('invalid_types')
    except Exception:
        return False

// === ARCHIVO: app/src/data/data_quality_reporter.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
"""
Módulo para generar reportes de calidad de datos.
Identifica valores faltantes y atípicos en DataFrames usando estadísticas descriptivas.
"""

import pandas as pd
import numpy as np
from typing import Dict, Union
from app.src.models.schemas import DataSchema, DataQualityReport

class DataQualityReporter:
    """
    Genera reportes de calidad de datos para DataFrames.
    Calcula estadísticas de valores faltantes y detecta valores atípicos usando IQR.
    """

    def generate_report(self, df: pd.DataFrame) -> dict:
        raise NotImplementedError("TODO(reto): generate_report")
    def _validate_schema(self, df: pd.DataFrame) -> None:
        """
        Valida que el DataFrame cumpla con el esquema esperado.

        Args:
            df: DataFrame a validar.

        Raises:
            ValueError: Si el DataFrame no cumple con el esquema esperado.
        """
        required_columns = DataSchema.get_required_columns()
        missing_columns = [col for col in required_columns if col not in df.columns]
        extra_columns = [col for col in df.columns if col not in required_columns]

        if missing_columns or extra_columns:
            error_msg = []
            if missing_columns:
                error_msg.append(f"Columnas faltantes: {missing_columns}")
            if extra_columns:
                error_msg.append(f"Columnas inesperadas: {extra_columns}")
            raise ValueError("Esquema inválido: " + ", ".join(error_msg))

    def _calculate_missing_stats(self, df: pd.DataFrame) -> Dict[str, float]:
        raise NotImplementedError("TODO(reto): _calculate_missing_stats")
    def _identify_outliers(self, df: pd.DataFrame) -> Dict[str, Dict[str, Union[int, float]]]:
        raise NotImplementedError("TODO(reto): _identify_outliers")

// === ARCHIVO: app/src/features/data_cleaner.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
"""
Módulo para limpieza de datos.
Aplica técnicas de imputación y tratamiento de valores atípicos.
"""

import pandas as pd
import numpy as np
from typing import Dict
from app.src.models.schemas import DataSchema

class DataCleaner:
    """
    Limpia DataFrames aplicando imputación de valores faltantes y tratamiento de valores atípicos.
    """

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("TODO(reto): clean")
    def _validate_schema(self, df: pd.DataFrame) -> None:
        """
        Valida que el DataFrame cumpla con el esquema esperado.

        Args:
            df: DataFrame a validar.

        Raises:
            ValueError: Si el DataFrame no cumple con el esquema esperado.
        """
        required_columns = DataSchema.get_required_columns()
        missing_columns = [col for col in required_columns if col not in df.columns]
        extra_columns = [col for col in df.columns if col not in required_columns]

        if missing_columns or extra_columns:
            error_msg = []
            if missing_columns:
                error_msg.append(f"Columnas faltantes: {missing_columns}")
            if extra_columns:
                error_msg.append(f"Columnas inesperadas: {extra_columns}")
            raise ValueError("Esquema inválido: " + ", ".join(error_msg))

    def _impute_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("TODO(reto): _impute_missing_values")
    def _treat_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("TODO(reto): _treat_outliers")

// === ARCHIVO: app/src/features/data_type_normalizer.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
"""
Normalizador de tipos de datos para DataFrames de pandas.

Convierte columnas a tipos apropiados para análisis:
- Numéricas a float64
- Categóricas a category
- Fechas a datetime64[ns]
Maneja errores de conversión y columnas duplicadas.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Set


class ColumnTypeMapper:
    """Mapea nombres de columnas a sus tipos esperados."""

    NUMERIC_COLUMNS = {'amount', 'quantity', 'price', 'discount', 'tax'}
    DATE_COLUMNS = {'transaction_date', 'created_at', 'updated_at', 'order_date'}
    CATEGORICAL_COLUMNS = {'customer_id', 'product_category', 'payment_method', 'status', 'region'}

    @classmethod
    def get_column_type(cls, column_name: str) -> str:
        """Determina el tipo de una columna basándose en su nombre."""
        col_lower = column_name.lower()
        if col_lower in cls.NUMERIC_COLUMNS:
            return 'numeric'
        elif col_lower in cls.DATE_COLUMNS:
            return 'date'
        elif col_lower in cls.CATEGORICAL_COLUMNS:
            return 'categorical'
        return 'unknown'


class DataTypeNormalizer:
    """Normaliza los tipos de datos de un DataFrame para consistencia."""

    def __init__(self):
        self.type_mapper = ColumnTypeMapper()

    def normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("TODO(reto): normalize")
    def _handle_duplicate_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Renombra columnas duplicadas automáticamente (p. ej. 'name', 'name_0')."""
        cols = list(df.columns)
        counts: Dict[str, int] = {}
        new_cols = []
        for col in cols:
            if cols.count(col) > 1:
                idx = counts.get(col, 0)
                counts[col] = idx + 1
                new_cols.append(col if idx == 0 else f"{col}_{idx - 1}")
            else:
                new_cols.append(col)
        df.columns = new_cols
        return df

    def _convert_numeric_columns(self, df: pd.DataFrame) -> List[str]:
        raise NotImplementedError("TODO(reto): _convert_numeric_columns")
    def _convert_categorical_columns(self, df: pd.DataFrame) -> List[str]:
        raise NotImplementedError("TODO(reto): _convert_categorical_columns")
    def _parse_date_columns(self, df: pd.DataFrame) -> List[str]:
        raise NotImplementedError("TODO(reto): _parse_date_columns")

// === ARCHIVO: app/src/serve/pipeline_reporter.py ===
# TODO(reto): archivo stubbeado; implementa los cuerpos.
"""
Generador de reportes de pipeline de transformación de datos.

Produce documentación en formato Markdown con:
- Transformaciones aplicadas
- Ejemplos de datos antes/después
- Validación de preservación de filas
- Warnings para columnas con alta cardinalidad
"""

import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime


def _df_to_markdown(df: pd.DataFrame) -> str:
    """Convierte un DataFrame a tabla Markdown sin dependencias externas."""
    headers = [str(c) for c in df.columns]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in df.itertuples(index=False):
        lines.append("| " + " | ".join(str(v) for v in row) + " |")
    return "\n".join(lines)


class TransformationLog:
    """Registro de transformaciones aplicadas al dataset."""

    def __init__(self):
        self.transformations: List[Dict[str, Any]] = []

    def add_transformation(self, name: str, description: str, columns: List[str]):
        """Registra una transformación aplicada."""
        self.transformations.append({
            'name': name,
            'description': description,
            'columns': columns,
            'timestamp': datetime.now()
        })

    def get_transformations(self) -> List[Dict[str, Any]]:
        """Retorna todas las transformaciones registradas."""
        return self.transformations


class PipelineReporter:
    """Genera reportes en Markdown del pipeline de transformación."""

    HIGH_CARDINALITY_THRESHOLD = 50

    def __init__(self):
        self.transformation_log = TransformationLog()

    def generate_report(self, original_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> str:
        raise NotImplementedError("TODO(reto): generate_report")
    def _generate_summary_section(self, original_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> str:
        """Genera la sección de resumen del reporte."""
        lines = []
        lines.append("## Resumen\n")
        lines.append(f"- **Filas originales:** {len(original_df)}\n")
        lines.append(f"- **Filas procesadas:** {len(cleaned_df)}\n")
        lines.append(f"- **Columnas originales:** {len(original_df.columns)}\n")
        lines.append(f"- **Columnas procesadas:** {len(cleaned_df.columns)}\n")
        lines.append("\n")
        return ''.join(lines)

    def _generate_row_validation_section(self, original_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> str:
        """Genera la sección de validación de preservación de filas."""
        lines = []
        lines.append("## Validación de Filas\n")
        original_rows = len(original_df)
        cleaned_rows = len(cleaned_df)

        if original_rows == cleaned_rows:
            lines.append(f"✅ **Filas preservadas:** {original_rows} filas en ambos conjuntos\n")
        else:
            lines.append(f"⚠️ **Diferencia en filas:** {original_rows} → {cleaned_rows} (diferencia: {abs(original_rows - cleaned_rows)})\n")

        lines.append("\n")
        return ''.join(lines)

    def _generate_column_comparison_section(self, original_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> str:
        """Genera la sección de comparación de columnas."""
        lines = []
        lines.append("## Comparación de Columnas\n")

        original_cols = set(original_df.columns)
        cleaned_cols = set(cleaned_df.columns)

        added_cols = cleaned_cols - original_cols
        removed_cols = original_cols - cleaned_cols

        if added_cols:
            lines.append(f"**Columnas agregadas:** {', '.join(sorted(added_cols))}\n")

        if removed_cols:
            lines.append(f"**Columnas eliminadas:** {', '.join(sorted(removed_cols))}\n")

        if not added_cols and not removed_cols:
            lines.append("**Sin cambios en columnas**\n")

        lines.append("\n")
        return ''.join(lines)

    def _generate_transformation_examples(self, original_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> str:
        raise NotImplementedError("TODO(reto): _generate_transformation_examples")
    def _generate_high_cardinality_warnings(self, df: pd.DataFrame) -> str:
        """Genera warnings para columnas con alta cardinalidad."""
        lines = []
        lines.append("## Warnings de Cardinalidad\n")

        high_cardinality_cols = []
        for col in df.columns:
            if isinstance(df[col].dtype, pd.CategoricalDtype):
                unique_count = df[col].cat.categories.size
                if unique_count > self.HIGH_CARDINALITY_THRESHOLD:
                    high_cardinality_cols.append((col, unique_count))

        if high_cardinality_cols:
            for col, count in high_cardinality_cols:
                lines.append(f"⚠️ **{col}:** {count} valores únicos (alta cardinalidad)\n")
        else:
            lines.append("✅ No se detectaron columnas con alta cardinalidad\n")

        lines.append("\n")
        return ''.join(lines)

    def _generate_unknown_columns_warning(self, original_df: pd.DataFrame, cleaned_df: pd.DataFrame) -> str:
        """Genera advertencia para columnas no esperadas."""
        lines = []
        lines.append("## Columnas Desconocidas\n")

        expected_columns = {
            'customer_id', 'transaction_date', 'amount',
            'product_category', 'payment_method'
        }

        all_columns = set(original_df.columns) | set(cleaned_df.columns)
        unknown_columns = all_columns - expected_columns

        if unknown_columns:
            lines.append("⚠️ **Columnas no reconocidas en el esquema:**\n")
            for col in sorted(unknown_columns):
                lines.append(f"  - {col}\n")
        else:
            lines.append("✅ Todas las columnas coinciden con el esquema esperado\n")

        lines.append("\n")
        return ''.join(lines)

// === ARCHIVO: tests/acceptance/test_f1.py ===
"""
Pruebas de aceptación para la fase 1: Identificación de problemas en los datos.
"""

import pandas as pd
import numpy as np
import pytest
from app.src.data.data_quality_reporter import DataQualityReporter

def test_informe_con_valores_faltantes_detectados():
    """Caso: Informe con valores faltantes detectados."""
    # Arrange
    data = {
        'customer_id': ['1', '2', None, '4'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'amount': [100.0, 200.0, 300.0, None],
        'product_category': ['electronics', 'clothing', None, 'groceries'],
        'payment_method': ['credit_card', 'debit_card', 'cash', 'bank_transfer']
    }
    df = pd.DataFrame(data)
    reporter = DataQualityReporter()

    # Act
    report = reporter.generate_report(df)

    # Assert
    assert report["total_records"] == 4
    assert report["missing_values"]["customer_id"] == 25.0
    assert report["missing_values"]["amount"] == 25.0
    assert report["missing_values"]["product_category"] == 25.0
    assert report["duplicate_records"] == 0

def test_informe_con_valores_atipicos_detectados():
    """Caso: Informe con valores atípicos detectados."""
    # Arrange
    data = {
        'customer_id': ['1', '2', '3', '4'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'amount': [100.0, 200.0, 300.0, 10000.0],  # 10000 es un valor atípico
        'product_category': ['electronics', 'clothing', 'groceries', 'furniture'],
        'payment_method': ['credit_card', 'debit_card', 'cash', 'bank_transfer']
    }
    df = pd.DataFrame(data)
    reporter = DataQualityReporter()

    # Act
    report = reporter.generate_report(df)

    # Assert
    assert report["outliers"]["amount"]["outlier_count"] == 1
    assert report["outliers"]["amount"]["outlier_percentage"] == 25.0

def test_manejo_de_dataset_vacio():
    """Caso: Manejo de dataset vacío."""
    # Arrange
    df = pd.DataFrame()
    reporter = DataQualityReporter()

    # Act
    report = reporter.generate_report(df)

    # Assert
    assert report["total_records"] == 0
    assert report["missing_values"] == {}
    assert report["outliers"] == {}

def test_validacion_de_esquema_esperado():
    """Caso: Validación de esquema esperado."""
    # Arrange
    data = {
        'customer_id': ['1', '2', '3'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'amount': [100.0, 200.0, 300.0],
        'product_category': ['electronics', 'clothing', 'groceries'],
        'invalid_column': ['a', 'b', 'c']  # Columna inesperada
    }
    df = pd.DataFrame(data)
    reporter = DataQualityReporter()

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        reporter.generate_report(df)
    assert "Columnas inesperadas: ['invalid_column']" in str(excinfo.value)

// === ARCHIVO: tests/acceptance/test_f2.py ===
"""
Pruebas de aceptación para la fase 2: Tratamiento de valores faltantes y atípicos.
"""

import pandas as pd
import numpy as np
import pytest
from app.src.features.data_cleaner import DataCleaner

def test_imputacion_de_valores_faltantes_numericos():
    """Caso: Imputación de valores faltantes numéricos."""
    # Arrange
    data = {
        'customer_id': ['1', '2', '3', '4'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'amount': [100.0, 200.0, None, 400.0],
        'product_category': ['electronics', 'clothing', 'groceries', 'furniture'],
        'payment_method': ['credit_card', 'debit_card', 'cash', 'bank_transfer']
    }
    df = pd.DataFrame(data)
    cleaner = DataCleaner()

    # Act
    df_clean = cleaner.clean(df)

    # Assert
    assert df_clean['amount'].isna().sum() == 0
    assert df_clean['amount'].iloc[2] == df_clean['amount'].median()

def test_imputacion_de_valores_faltantes_categoricos():
    """Caso: Imputación de valores faltantes categóricos."""
    # Arrange
    data = {
        'customer_id': ['1', '2', '3', '4'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'amount': [100.0, 200.0, 300.0, 400.0],
        'product_category': ['electronics', None, 'groceries', 'furniture'],
        'payment_method': ['credit_card', 'debit_card', 'cash', 'bank_transfer']
    }
    df = pd.DataFrame(data)
    cleaner = DataCleaner()

    # Act
    df_clean = cleaner.clean(df)

    # Assert
    assert df_clean['product_category'].isna().sum() == 0
    assert df_clean['product_category'].iloc[1] == df_clean['product_category'].mode()[0]

def test_tratamiento_de_valores_atipicos():
    """Caso: Tratamiento de valores atípicos."""
    # Arrange
    data = {
        'customer_id': ['1', '2', '3', '4'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'amount': [100.0, 200.0, 300.0, 10000.0],  # 10000 es un valor atípico
        'product_category': ['electronics', 'clothing', 'groceries', 'furniture'],
        'payment_method': ['credit_card', 'debit_card', 'cash', 'bank_transfer']
    }
    df = pd.DataFrame(data)
    # Cuantiles calculados sobre los datos originales (los límites del capping)
    q05 = df['amount'].quantile(0.05)
    q95 = df['amount'].quantile(0.95)
    cleaner = DataCleaner()

    # Act
    df_clean = cleaner.clean(df)

    # Assert
    assert df_clean['amount'].max() <= q95
    assert df_clean['amount'].min() >= q05

def test_validacion_de_esquema_fallida():
    """Caso: Validación de esquema fallida."""
    # Arrange
    data = {
        'customer_id': ['1', '2', '3'],
        'transaction_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
        'amount': [100.0, 200.0, 300.0],
        'product_category': ['electronics', 'clothing', 'groceries'],
        'invalid_column': ['a', 'b', 'c']  # Columna inesperada
    }
    df = pd.DataFrame(data)
    cleaner = DataCleaner()

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        cleaner.clean(df)
    assert "Columnas inesperadas: ['invalid_column']" in str(excinfo.value)

// === ARCHIVO: tests/acceptance/test_f3.py ===
"""
Pruebas de aceptación para la fase f3 - Normalización de tipos de datos.

Verifica que el normalizador de tipos convierta correctamente:
- Columnas numéricas a float64
- Columnas categóricas a category
- Columnas de fecha a datetime64[ns]
- Maneje errores de conversión
- Renombre columnas duplicadas
"""

import pytest
import pandas as pd
import numpy as np
from app.src.features.data_type_normalizer import DataTypeNormalizer


class TestDataTypeNormalizer:
    """Suite de pruebas para DataTypeNormalizer."""

    def test_conversion_de_columnas_numericas(self):
        """Caso 1: Conversión de columnas numéricas."""
        data = {
            'amount': ['100.5', '200.75', '300.0'],
            'quantity': ['1', '2', '3'],
            'name': ['A', 'B', 'C']
        }
        df = pd.DataFrame(data)
        normalizer = DataTypeNormalizer()

        result = normalizer.normalize(df)

        assert pd.api.types.is_float_dtype(result['amount']), "amount debe ser float64"
        assert pd.api.types.is_float_dtype(result['quantity']), "quantity debe ser float64"
        assert result['amount'].iloc[0] == 100.5
        assert result['quantity'].iloc[0] == 1.0

    def test_conversion_de_columnas_categoricas(self):
        """Caso 2: Conversión de columnas categóricas."""
        data = {
            'customer_id': ['C001', 'C002', 'C003'],
            'product_category': ['electronics', 'clothing', 'groceries'],
            'payment_method': ['credit_card', 'debit_card', 'cash']
        }
        df = pd.DataFrame(data)
        normalizer = DataTypeNormalizer()

        result = normalizer.normalize(df)

        assert pd.api.types.is_categorical_dtype(result['customer_id']), "customer_id debe ser category"
        assert pd.api.types.is_categorical_dtype(result['product_category']), "product_category debe ser category"
        assert pd.api.types.is_categorical_dtype(result['payment_method']), "payment_method debe ser category"

    def test_parseo_de_columnas_de_fecha(self):
        """Caso 3: Parseo de columnas de fecha."""
        data = {
            'transaction_date': ['2024-01-15', '2024-02-20', '2024-03-25'],
            'created_at': ['2024-01-01 10:00:00', '2024-01-02 11:00:00', '2024-01-03 12:00:00'],
            'amount': [100, 200, 300]
        }
        df = pd.DataFrame(data)
        normalizer = DataTypeNormalizer()

        result = normalizer.normalize(df)

        assert pd.api.types.is_datetime64_any_dtype(result['transaction_date']), "transaction_date debe ser datetime64[ns]"
        assert pd.api.types.is_datetime64_any_dtype(result['created_at']), "created_at debe ser datetime64[ns]"

    def test_manejo_de_error_en_conversion_de_tipo(self):
        """Caso 4: Manejo de error en conversión de tipo."""
        data = {
            'amount': ['100', 'invalid', '300'],
            'name': ['A', 'B', 'C']
        }
        df = pd.DataFrame(data)
        normalizer = DataTypeNormalizer()

        with pytest.raises(ValueError) as exc_info:
            normalizer.normalize(df)

        assert 'amount' in str(exc_info.value).lower()
        assert 'numérico' in str(exc_info.value) or 'numeric' in str(exc_info.value).lower()

    def test_manejo_de_columnas_duplicadas(self):
        """Caso 5: Manejo de columnas duplicadas."""
        # Un dict literal no admite claves repetidas, por eso se construye
        # el DataFrame con una lista de filas y nombres de columna duplicados.
        df = pd.DataFrame(
            [['A', 'D', 100], ['B', 'E', 200], ['C', 'F', 300]],
            columns=['name', 'name', 'amount']
        )
        normalizer = DataTypeNormalizer()

        result = normalizer.normalize(df)

        assert 'name' in result.columns
        assert 'name_0' in result.columns or 'name_1' in result.columns
        assert len(result.columns) == len(set(result.columns))

    def test_dataframe_vacio(self):
        """Verifica que maneja DataFrame vacío."""
        df = pd.DataFrame()
        normalizer = DataTypeNormalizer()

        with pytest.raises(ValueError) as exc_info:
            normalizer.normalize(df)

        assert 'vacío' in str(exc_info.value).lower() or 'empty' in str(exc_info.value).lower()

    def test_columnas_mixtas(self):
        """Verifica conversión de DataFrame con tipos mixtos."""
        data = {
            'transaction_date': ['2024-01-15', '2024-02-20', '2024-03-25'],
            'amount': ['100.5', '200.75', '300.0'],
            'customer_id': ['C001', 'C002', 'C003'],
            'product_category': ['electronics', 'clothing', 'groceries'],
            'payment_method': ['credit_card', 'debit_card', 'cash']
        }

// === ARCHIVO: tests/acceptance/test_f4.py ===
"""
Pruebas de aceptación para la fase f4 - Documentación del pipeline.

Verifica que el reporter genere:
- Reporte con transformaciones aplicadas
- Ejemplos de datos antes/después
- Validación de preservación de filas
- Warnings para columnas con alta cardinalidad
- Manejo de columnas desconocidas
"""

import pytest
import pandas as pd
import numpy as np
from app.src.serve.pipeline_reporter import PipelineReporter


class TestPipelineReporter:
    """Suite de pruebas para PipelineReporter."""

    def test_reporte_con_transformaciones_aplicadas(self):
        """Caso 1: Reporte con transformaciones aplicadas."""
        original_data = {
            'customer_id': ['C001', 'C002', 'C003'],
            'transaction_date': ['2024-01-15', '2024-02-20', '2024-03-25'],
            'amount': [100.0, 200.0, 300.0],
            'product_category': ['electronics', 'clothing', 'groceries'],
            'payment_method': ['credit_card', 'debit_card', 'cash']
        }
        cleaned_data = {
            'customer_id': pd.Categorical(['C001', 'C002', 'C003']),
            'transaction_date': pd.to_datetime(['2024-01-15', '2024-02-20', '2024-03-25']),
            'amount': pd.array([100.0, 200.0, 300.0], dtype='float64'),
            'product_category': pd.Categorical(['electronics', 'clothing', 'groceries']),
            'payment_method': pd.Categorical(['credit_card', 'debit_card', 'cash'])
        }

        original_df = pd.DataFrame(original_data)
        cleaned_df = pd.DataFrame(cleaned_data)

        reporter = PipelineReporter()
        report = reporter.generate_report(original_df, cleaned_df)

        assert '## Resumen' in report
        assert '## Validación de Filas' in report
        assert '## Comparación de Columnas' in report
        assert '## Ejemplos de Transformaciones' in report

    def test_ejemplos_de_datos_antes_despues(self):
        """Caso 2: Ejemplos de datos antes/después."""
        original_data = {
            'amount': ['100', '200', '300'],
            'name': ['A', 'B', 'C']
        }
        cleaned_data = {
            'amount': pd.array([100.0, 200.0, 300.0], dtype='float64'),
            'name': ['A', 'B', 'C']
        }

        original_df = pd.DataFrame(original_data)
        cleaned_df = pd.DataFrame(cleaned_data)

        reporter = PipelineReporter()
        report = reporter.generate_report(original_df, cleaned_df)

        assert '### Datos Originales' in report
        assert '### Datos Procesados' in report
        assert '100' in report
        assert '200' in report

    def test_validacion_de_preservacion_de_filas(self):
        """Caso 3: Validación de preservación de filas."""
        original_df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': ['a', 'b', 'c', 'd', 'e']
        })
        cleaned_df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': ['a', 'b', 'c', 'd', 'e']
        })

        reporter = PipelineReporter()
        report = reporter.generate_report(original_df, cleaned_df)

        assert 'Filas preservadas' in report or '✅' in report
        assert '5' in report

    def test_validacion_de_perdida_de_filas(self):
        """Verifica que detecta pérdida de filas."""
        original_df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': ['a', 'b', 'c', 'd', 'e']
        })
        cleaned_df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })

        reporter = PipelineReporter()
        report = reporter.generate_report(original_df, cleaned_df)

        assert 'Diferencia' in report or '⚠️' in report

    def test_manejo_de_datasets_con_esquemas_desconocidos(self):
        """Caso 4: Manejo de datasets con esquemas desconocidos."""
        original_df = pd.DataFrame({
            'customer_id': ['C001', 'C002'],
            'transaction_date': ['2024-01-15', '2024-02-20'],
            'unknown_column': [1, 2],
            'another_unknown': ['x', 'y']
        })
        cleaned_df = pd.DataFrame({
            'customer_id': pd.Categorical(['C001', 'C002']),
            'transaction_date': pd.to_datetime(['2024-01-15', '2024-02-20']),
            'unknown_column': [1, 2],
            'another_unknown': ['x', 'y']
        })

        reporter = PipelineReporter()
        report = reporter.generate_report(original_df, cleaned_df)

        assert '## Columnas Desconocidas' in report
        assert 'unknown_column' in report or 'another_unknown' in report
        assert '⚠️' in report

    def test_warning_para_alta_cardinalidad(self):
        """Caso 5: Warning para alta cardinalidad."""
        high_cardinality_data = {
            'customer_id': pd.Categorical([f'C{i:04d}' for i in range(100)]),
            'amount': [100.0] * 100
        }
        df = pd.DataFrame(high_cardinality_data)

        reporter = PipelineReporter()
        report = reporter.generate_report(df, df)

        assert '## Warnings de Cardinalidad' in report
        assert 'customer_id' in report
        assert '⚠️' in report

    def test_sin_warning_para_baja_cardinalidad(self):
        """Verifica que no genera warning para baja cardinalidad."""
        low_cardinality_data = {
            'product_category': pd.Categorical(['electronics', 'clothing', 'groceries']),
            'amount': [100.0, 200.0, 300.0]
        }
        df = pd.DataFrame(low_cardinality_data)

        reporter = PipelineReporter()
        report = reporter.generate_report(df, df)

        assert '## Warnings de Cardinalidad' in report
        assert '✅' in report or 'No se detectaron' in report

    def test_manejo_de_dataframe_none(self):
        """Verifica que maneja DataFrame None."""
        reporter = PipelineReporter()

        with pytest.raises(ValueError):
            reporter.generate_report(None, pd.DataFrame({'a': [1]}))

        with pytest.raises(ValueError):
            reporter.generate_report(pd.DataFrame({'a': [1]}), None)

    def test_reporte_contiene_todas_las_secciones(self):
        """Verifica que el reporte contiene todas las secciones esperadas."""
        df = pd.DataFrame({
            'customer_id': ['C001', 'C002'],
            'transaction_date': ['2024-01-15', '2024-02-20'],
            'amount': [100.0, 200.0]
        })

        reporter = PipelineReporter()
        report = reporter.generate_report(df, df)

        assert '# Reporte de Pipeline de Datos' in report
        assert '## Resumen' in report
        assert '## Validación de Filas' in report
        assert '## Comparación de Columnas' in report
        assert '## Ejemplos de Transformaciones' in report
        assert '## Warnings de Cardinalidad' in report
        assert '## Columnas Desconocidas' in report

// === ARCHIVO: app/src/serve/main.py ===
"""
Punto de entrada para el pipeline de limpieza de datos.
Orquesta la carga, limpieza, transformación y generación de reportes.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.src.data.data_loader import DataLoader
from app.src.data.data_quality_reporter import DataQualityReporter
from app.src.features.data_cleaner import DataCleaner
from app.src.features.data_type_normalizer import DataTypeNormalizer
from app.src.serve.pipeline_reporter import PipelineReporter


def main():
    """
    Ejecuta el pipeline completo de limpieza de datos.
    """
    source_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'transactions.csv')
    
    print("=== Pipeline de Limpieza de Datos ===\n")
    
    print("1. Cargando datos...")
    loader = DataLoader(source_path=source_path, source_type='csv')
    df = loader.load_data()
    print(f"   Registros cargados: {len(df)}")
    print(f"   Columnas: {list(df.columns)}\n")
    
    print("2. Generando reporte de calidad inicial...")
    quality_reporter = DataQualityReporter()
    quality_report = quality_reporter.generate_report(df)
    
    report_path = os.path.join(os.path.dirname(__file__), '..', '..', 'reports', 'data_quality_report.md')
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Reporte de Calidad de Datos\n\n")
        f.write(f"## Resumen General\n\n")
        f.write(f"- **Total de registros:** {quality_report.get('total_records', len(df))}\n")
        f.write(f"- **Registros duplicados:** {quality_report.get('duplicate_records', 0)}\n\n")
        
        missing = quality_report.get('missing_values', {})
        if missing:
            f.write("## Valores Faltantes\n\n")
            f.write("| Columna | Cantidad | Porcentaje |\n")
            f.write("|---------|----------|------------|\n")
            for col, stats in missing.items():
                pct = stats.get('percentage', 0)
                count = stats.get('count', 0)
                f.write(f"| {col} | {count} | {pct:.2f}% |\n")
            f.write("\n")
        
        outliers = quality_report.get('outliers', {})
        if outliers:
            f.write("## Valores Atípicos Detectados\n\n")
            f.write("| Columna | Cantidad | Rango |\n")
            f.write("|---------|----------|-------|\n")
            for col, stats in outliers.items():
                count = stats.get('count', 0)
                lower = stats.get('lower_bound', 0)
                upper = stats.get('upper_bound', 0)
                f.write(f"| {col} | {count} | [{lower:.2f}, {upper:.2f}] |\n")
            f.write("\n")
        
        f.write("## Recomendaciones\n\n")
        if missing:
            f.write("- Aplicar imputación para valores faltantes\n")
        if outliers:
            f.write("- Aplicar capping para valores atípicos\n")
        if not missing and not outliers:
            f.write("- No se requieren transformaciones de limpieza\n")
    
    print(f"   Reporte guardado en: {report_path}\n")
    
    print("3. Limpiando datos (tratando valores faltantes y atípicos)...")
    cleaner = DataCleaner()
    df_cleaned = cleaner.clean(df)
    print(f"   Registros después de limpieza: {len(df_cleaned)}\n")
    
    print("4. Normalizando tipos de datos...")
    normalizer = DataTypeNormalizer()
    df_normalized = normalizer.normalize(df_cleaned)
    print(f"   Tipos normalizados correctamente\n")
    
    print("5. Generando reporte del pipeline...")
    pipeline_reporter = PipelineReporter()
    pipeline_report = pipeline_reporter.generate_report(df, df_normalized)
    
    pipeline_report_path = os.path.join(os.path.dirname(__file__), '..', '..', 'reports', 'pipeline_report.md')
    with open(pipeline_report_path, 'w', encoding='utf-8') as f:
        f.write(pipeline_report)
    
    print(f"   Reporte guardado en: {pipeline_report_path}\n")
    
    print("=== Pipeline completado exitosamente ===")
    
    return df_normalized


if __name__ == '__main__':
    main()

// === ARCHIVO: app/reports/data_quality_report.md ===
# Reporte de Calidad de Datos

## Resumen General

- **Total de registros:** 0
- **Registros duplicados:** 0

## Valores Faltantes

| Columna | Cantidad | Porcentaje |
|---------|----------|------------|

## Valores Atípicos Detectados

| Columna | Cantidad | Rango |

## Recomendaciones

- Ejecutar el pipeline para generar el reporte con datos reales
```
