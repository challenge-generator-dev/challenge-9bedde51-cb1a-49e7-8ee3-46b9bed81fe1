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