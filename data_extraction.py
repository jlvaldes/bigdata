import pandas as pd
from global_variables import CSV_BOOK_DATA_PATH
from global_variables import CSV_BOOK_RATING_PATH
from global_variables import CSV_BOOK_DATA_CLEANED_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH
from global_variables import PERCENT
import os

#generar un nuevo CSV con la información de los libros, solo con las columnas de interés
def extract_book_data( percent = PERCENT):
    print('Cargar en memoria dataset de libros...')
    pd.set_option('display.max_colwidth', None)
    ruta_data_csv = CSV_BOOK_DATA_PATH
    ruta_data_absoluta = os.path.abspath(ruta_data_csv)
    df_data = pd.read_csv(ruta_data_absoluta)
    print('Dataset de libros cargado en memoria...')


    if PERCENT < 100:
        print(f'Seleccionando muestra aleatoria del {PERCENT}%')
        num_filas_seleccion = int(len(df_data) * (PERCENT / 100))
        df_data = df_data.sample(n=num_filas_seleccion)
        print(f'Muestra aleatoria seleccionada. Filas seleccionadas: {num_filas_seleccion}')


    print('Limpiando dataset...')
    columnas = ['Title', 'description', 'publisher', 'categories', 'ratingsCount', 'publishedDate', 'authors'] 
    df_new = df_data[columnas].copy()
    df_new.to_csv(CSV_BOOK_DATA_CLEANED_PATH)
    print('Datset limpio...')
    return df_new


def func_dani():
    #leer el csv original CSV_BOOK_DATA_PATH
    df = pd.read_csv(CSV_BOOK_DATA_PATH)
    #eliminiar del df las columnas que no usamos
    df_clean = df[[
    'Title', 
    'description', 
    'authors', 
    'publisher',
    'publishedDate', 
    'categories', 
    'ratingsCount']]
    #almacenas ese df en un nuevo csv (localmente, el raiz del proyecto)

    df_clean.to_csv(CSV_BOOK_DATA_CLEANED_PATH)

    return df_clean


#generar un nuevo CSV con la información de los libros, solo con las columnas de interés
def extract_book_rating(percent = PERCENT):
    print('Cargar en memoria dataset de ratings...')
    pd.set_option('display.max_colwidth', None)
    ruta_rating_csv = CSV_BOOK_RATING_PATH
    ruta_data_absoluta = os.path.abspath(ruta_rating_csv)
    df_rating = pd.read_csv(ruta_data_absoluta)
    print('Dataset de ratings cargado en memoria...')

    if PERCENT < 100:
        print(f'Seleccionando muestra aleatoria del {PERCENT}%')
        num_filas_seleccion = int(len(df_rating) * (PERCENT / 100))
        df_rating = df_rating.sample(n=num_filas_seleccion)
        print(f'Muestra aleatoria seleccionada. Filas seleccionadas: {num_filas_seleccion}')

    print('Limpiando dataset...')
    columnas = ['Title', 'Price', 'review/score', 'review/time', 'review/summary', 'review/text']
    df_new = df_rating[columnas].copy()
    df_new.to_csv(CSV_BOOK_RATING_CLEANED_PATH)
    print('Datset limpio...')
    return df_new


def func_dani_2():    
    df = pd.DataFrame()
   
    #leer el csv original CSV_BOOK_RATING_PATH
    df2 = pd.read_csv(CSV_BOOK_RATING_PATH)
    #eliminiar del df las columnas que no usamos
    df_clean_rating = df2[[
    'Id', 
    'Title', 
    'Price', 
    'User_id', 
    'profileName', 
    'review/helpfulness',
    'review/score', 
    'review/time', 
    'review/summary', 
    'review/text']]
    #almacenas ese df en un nuevo csv (localmente, el raiz del proyecto)

    df_clean_rating.to_csv(CSV_BOOK_RATING_CLEANED_PATH)

    return df_clean_rating



if __name__ == "__main__":
    extract_book_data()
    extract_book_rating()
