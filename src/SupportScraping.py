# Importamos las librerías que necesitamos

# Librerías para control y automatización de navegadores (Web Scraping)
# -----------------------------------------------------------------------
from selenium import webdriver                   # Controla el navegador automáticamente para realizar acciones de scraping
from selenium.webdriver.chrome.service import Service  # Maneja los servicios del ChromeDriver, que permite ejecutar Chrome sin intervención manual
from selenium.webdriver.common.by import By      # Localiza y selecciona elementos específicos dentro del DOM de una página web
from selenium.webdriver.chrome.options import Options  # Establece opciones para Chrome (ej., headless mode para ejecutar sin interfaz gráfica)

# Librerías para el tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd             # Estructura y manipula datos en DataFrames, facilitando análisis y transformación de datos
import numpy as np              # Realiza cálculos numéricos avanzados y manipulación de arrays multidimensionales
import datetime                 # Gestiona fechas y tiempos, útil para ordenar y filtrar datos por periodos específicos

# Librerías del sistema y utilidades
# -----------------------------------------------------------------------
import os                       # Permite interactuar con el sistema operativo, gestionar rutas y archivos
import sys                      # Permite modificar las rutas de búsqueda de módulos para importar scripts personalizados
sys.path.append("../")          # Añade el directorio padre al PATH, permitiendo importar módulos personalizados en subcarpetas

from time import sleep          # Pausa la ejecución por un tiempo determinado, útil para evitar bloqueos en scraping debido a solicitudes continuas
import pdfplumber               # Extrae texto de archivos PDF, permitiendo la conversión de datos en PDF a formatos analizables

def precios_combustible(fechas_inicio,fechas_fin):
    """
    Realiza scraping en la página web del Ministerio de Energía para obtener precios de combustibles en un rango de fechas específico,
    configurando el navegador para descargar archivos automáticamente.

    Args:
        fechas_inicio (list): Lista de fechas de inicio en formato "DD/MM/AAAA" para cada rango de consulta.
        fechas_fin (list): Lista de fechas de fin en formato "DD/MM/AAAA" para cada rango de consulta.

    Proceso:
        - Configura el navegador Chrome con preferencias de descarga automática.
        - Accede a la página, selecciona las fechas de consulta y las series de combustibles (Gasolina 98, Diésel, Diésel Premium).
        - Descarga los archivos correspondientes y renombra el archivo descargado según el año de la consulta.
    """
    for inicio , fin  in zip(fechas_inicio,fechas_fin):

            ruta_padre = os.path.dirname(os.getcwd())
            ruta_hacer = os.path.join(ruta_padre, "datos", "03_PreciosCombustible", "DatosDescargados")
            os.makedirs(ruta_hacer,exist_ok=True)


            # lo primero que vamos a hacer es configurar nuestras preferencias del navegador para el driver
            chrome_options = webdriver.ChromeOptions()

            # establacemos las preferencias que queremos
            prefs = {
                
                "download.default_directory": ruta_hacer,  # AQUÍ CADA UNO TENDREMOS QUE PONER LA RUTA QUE QUERAMOS PARA QUE SE GUARDEN LOS ARCHIVOS DESCARGADOS
                "download.prompt_for_download": False,   # desactiva el diálogo que Chrome normalmente muestra para pedir confirmación del usuario antes de descargar un archivo
                "directory_upgrade": True,    # hace que Chrome actualice el directorio de descarga predeterminado a la nueva ubicación especificada por download.default_directory si esta ha cambiado.
            }
            url = "https://energia.serviciosmin.gob.es/shpCarburantes/"
            chrome_options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            driver.maximize_window()

            # Selecccionar Tipo temporal "Mensual"
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[1]/div[2]/select/option[3]").click()
            # Seleccionar fecha inicio
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[1]/div[3]/input").send_keys(inicio)
            # Seleccionar fecha fin
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[1]/div[4]/input").send_keys(fin)
            # Seleccionar Comunidad de Madrid
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[3]/fieldset/div[1]/div[2]/select/option[16]").click()
            # Click en Aceptar
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[3]/fieldset/div[2]/input").click()
            sleep(1)
            # Click en Añadir Serie
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[2]/input").click()
            sleep(0.2)
            # Click en Gasolina 98
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[4]/fieldset/div[1]/div[7]/select/option[4]").click()
            sleep(0.2)
            # Click en Aceptar
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[4]/fieldset/div[2]/input").click()
            sleep(1)
            # Click en Añadir Serie
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[2]/input").click()
            sleep(0.2)
            # Click en Diesel
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[4]/fieldset/div[1]/div[7]/select/option[6]").click()
            sleep(0.2)
            # Click en Aceptar
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[4]/fieldset/div[2]/input").click()
            sleep(1)
            # Click en Añadir Serie
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[2]/input").click()
            sleep(0.2)
            # Click en Diesel Premium
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[4]/fieldset/div[1]/div[7]/select/option[7]").click()
            sleep(0.2)
            # Click en Aceptar
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div/div[4]/fieldset/div[2]/input").click()
            sleep(1)
            # Click en Descargar
            driver.find_element("xpath","/html/body/form/div[3]/div[3]/div/div[1]/fieldset[2]/div[1]/div[1]/div/table/tbody/tr[1]/th[5]/input[2]").click()
            sleep(0.5)
            driver.quit()
            old_name= os.listdir(ruta_hacer)[0]
            new_name = f"PreciosCombustibleMadrid{inicio.split('/')[2]}.xls"
            os.rename(f"{ruta_hacer}/{old_name}",f"{ruta_hacer}/{new_name}")

