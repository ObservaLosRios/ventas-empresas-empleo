# Proyecto ETL: Ventas, Empresas y Empleo

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) robusto y escalable para procesar datos de ventas, empresas y empleo.

## Estructura del Proyecto

El proyecto sigue una estructura estándar de Data Science:

```
├── data/               # Datos del proyecto
│   ├── raw/            # Datos originales (inmutables)
│   └── processed/      # Datos limpios y procesados
├── docs/               # Documentación del proyecto
├── notebooks/          # Jupyter Notebooks para exploración y análisis
├── scripts/            # Scripts de utilidad o ejecución única
├── src/                # Código fuente del proyecto
│   ├── etl/            # Módulos del pipeline ETL
│   └── utils/          # Utilidades compartidas
├── main.py             # Punto de entrada principal
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

## Configuración

1.  **Entorno Virtual**: Se recomienda usar un entorno virtual.
2.  **Dependencias**: Instalar con `pip install -r requirements.txt`.

## Ejecución

Para ejecutar el pipeline ETL completo:

```bash
python main.py
```

## Visualización

El proyecto incluye un dashboard interactivo generado con Highcharts para visualizar los datos procesados.

- **Dashboard**: `docs/index.html`
- **Características**:
    - Ventas Promedio por Comuna (Top 15)
    - Trabajadores Promedio por Comuna (Top 15)
    - Evolución de Ventas Efectivas por Región (Biobío, La Araucanía, Los Ríos, Los Lagos)
    - Evolución de Empleo por Región

## Principios de Diseño

- **SOLID**: Arquitectura modular y extensible.
- **Clean Code**: Código legible y mantenible.
- **Logging**: Trazabilidad completa del proceso.
