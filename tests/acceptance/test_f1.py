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