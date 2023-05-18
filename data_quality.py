
import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH

    
def prepare_book_data(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    #Eliminar columnas que contienen links
    df_cleaned = pd.DataFrame(df)
    columas_eliminar = ["image", "previewLink", "infoLink"]
    df_cleaned=df_cleaned.drop(columns=columas_eliminar, axis=1)
    print(df_cleaned.dtypes)
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

#df=pd.read_csv('../Datasets/books_data.csv')
#prepare_book_data(df)


