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