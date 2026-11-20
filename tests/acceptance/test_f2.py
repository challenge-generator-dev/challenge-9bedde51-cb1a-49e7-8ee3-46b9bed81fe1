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