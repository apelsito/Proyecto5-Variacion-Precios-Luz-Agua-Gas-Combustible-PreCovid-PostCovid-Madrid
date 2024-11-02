# Se importa la librería para la llamada a la API
import requests
import pandas as pd


def hacer_request_json(url):
    result = requests.get(url)
    json = result.json()
    return json


def api_gas(fecha_inicio,fecha_final):
    # Llamada API para obtener la información del recurso del catálogo de un dataset 
    url = "https://catalogodatos.cnmc.es/api/3/action/package_search?q=Evolución de los precios por productos MIBGAS" 
    # Obtención del identificador del recurso con los datos del dataset 
    datos_catalogo = hacer_request_json(url)
    id_recurso = datos_catalogo["result"]["results"][0]["resources"][0]["id"]; 
    # Llamada API para obtener todos los datos del recurso del dataset 
    url = "https://catalogodatos.cnmc.es/api/3/action/datastore_search?limit=32000&resource_id="+ id_recurso
    result = hacer_request_json(url)

    datos_dataset = result["result"]["records"]
    df_gas = pd.DataFrame(datos_dataset)
    # Pasar las fechas a datetime
    df_gas["fecha_de_negociacion"] = pd.to_datetime(df_gas["fecha_de_negociacion"])
    cond1 = df_gas["fecha_de_negociacion"] > fecha_inicio
    cond2 = df_gas["fecha_de_negociacion"] < fecha_final
    df_filtrado = df_gas[cond1 & cond2]
    return df_filtrado

def api_luz(years):
    
    for year in years:
        
    
    return