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