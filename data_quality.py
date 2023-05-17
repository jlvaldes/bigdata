
import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH

    
def prepare_book_data(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    #Easte es un comentario
    df_cleaned = pd.DataFrame()
    columas_eliminar = [] #############
    df_cleaned.drop(columns=columas_eliminar, axis=1)
    df_cleaned.to_csv(CSV_BOOK_DATA_CLEANED_PATH)
    return df_cleaned


def prepare_book_rating(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    #limpiar del dataframe de rating lo que se necesita limpiar
    #actualiza los CVS generados con la nueva data

    df_cleaned = pd.DataFrame()
    df_cleaned.to_csv(CSV_BOOK_RATING_CLEANED_PATH)
    return df_cleaned

