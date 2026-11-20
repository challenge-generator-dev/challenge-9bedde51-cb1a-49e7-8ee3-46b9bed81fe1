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