
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
    
    #Extaer año, convertir nulls en 0 y cambiar el tipo a integer
    df_cleaned['publishedDate'] = df_cleaned['publishedDate'].str.extract(r'(\d{4})')
    df_cleaned['publishedDate'] = df_cleaned['publishedDate'].fillna('0')
    df_cleaned['publishedDate']=df_cleaned['publishedDate'].astype(int)
    
    #Función para eliminar caracteres innecesarios
    def quitar_corchetes(valor):
        if isinstance(valor, str):
            return valor.strip("[]''")
        elif isinstance(valor, list):
            return [v.strip("''") for v in valor]
        else:
            return valor
            
    #Eliminación de caracteres para authors y categories
    df_cleaned['authors'] = df_cleaned['authors'].apply(quitar_corchetes)
    df_cleaned['categories'] = df_cleaned['categories'].apply(quitar_corchetes)
    
    #Retornar CSV
    df_cleaned.to_csv(CSV_BOOK_DATA_CLEANED_PATH, index=False)
    df_cleaned.info()
    
    return df_cleaned


def prepare_book_rating(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")

    return df