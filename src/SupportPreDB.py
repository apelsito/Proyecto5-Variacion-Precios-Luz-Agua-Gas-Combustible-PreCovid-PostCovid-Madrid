# Tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd             # Manipulación y análisis de datos en estructuras DataFrame
import numpy as np              # Realización de cálculos numéricos y manipulación de arrays multidimensionales
import datetime                 # Manejo y procesamiento de fechas y tiempos para análisis temporal

# Visualización de progreso
# -----------------------------------------------------------------------
from tqdm import tqdm           # Crea barras de progreso visuales para bucles largos, mejorando la legibilidad del progreso


def crear_dictio(df,columna):
    """
    Crea un diccionario a partir de un DataFrame, donde las claves son valores únicos de una columna específica,
    y los valores son los primeros índices asociados a cada clave en el DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame de entrada que contiene la columna de interés.
        columna (str): Nombre de la columna cuyos valores únicos se usarán como claves en el diccionario.

    Returns:
        dict: Diccionario donde las claves son los valores únicos de la columna especificada, y los valores son 
              los primeros índices asociados a cada clave en el DataFrame.

    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'index': [1, 2, 3, 4], 'columna': ['A', 'B', 'A', 'C']})
        >>> crear_dictio(df, 'columna')
        {'A': 1, 'B': 2, 'C': 4}
    """
    dictio = {}
    datos = df.groupby(columna)["index"].first()
    indices = list(datos.index)
    valores = list(datos.values)
    for i in range(0, len(indices)):
        dictio[indices[i]] = valores[i] 
    
    return dictio

def df_a_db(dictio,df,columna):
    """
    Mapea los valores de una columna específica en un DataFrame según un diccionario y devuelve el DataFrame modificado.

    Args:
        dictio (dict): Diccionario de mapeo donde las claves son los valores originales y los valores son los nuevos valores deseados.
        df (pd.DataFrame): DataFrame que contiene la columna a mapear.
        columna (str): Nombre de la columna en el DataFrame que será modificada usando el diccionario de mapeo.

    Returns:
        pd.DataFrame: DataFrame con la columna especificada modificada según el diccionario de mapeo.
    """
    df[columna] = df[columna].map(dictio)

    return df