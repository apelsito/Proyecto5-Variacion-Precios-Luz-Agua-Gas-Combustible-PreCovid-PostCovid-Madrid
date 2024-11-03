# 📊 Evolución de los Precios de Agua, Luz, Gas y Combustibles en la Comunidad de Madrid (2019-2022)

# Descripción del Proyecto 💡

## 🎯 Objetivo
Este proyecto tiene como objetivo analizar cómo el COVID-19 impactó los precios de servicios esenciales como la luz, el gas, el agua y los combustibles en la Comunidad de Madrid. Observaremos cómo, durante la pandemia, la reducción en la demanda generó una caída en los precios, y cómo, tras el levantamiento de las restricciones y la recuperación económica, estos mismos servicios experimentaron un aumento significativo. Además, evaluaremos otros factores como los conflictos geopolíticos y las tensiones en la cadena de suministro que han contribuido a una subida sostenida de precios a partir de 2021. Este análisis busca proporcionar una comprensión más profunda de cómo estos eventos globales han afectado el coste de vida.

## Estructura del Proyecto 🗂️

```bash
ImpactoCOVID-PreciosMadrid/
├── datos/                          # Archivos de datos CSV, JSON, PDF, SQL, respaldos y consultas.
│   ├── 01_PreciosGas/              # Precios del Gas.
│   ├── 02_PreciosLuz/              # Precios de la Luz.
│   ├── 03_PreciosCombustible/      # Precios de los Combustibles.
│   ├── 04_PreciosAgua/             # Precios del Agua.
│   ├── 05_TablasPreDB/             # CSV con los DataFrames para Crear la Base de Datos
│   ├── 06_TablasPreVisualizacion/  # Tablas con las Consultas
│
├── notebooks/               # Notebooks de Jupyter con el análisis y las visualizaciones.
│
├── src/                     # Archivos .py para funciones auxiliares del proyecto.
│    ├── 01_graficas/        # Gráficas Realizadas para el análisis.
│
└── README.md                # Descripción del proyecto, instrucciones de instalación y uso.
```
# Instalación y Requisitos 🛠️
## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.x** 🐍
- **Jupyter Notebook** 📓 para ejecutar y visualizar los análisis de datos
- **Bibliotecas de Python**:
    - [pandas](https://pandas.pydata.org/docs/) para manipulación de datos 🧹
    - [numpy](https://numpy.org/doc/2.1/) para cálculos numéricos 🔢
    - [shutil](https://docs.python.org/es/3/library/shutil.html) para gestión de archivos y directorios, como copiar y mover archivos de manera eficiente 📂
    - [matplotlib](https://matplotlib.org/stable/index.html) para crear gráficos y visualizaciones básicas 📊
    - [seaborn](https://seaborn.pydata.org/) para visualizaciones estadísticas avanzadas y atractivas 📈
    - [requests](https://requests.readthedocs.io/en/latest/) para conectar con FACUA y realizar peticiones HTTP 🌐
    - [selenium](https://www.selenium.dev/documentation/) para interactuar con sitios web dinámicos 💻
    - [pdfplumber](https://github.com/jsvine/pdfplumber) para extraer datos de archivos PDF, útil para analizar reportes de precios en formato PDF 📄
    - [dotenv](https://www.dotenv.org/docs/) para manejar variables de entorno de manera segura 🔐
    - [tqdm](https://tqdm.github.io/) para crear barras de progreso en los procesos largos ⏳
    - [psycopg2](https://www.psycopg.org/docs/) para conectarse y ejecutar consultas en PostgreSQL 🛢️
- **Para crear la Base de Datos**
    - [PostgreSQL](https://www.postgresql.org/) para la gestión y almacenamiento de datos relacionales 📂
    - [DBeaver](https://dbeaver.io/) para administración y consulta visual de bases de datos 🖥️

## Instalación 🛠️

1. Clona este repositorio para visualizarlo en vscode:
```bash
git clone https://github.com/apelsito/Proyecto5-Variacion-Precios-Luz-Agua-Gas-Combustible-PreCovid-PostCovid-Madrid.git
cd Proyecto5-Variacion-Precios-Luz-Agua-Gas-Combustible-PreCovid-PostCovid-Madrid
```
# Desarrollo del Proyecto 🚀

Este proyecto se estructura en varias fases para obtener y analizar datos de precios históricos de gasolina y agua en España.

## Fase 1: Scraping 🔍

### Pasos:
1. **Configuración del Entorno**: Importación de librerías como Selenium y Pandas, y configuración del navegador para descargas automáticas.
2. **Definición de Rango de Fechas**: Creación de listas de fechas de inicio y fin (2019-2022) para organizar la descarga anual de datos de gasolina.
3. **Scraping de Precios de Gasolina**: Uso de Selenium y la función `precios_combustible` para acceder a la web del Ministerio de Energía y descargar datos de diferentes tipos de combustible.
4. **Extracción de Datos en Excel y PDF**: Procesamiento de archivos Excel y PDF (FACUA) con funciones específicas (`excel_a_Dataframe` y `pdf_a_df`) para convertir los datos en DataFrames de Pandas.

### Observaciones 📌
- Se evita la duplicación de archivos sobrescribiendo los existentes.
- Los PDF de FACUA varían ligeramente en formato según el año, lo que requerirá ajustes en la extracción.

# Fase 2: Obtención de Datos con APIs 🔌

En esta segunda fase, se recopilaron datos históricos de precios de gas y electricidad mediante llamadas a APIs específicas. Los datos obtenidos se estructuraron para su análisis posterior.

### Pasos:
1. **Configuración y Importación de Librerías**:
   - Importación de `requests` para realizar llamadas HTTP a las APIs.
   - Uso de `Pandas` para manipular y almacenar los datos obtenidos.

2. **Funciones de Llamada a APIs**:
   - En `SupportApi.py`, se implementaron las siguientes funciones:
     - **`hacer_request_json(url)`**: Realiza la llamada a una URL y maneja errores comunes de conexión, devolviendo la respuesta en formato JSON.
     - **`api_gas(fecha_inicio, fecha_final)`**: Realiza una solicitud a la API de precios de gas, filtrando los datos entre las fechas indicadas. La respuesta se convierte en un DataFrame.
     - **`api_luz(years, ruta_guardado)`**: Recupera los datos de precios de electricidad para los años especificados y guarda los resultados.

3. **Obtención de Datos en el Notebook**:
   - En `02_requests_apis.ipynb`, se usaron las funciones de `SupportApi` para:
     - **Obtener datos de gas**: Llamada a `api_gas` para recuperar y filtrar datos de MIBGAS entre 2019 y 2022.
     - **Obtener datos de electricidad**: Llamada a `api_luz` para obtener datos de precios de electricidad para los años 2019-2022.

### Observaciones 📌
- La API de gas requiere un filtro adicional para seleccionar solo los datos de MIBGAS.
- La función `api_luz` permite guardar los datos directamente, facilitando el acceso y organización de los archivos para su análisis.

# Fase 3: Preparación para Base de Datos 🗄️

En esta fase, se organizan y estructuran los datos en tablas adecuadas para su integración en una base de datos. Este paso es crucial para garantizar un análisis eficiente y facilitar futuras consultas.

### Pasos:
1. **Definición de Tablas**:
   - Se crean las tablas base que incluyen: `fechas`, `combustibles`, `categorías`, `unidades`, y `historico_precios`.
  
2. **Carga de Datos**:
   - Se cargan los datos de gas, electricidad, gasolina y agua desde archivos CSV preprocesados y se estructuran para integrarse en las tablas definidas.

3. **Funciones de Apoyo**:
   - En `SupportPreDB.py`, se implementan funciones para crear diccionarios de mapeo y transformar los datos:
     - **`crear_dictio(df, columna)`**: Crea un diccionario donde las claves son valores únicos de una columna y los valores son los índices correspondientes.
     - **`df_a_db(dictio, df, columna)`**: Usa el diccionario para mapear valores en el DataFrame, facilitando la normalización de los datos.

4. **Organización de Datos en Tablas**:
   - En el Notebook, se crean y estructuran las tablas usando los valores únicos y aplicando los diccionarios de mapeo. Esto prepara los datos para ser cargados en una base de datos relacional.

### Observaciones 📌
- La tabla de `fechas` se crea a partir de valores únicos de las fechas en los datos de gas, asegurando que todos los registros se alineen cronológicamente.
- Las funciones de mapeo permiten transformar datos categóricos en identificadores, optimizando el espacio y la eficiencia en la base de datos.

# Fase 4: Creación de Base de Datos 🗄️

En esta fase, se creó una base de datos en PostgreSQL y se insertaron las tablas con los datos recopilados y organizados en las fases anteriores.

### Pasos:
1. **Configuración de la Conexión**:
   - Se importaron librerías necesarias, como `psycopg2` para la conexión con PostgreSQL y `dotenv` para cargar credenciales desde un archivo `.env`.
   - Variables de conexión (`user`, `password`, `host`, `port`) configuradas para asegurar un acceso seguro.

2. **Funciones de Soporte para Base de Datos**:
   - En `SupportDB.py`, se implementaron funciones clave:
     - **`crear_bd`**: Crea la base de datos en PostgreSQL si no existe.
     - **`conectarse_a_bd`**: Establece la conexión a la base de datos creada.
     - **`modificar_bd`**: Ejecuta comandos SQL para crear tablas o modificar la estructura.
     - **`insertar_muchos_datos_bd`**: Inserta grandes volúmenes de datos en la base de datos.
     - **`generar_tupla`**: Prepara los datos en tuplas para su inserción masiva.

3. **Creación e Inserción de Tablas**:
   - En el Notebook, se ejecutan comandos SQL para crear las tablas y definir sus relaciones.
   - Los datos organizados (fechas, combustibles, categorías, unidades, histórico de precios) se insertan en la base de datos, consolidando toda la información en un solo sistema.

### Observaciones 📌
- La creación y estructura de la base de datos facilitan la consulta y el análisis de datos de manera eficiente.
- Las funciones de inserción masiva optimizan el tiempo de carga, incluso con grandes volúmenes de datos.

# Fase 5: Consultas para Pre-visualización 🔍

En esta fase, se realizan consultas SQL a la base de datos para obtener los datos necesarios para la visualización y análisis final.

### Pasos:
1. **Conexión a la Base de Datos**:
   - Importación de librerías necesarias, como `psycopg2` para acceder a PostgreSQL y `dotenv` para cargar credenciales de forma segura.
   - Establecimiento de la conexión usando las credenciales y funciones de `SupportDB`.

2. **Consultas SQL**:
   - Se emplea la función `consulta_sql` para ejecutar las consultas de selección, obteniendo datos específicos de cada tabla.
   - Extracción de datos de precios históricos y otras métricas clave para la visualización.

3. **Preparación de Datos**:
   - Los resultados de las consultas SQL se transforman en DataFrames de Pandas, lo que facilita la previsualización y preparación para su análisis gráfico.

### Observaciones 📌
- La estructura de las consultas asegura que los datos extraídos estén listos para visualización.
- El uso de DataFrames permite realizar exploraciones rápidas antes de la visualización completa.

# Fase 6: Visualización 📊

En esta última fase, se crean visualizaciones de los datos procesados para analizar la evolución de precios y extraer conclusiones significativas.

### Pasos:
1. **Configuración de Librerías de Visualización**:
   - Importación de `matplotlib` y `seaborn` para la creación de gráficos.
   - Configuración de parámetros para ignorar advertencias y mejorar la visualización.

2. **Gráficos de Evolución de Precios**:
   - **Evolución Anual del Precio Promedio**: Se representa la evolución del precio promedio de agua y combustibles entre 2019 y 2022. 
   - Uso de gráficos de línea con anotaciones para destacar el precio promedio de cada año.

3. **Análisis Visual**:
   - A partir de los gráficos generados, se identifican patrones de variación de precios a lo largo de los años, proporcionando información útil para el análisis de tendencias.

### Observaciones 📌
- Las visualizaciones permiten observar cómo han fluctuado los precios de servicios clave, como el agua y los combustibles, en el periodo de estudio.
- Las anotaciones en los gráficos ayudan a resaltar valores específicos, facilitando la interpretación de los resultados.

# 📊 Análisis de las Gráficas 📊
## 1. 📈 Evolución Anual del Precio Promedio por Servicio (2019-2022)

![Evolución Anual del Precio Promedio por Servicio](src/01_graficas/01_EvolucionAnualPorServicio.png)

### Observaciones:
- **Agua**💧: El precio promedio del agua se mantuvo estable entre 2019 y 2021 (1.57€ a 1.65€), con un aumento notable en 2022 a 1.80€. Este incremento, aunque moderado en comparación con otros servicios, impacta el coste de vida dado su carácter esencial.
- **Combustible**⛽: Después de una bajada notoria en 2020 (1.22€) por la caída de la demanda durante la pandemia, los precios se dispararon en 2021 y 2022, alcanzando 1.87€ en 2022. La recuperación económica y la alta demanda global impulsaron estos aumentos, exacerbados por las restricciones en la oferta y las tensiones internacionales en el sector energético.

---

## 2. 📉 Variación Mensual del Precio Promedio por Servicio (2019-2022)

![Variación Mensual del Precio Promedio por Servicio](src/01_graficas/03_VariaciónMensualPrecioPorServicio.png)

### Observaciones:
- **Agua**💧: Mantiene una estabilidad considerable en su precio mensual hasta 2022. Este servicio esencial experimenta un aumento en el último año, probablemente relacionado con la inflación en el coste de mantenimiento y distribución.
- **Combustibles**⛽: Muestran una gran variabilidad mensual, con aumentos significativos hacia finales de 2021 y 2022, vinculados con problemas de suministro y el encarecimiento de las materias primas como el petróleo.

---

## 3. ⚡ Variación Mensual del Precio Promedio de Luz y Gas (2019-2022)

![Variación Mensual del Precio Promedio de Luz y Gas](src/01_graficas/04_VariaciónMensualPrecioPorServicio.png)

### Observaciones:
- **Luz**💡: Observamos un incremento sostenido en 2021, alcanzando máximos históricos a finales de ese año, y se estabiliza en niveles altos en 2022. Las causas incluyen la creciente demanda de gas natural (utilizado en muchas plantas de generación de electricidad) y el aumento de precios de los derechos de emisión de CO₂ en la Unión Europea, que afectaron el coste de generación.
- **Gas**🔥: Los precios del gas se mantienen relativamente estables hasta principios de 2021, cuando comienzan a escalar significativamente, llegando a un máximo en octubre de 2022. Esta subida está directamente vinculada a la dependencia europea del gas natural ruso y a las interrupciones de suministro derivadas del conflicto en Ucrania y las sanciones impuestas.

---

## 4. 💡 Evolución Mensual del Precio de la Luz

![Evolución Mensual del Precio de la Luz](src/01_graficas/05_EvolucionMensualPrecioLuz.png)

### Observaciones:
- La electricidad ha experimentado una volatilidad extrema, sobre todo a partir de 2021. Los precios subieron rápidamente debido a varios factores, entre ellos:
  - **Aumento de la demanda de gas natural**: Al ser el gas una fuente primaria para la generación de electricidad en Europa, el aumento en sus precios encarece directamente la electricidad.
  - **Mercado de CO₂**🌍: El sistema de comercio de emisiones de la UE incrementa el coste de emisión de gases contaminantes, lo cual encarece la generación de electricidad en plantas tradicionales.
  - **Limitaciones de infraestructura**: La dependencia de fuentes renovables intermitentes como la energía eólica o solar, que no siempre pueden suplir la demanda, obliga a recurrir a plantas de energía más caras.

---

## 5. 🔥 Evolución Mensual del Precio del Gas

![Evolución Mensual del Precio del Gas](src/01_graficas/06_EvolucionPreciosGas.png)

### Observaciones:
- El precio del gas se ha disparado desde mediados de 2021, alcanzando picos a mediados de 2022. Los principales factores detrás de esta subida son:
  - **Conflicto en Ucrania**: La guerra entre Rusia y Ucrania y las subsecuentes sanciones han afectado el suministro de gas a Europa, lo que generó escasez y un aumento de precios.
  - **Alta demanda post-pandemia**📈: La recuperación económica global aumentó la demanda de gas, creando un desbalance entre oferta y demanda en un momento de limitación en los recursos.
  - **Capacidad limitada de almacenamiento**: Europa no tenía suficiente capacidad de almacenamiento de gas para compensar la reducción en el suministro, lo cual exacerbó las subidas de precios.

---

## 6. ⛽ Evolución Mensual del Precio de los Combustibles (Gasolina y Diésel)

![Evolución Mensual del Precio de los Combustibles](src/01_graficas/07_EvolucionPreciosCombustible.png)

### Observaciones:
- Tanto la gasolina como el diésel muestran incrementos significativos a partir de mediados de 2021, alcanzando máximos en 2022. Estos incrementos se explican por:
  - **Subida en el precio del crudo**: El petróleo, materia prima clave, se ha encarecido debido a la menor producción y a la incertidumbre geopolítica.
  - **Crisis en la cadena de suministro**🛢️: Las dificultades logísticas globales y el aumento de los costes de transporte han impactado los precios.
  - **Política energética global**🚢: Los intentos de transición hacia energías limpias han llevado a una reducción en inversiones en petróleo, limitando la capacidad de producción frente a una alta demanda.

---

## 7. 💧 Evolución Mensual del Precio del Agua

![Evolución Mensual del Precio del Agua](src/01_graficas/08_EvolucionPrecioAgua.png)

### Observaciones:
- El precio del agua se ha mantenido estable, con un incremento modesto en 2022. A diferencia de los combustibles y la electricidad, el agua ha sido menos afectada por factores de mercado y geopolíticos, debido a su carácter local y su menor dependencia de los mercados globales.

# 📌 Conclusión

Este análisis muestra cómo los precios de productos esenciales como la luz 💡, el gas 🔥 y los combustibles ⛽ han experimentado aumentos drásticos entre 2021 y 2022, impulsados por factores como la crisis energética, el conflicto en Ucrania 🇺🇦 y la alta demanda post-COVID 📈. La electricidad y el gas, en particular, han sido afectados por la dependencia de Europa en energías importadas y por la volatilidad en el mercado de emisiones de CO₂ 🌍. 

El agua 💧, en cambio, ha mostrado una mayor estabilidad, aunque también ha tenido un leve incremento en 2022.

## 💰 Impacto en el Costo de Vida
El aumento en los precios de estos productos esenciales afecta directamente el coste de vida. Luz, gas y combustibles son bienes que no podemos dejar de consumir, y sus aumentos se reflejan en facturas más altas 🧾, lo cual reduce el poder adquisitivo y eleva el costo de vida 📉. Además, el incremento en el precio de la energía tiene un efecto en cadena, encareciendo también la producción y el transporte de bienes y servicios.

En conclusión, el encarecimiento de estos bienes plantea un desafío para la economía doméstica, sobre todo para las familias con ingresos limitados. La presión sobre los presupuestos familiares obliga a reducir el gasto en otras áreas, afectando la calidad de vida general. Esto subraya la importancia de políticas que aseguren la accesibilidad y estabilidad de estos servicios básicos 🔄, para mitigar el impacto en la población y promover una vida más sostenible y accesible.

# Próximos Pasos 🚀

Para mejorar el análisis de precios y explorar patrones más detallados en los datos obtenidos, se plantean los siguientes pasos:

1. **Ampliación del Análisis a Toda España**
   - **Cobertura Nacional**: Extender el análisis de precios de agua, electricidad, gas y combustibles a todas las comunidades autónomas de España, con el fin de identificar variaciones regionales y obtener un panorama completo del mercado nacional.
   - **Desglose Regional**: Incorporar un desglose detallado que permita comparar los precios entre diferentes regiones, resaltando áreas con costos más altos o bajos.

2. **Solicitud de Información Detallada sobre Precios del Agua**
   - **Fuentes Adicionales**: Contactar organismos que dispongan de datos más desagregados sobre precios de agua en cada comunidad o ciudad, lo que permitirá un análisis preciso.
   - **Normalización de Datos**: Implementar un proceso de limpieza y normalización de datos del agua, asegurando que las comparaciones sean consistentes y precisas entre diferentes años y fuentes.

3. **Comparación con Precios en Europa**
   - **Análisis Comparativo Internacional**: Incorporar datos de precios de servicios (agua, electricidad, gas, combustibles) de otros países europeos para comparar la evolución de precios en España con la de otros países.
   - **Identificación de Patrones Globales**: Observar si las variaciones de precios en España siguen tendencias similares en el resto de Europa, lo que puede ayudar a identificar factores externos (como conflictos geopolíticos o cambios en el mercado global) que impacten los precios.

4. **Profundización en el Análisis Temporal y Estacional**
   - **Estacionalidad y Tendencias**: Desarrollar análisis más detallados para observar patrones estacionales en los precios, especialmente en servicios con alta variabilidad, como los combustibles.
   - **Predicción de Precios**: Utilizar modelos predictivos para anticipar posibles fluctuaciones en los precios de estos servicios y brindar un panorama a futuro.

5. **Mejora de Visualizaciones y Reportes**
   - **Visualizaciones Interactivas**: Implementar gráficos interactivos que permitan a los usuarios explorar los datos por comunidad autónoma, tipo de servicio y rango de fechas.
   - **Reportes Automatizados**: Crear reportes periódicos que informen sobre cambios significativos en los precios, y detectar anomalías que puedan alertar sobre subidas o bajadas inusuales.


# Contribuciones 🤝

Las contribuciones a este proyecto son muy bienvenidas. Si tienes alguna sugerencia, mejora o corrección, no dudes en ponerte en contacto o enviar tus ideas.

Cualquier tipo de contribución, ya sea en código, documentación o feedback, será valorada. ¡Gracias por tu ayuda y colaboración!

# Autores y Agradecimientos ✍️

## Autor ✒️
**Gonzalo Ruipérez Ojea** - [@apelsito](https://github.com/apelsito) en github

## Agradecimientos ❤️
Quiero expresar mi agradecimiento a **Hackio** y su equipo por brindarme la capacidad y las herramientas necesarias para realizar este proyecto con solo una semana de formación. Su apoyo ha sido clave para lograr este trabajo.
