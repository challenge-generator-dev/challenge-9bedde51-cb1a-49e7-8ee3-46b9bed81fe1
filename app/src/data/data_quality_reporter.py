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