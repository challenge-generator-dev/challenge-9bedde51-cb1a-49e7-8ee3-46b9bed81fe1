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