def excel_a_Dataframe(ruta_archivos):
    """
    Lee múltiples archivos Excel de una carpeta, extrae y concatena las hojas en un solo DataFrame,
    asignando etiquetas de combustible según el nombre de la hoja.

    Args:
        ruta_archivos (str): Ruta del directorio que contiene los archivos Excel.

    Returns:
        pd.DataFrame: DataFrame con los datos de todas las hojas concatenadas y una columna 'combustible' 
                      que identifica el tipo de combustible en cada registro.
                      
    Proceso:
        - Itera sobre cada archivo Excel en el directorio especificado.
        - Lee cada hoja en el archivo, añade una columna con el nombre del combustible y la concatena en un DataFrame.
        - Estandariza los nombres de los combustibles para una mayor consistencia en el DataFrame final.
    """
    df_combustibles_total = []

    for archivo in os.listdir(ruta_archivos):
        if archivo.endswith(".xls"):
            ruta_archivo = os.path.join(ruta_archivos, archivo)
            leer_excel = pd.ExcelFile(ruta_archivo)
            sheets = leer_excel.sheet_names
            
            # Iterar sobre cada hoja del archivo
            for hoja in sheets:
                df_combustible = pd.read_excel(ruta_archivo, sheet_name=hoja)
                df_combustible["combustible"] = hoja
                df_combustibles_total.append(df_combustible)

    df_final = pd.concat(df_combustibles_total, ignore_index=True)
    df_final["combustible"] = df_final["combustible"].str.replace("1 G95E5 Madrid","Gasolina 95")
    df_final["combustible"] = df_final["combustible"].str.replace("2 G98E5 Madrid","Gasolina 98")
    df_final["combustible"] = df_final["combustible"].str.replace("3 GOA Madrid","Diésel")
    df_final["combustible"] = df_final["combustible"].str.replace("4 GOA+ Madrid","Diésel Premium")
    return df_final

def pdf_a_df(ruta_archivos):
    """
    Lee múltiples archivos PDF de una carpeta, extrae tablas de páginas específicas y guarda los datos en archivos CSV.

    Args:
        ruta_archivos (str): Ruta del directorio que contiene los archivos PDF.

    Proceso:
        - Itera sobre cada archivo PDF en el directorio especificado.
        - Extrae las tablas de las páginas 1 y 2 de cada archivo y convierte los datos en un DataFrame.
        - Concatena las tablas extraídas y guarda el DataFrame resultante en un archivo CSV, nombrado según el año en el nombre del archivo PDF.
        
    Manejo de errores:
        - Si ocurre algún error durante la lectura o extracción de datos de un PDF, se imprime un mensaje de advertencia y el proceso continúa.
    """
    for archivo in os.listdir(ruta_archivos):
        try:
            print(archivo)
            with pdfplumber.open(f"{ruta_archivos}/{archivo}") as pdf:
                pagina1 = pdf.pages[1]
                tabla = pagina1.extract_table()
                pagina2 = pdf.pages[2]
                tabla2 = pagina2.extract_table()
                df1 = pd.DataFrame(tabla[1:],columns=tabla[0])
                df2 = pd.DataFrame(tabla2[1:],columns=tabla[0])
                df = pd.concat([df1,df2],ignore_index=True)
            
            ruta_padre = os.path.dirname(ruta_archivos)
            year = archivo.split(".")[0].strip("agua")
            os.makedirs(ruta_padre,exist_ok=True)
            df.to_csv(f"{ruta_padre}/PreciosAgua{year}.csv")
        except:
            print(f"{archivo} no se ha podido realizar")
    return 