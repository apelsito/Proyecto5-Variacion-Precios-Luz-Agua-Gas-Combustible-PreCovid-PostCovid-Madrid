# Tratamiento y manipulación de datos
# -----------------------------------------------------------------------
import pandas as pd                                 # Manipulación de estructuras de datos como DataFrames
import numpy as np                                  # Cálculos numéricos y manejo de arrays
import datetime                                     # Manipulación de fechas y tiempos

# Visualización de progreso
# -----------------------------------------------------------------------
from tqdm import tqdm                               # Creación de barras de progreso durante bucles

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
    
    df[columna] = df[columna].map(dictio)

    return df