
import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH

    
def prepare_book_data(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    print('[TODO] Limpieza de datos')

    return df


def prepare_book_rating(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    print('[TODO] Limpieza de datos')

    return df

