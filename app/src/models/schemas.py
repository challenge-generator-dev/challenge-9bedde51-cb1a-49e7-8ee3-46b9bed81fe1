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