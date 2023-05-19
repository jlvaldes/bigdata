
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
    
    #Contar nulls
    print(df_cleaned["publishedDate"].isnull().sum())
    
    #Reemplazar nulls por 0
    df_cleaned['publishedDate'].fillna(0, inplace=True)
    
    #Transformar datos solo a años
    def extract_year(value):
        if value != 0 and value.isdigit() and len(value) >= 4:
            return int(value[:4])
        else:
            return 0
            
    #Llamar función
    df_cleaned['publishedDate'] = df_cleaned['publishedDate'].apply(extract_year)
    
    #Contar valores
    print(df_cleaned["publishedDate"].value_counts())
    
    #Retornar CSV
    #df_cleaned.to_csv(CSV_BOOK_DATA_CLEANED_PATH)
    return df_cleaned


def prepare_book_rating(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    print('[TODO] Limpieza de datos')

    return df

df=pd.read_csv('../Datasets/books_data.csv')
prepare_book_data(df)


