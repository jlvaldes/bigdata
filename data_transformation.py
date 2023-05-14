import pandas as pd
from global_variables import CSV_TO_LOAD_PATH


def transform_data(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    path_new_csv = CSV_TO_LOAD_PATH
    #poner acá el código de transformación, generar un nuevo CSV con la data a cargar

    return 0