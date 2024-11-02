# Se importa la librería para la llamada a la API
import requests
import pandas as pd
import json



def hacer_request_json(url):
    try:
        result = requests.get(url)
        result.raise_for_status() 
        json_data = result.json()  
        return json_data
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")  # Error específico de HTTP
    except requests.exceptions.ConnectionError:
        print("Error de conexión. Verifica la URL o tu conexión a internet.")
    except requests.exceptions.Timeout:
        print("La solicitud ha tardado demasiado. Intenta de nuevo más tarde.")
    except requests.exceptions.RequestException as req_err:
        print(f"Error inesperado en la solicitud: {req_err}")
    except ValueError:
        print("La respuesta no contiene un JSON válido.")
    return None


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

def api_luz(years,ruta_guardado):
    df = pd.DataFrame()
    for year in years:
        url = f"https://apidatos.ree.es/es/datos/mercados/componentes-precio?start_date={year}-01-01T00:00&end_date={year}-12-31T23:59&time_trunc=month&geo_limit=ccaa"
        print(f"Realizando Request a: {url}")
        jason = hacer_request_json(url)
        
        if jason is not None:
            # Guardar JSON en archivo
            with open(f"../datos/02_PreciosLuz/01_JsonBackups/PreciosLuz{year}.json", "w") as file:
                json.dump(jason, file, indent=4)  # Guarda el JSON en un archivo
            
            print(f"Backup Realizado: PreciosLuz{year}.json")
            
            precios = jason["included"][-1]["attributes"]["values"]
            fechas = []
            costes = []
            for precio in precios:
                costes.append(precio["value"])
                fechas.append(precio["datetime"])

            df_temp = pd.DataFrame({
                "precio": costes,
                "fecha": fechas
            })
            df = pd.concat([df, df_temp], ignore_index=True)
        else:
            print(f"No se pudo obtener datos para el año {year}")
   
    df.index = df.index + 1
    df.reset_index(inplace=True)
    df.to_csv(f"{ruta_guardado}/01_PreciosLuzSinLimpiar.csv")
    print(f"Dataframe guardado en: {ruta_guardado}")
    return df