
## Visión general del Proyecto
Desarrollo de una plataforma web para la gestión, seguimiento y análisis de carteras de inversión financiera, orientada a inversores particulares con cuentas multiactivo y multidivisa, con especial énfasis en el cumplimiento fiscal en España (IRPF/FIFO y Modelo 720).

---

## Requisitos del Sistema

### Requisitos funcionales

- **Gestión de Transacciones:**
	- Registro completo del ciclo de vida de operaciones (compras, ventas, dividendos, comisiones, splits y transferencias).
	- Soporte de derivados financieros básicos (opciones y futuros), gestionando su fecha de expiración y resultado al vencimiento o cierre anticipado.
- **Entorno Multidivisa:** Gestión de cuentas denominadas en diferentes divisas (EUR, USD y GBP) con trazabilidad del tipo de cambio histórico en la fecha de liquidación.
- **Fiscalidad Española:**
	- **Ganancias y Pérdidas Patrimoniales:** Motor determinista con criterio FIFO homogéneo y conversión al cambio oficial del BCE a fecha de devengo para ventas de acciones y cierre de derivados.
	-  **Rendimiento de Dividendos:** Tratamiento fiscal diferenciado de dividendos y cálculo de la deducción por doble imposición internacional (retenciones en origen vs. destino).
- **Modelo 720:** Generación de información sobre cuentas y valores situados en el extranjero frente al umbral conjunto de 50.000 € establecido por la normativa (saldo a 31 de diciembre y saldo medio del último trimestre)
- **Análisis de cartera y métricas:** Desglose visual por sector económico e industrias, exposición geográfica por países y distribución por divisas y clases de activos (acciones, ETF, liquidez).
- **Módulo de Ingesta:** Arquitectura basada en parsers, tomando como plataforma de referencia principal Interactive Brokers (informes de actividad) y extensible a brokers habituales (Trade Republic, MyInvestor), complementado con plantilla canónica (CSV/Excel) y entrada manual.

### Requisitos no funcionales
- **Multiplataforma y Accesibilidad:** Acceso fluido desde escritorio, tablets y dispositivos móviles.
- **Precisión numérica:** Cero tolerancia a errores de redondeo.
- **Integridad y Control de Duplicados:** Detección y prevención de registros duplicados en importaciones masivas. 

---

## Propuesta tecnológica 

#### Backend
- **Framework - FastAPI:** Procesamiento asíncrono nativo, validación estricta de esquemas y documentación OpenAPI/Swagger automática.
- **Manipulación y Análisis de Datos - Pandas + Numpy:** Transformación vectorizada de series temporales de precios, agregaciones por sector/país y cálculo ágil de rentabilidades.
- **Precisión numérica - `decimal.Decimal`:** Aritmética de coma fija de precisión arbitraria, eliminando por diseño los errores de redondeo.
- **ORM y Persistencia - SQLAlchemy + Alembic:** Mapeo relacional tipado y gestión controlada de migraciones de esquema de base de datos.
- **Testing - pytest:** Suite de pruebas unitarias parametrizadas.

#### Frontend
- **Framework - React:** Tiempo de compilación instantáneo en desarrollo y garantiza consistencia de contratos con DTOs de FastAPI.
- **Diseño y Adaptabilidad Multiplataforma - Tailwind CSS:** Estrategia _mobile-first_ mediante clases utilitarias para que una única aplicación se ajuste de forma nativa a pantalla de escritorio, tabletas y smartphones sin duplicar código.
- **Capacidades PWA - `vite-plugin-pwa`:** Service Worker para que la web sea instalable en Android, iOS o Windows con experiencia visual de app nativa.
- **Visualización Gráfica - Recharts:** Componentes declarativos ligeros para desgloses en tarta y gráficos temporales de evolución de cartera.

#### Persistencia y Almacenamiento: PostgreSQL
- **Motor relacional - PostgreSQL:** Cumplimiento estricto de transacciones ACID e integridad referencial, con tipos nativos para importes y tipos de cambio oficiales.
- **Caché (Opcional) - Redis:** Almacenamiento en memoria de cotizaciones y tipos de cambio diarios para no penalizar el tiempo de respuesta ni saturar APIs externas.

#### Fuentes de Datos y Parseo de Extractos
- **Tipo de Cambio Oficial - Frankfurter API:** Datos oficiales diarios EUR/divisas, gratuitos y sin límites restrictivos de uso.
- **Datos de Mercado y Activo - `yfinance`:** Descarga históricos diarios de precios, dividendos y metadatos de activos.
- **Módulos de Ingesta:**
	- **Interactive Brokers:** Parser a medida para informes de actividad.
	- **Librerías de Ingesta:** `pandas`, `openpyxl` (para Excel) y `defusedxml` (para XML).

#### Entorno y Despliegue
- **Contenedorización - Docker + Docker Compose:** Definición de tres servicios (`backend`, `frontend`, `db`) que se levantan con un único comando (`docker compose up --build`), garantizando portabilidad total.

