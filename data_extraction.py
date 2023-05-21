import pandas as pd
from global_variables import CSV_BOOK_DATA_PATH
from global_variables import CSV_BOOK_RATING_PATH
from global_variables import CSV_BOOK_DATA_CLEANED_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH
from global_variables import PERCENT
import os
from data_quality import prepare_book_data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from dtos import get_engine
from dtos import Book, Rating, AuthorBook, RatingsAnalytics
import numpy as np
from ml_nlp import tokenization


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


    print('Data quality check...')
    df_new = prepare_book_data(df_data)
    df_new.to_csv(CSV_BOOK_DATA_CLEANED_PATH)
    print('Datset limpio...')
    return df_new


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


def create_analytics():
    engine = get_engine()
    Session = sessionmaker(bind = engine)
    session = Session()

    result = session.query(Rating.title, Rating.text, Rating.score).limit(100)
    ratings = [RatingsAnalytics(title=tit, text=txt, score=sc) for tit, txt, sc in result]
    datos = [
        {"title": obj.title, "text": obj.text, "score": obj.score}
        for obj in ratings]
    df = pd.DataFrame(datos)
    df['category'] =   np.where(df['score'] < 3, 'negativa', 'positiva')

    doc_squeeze = df['text'].squeeze()
    df['tokens'] = tokenization(doc_squeeze)
    print(df['tokens'])


if __name__ == '__main__':
    create_analytics()

