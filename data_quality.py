
import pandas as pd

    
def prepare_data(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    

    df_cleaned = pd.DataFrame()

    #poner acá el código para limpiar la dat y generar un data frame nuevo

    return df_cleaned