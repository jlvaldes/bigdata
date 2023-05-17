import pandas as pd
from global_variables import CSV_ORIGIN_PATH

def extract_data():
    df = pd.DataFrame()
    
    #poner el código de exracción de datos acá
    df = pd.read_csv(CSV_ORIGIN_PATH)
    df.head(3)

    return df