"""
Punto de entrada para el pipeline de limpieza de datos.
Orquesta la carga, limpieza, transformación y generación de reportes.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app.src.data.data_loader import DataLoader
from app.src.data.data_quality_reporter import DataQualityReporter
from app.src.features.data_cleaner import DataCleaner
from app.src.features.data_type_normalizer import DataTypeNormalizer
from app.src.serve.pipeline_reporter import PipelineReporter


def main():
    """
    Ejecuta el pipeline completo de limpieza de datos.
    """
    source_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'transactions.csv')
    
    print("=== Pipeline de Limpieza de Datos ===\n")
    
    print("1. Cargando datos...")
    loader = DataLoader(source_path=source_path, source_type='csv')
    df = loader.load_data()
    print(f"   Registros cargados: {len(df)}")
    print(f"   Columnas: {list(df.columns)}\n")
    
    print("2. Generando reporte de calidad inicial...")
    quality_reporter = DataQualityReporter()
    quality_report = quality_reporter.generate_report(df)
    
    report_path = os.path.join(os.path.dirname(__file__), '..', '..', 'reports', 'data_quality_report.md')
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Reporte de Calidad de Datos\n\n")
        f.write(f"## Resumen General\n\n")
        f.write(f"- **Total de registros:** {quality_report.get('total_records', len(df))}\n")
        f.write(f"- **Registros duplicados:** {quality_report.get('duplicate_records', 0)}\n\n")
        
        missing = quality_report.get('missing_values', {})
        if missing:
            f.write("## Valores Faltantes\n\n")
            f.write("| Columna | Cantidad | Porcentaje |\n")
            f.write("|---------|----------|------------|\n")
            for col, stats in missing.items():
                pct = stats.get('percentage', 0)
                count = stats.get('count', 0)
                f.write(f"| {col} | {count} | {pct:.2f}% |\n")
            f.write("\n")
        
        outliers = quality_report.get('outliers', {})
        if outliers:
            f.write("## Valores Atípicos Detectados\n\n")
            f.write("| Columna | Cantidad | Rango |\n")
            f.write("|---------|----------|-------|\n")
            for col, stats in outliers.items():
                count = stats.get('count', 0)
                lower = stats.get('lower_bound', 0)
                upper = stats.get('upper_bound', 0)
                f.write(f"| {col} | {count} | [{lower:.2f}, {upper:.2f}] |\n")
            f.write("\n")
        
        f.write("## Recomendaciones\n\n")
        if missing:
            f.write("- Aplicar imputación para valores faltantes\n")
        if outliers:
            f.write("- Aplicar capping para valores atípicos\n")
        if not missing and not outliers:
            f.write("- No se requieren transformaciones de limpieza\n")
    
    print(f"   Reporte guardado en: {report_path}\n")
    
    print("3. Limpiando datos (tratando valores faltantes y atípicos)...")
    cleaner = DataCleaner()
    df_cleaned = cleaner.clean(df)
    print(f"   Registros después de limpieza: {len(df_cleaned)}\n")
    
    print("4. Normalizando tipos de datos...")
    normalizer = DataTypeNormalizer()
    df_normalized = normalizer.normalize(df_cleaned)
    print(f"   Tipos normalizados correctamente\n")
    
    print("5. Generando reporte del pipeline...")
    pipeline_reporter = PipelineReporter()
    pipeline_report = pipeline_reporter.generate_report(df, df_normalized)
    
    pipeline_report_path = os.path.join(os.path.dirname(__file__), '..', '..', 'reports', 'pipeline_report.md')
    with open(pipeline_report_path, 'w', encoding='utf-8') as f:
        f.write(pipeline_report)
    
    print(f"   Reporte guardado en: {pipeline_report_path}\n")
    
    print("=== Pipeline completado exitosamente ===")
    
    return df_normalized


if __name__ == '__main__':
    main()