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