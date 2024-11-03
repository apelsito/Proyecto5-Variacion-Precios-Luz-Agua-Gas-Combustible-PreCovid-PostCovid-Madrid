# Importamos las librerías que necesitamos

# Librerías para control y automatización de navegadores (Web Scraping)
# -----------------------------------------------------------------------
from selenium import webdriver                   # Para controlar el navegador automáticamente
from selenium.webdriver.chrome.service import Service  # Para manejar los servicios de ChromeDriver
from selenium.webdriver.common.by import By      # Para seleccionar elementos en el DOM de la página
from selenium.webdriver.chrome.options import Options  # Para establecer opciones en el navegador (como headless mode)

# Librerías para el tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd             # Para manipular estructuras de datos como DataFrames
import numpy as np              # Para cálculos numéricos y arrays multidimensionales
import datetime                 # Para manejar fechas y horas

import os
import sys
sys.path.append("../")
from time import sleep
import pdfplumber


def precios_combustible(fechas_inicio,fechas_fin):
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