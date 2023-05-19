#ETL para la carga inicial de toda la data a la base de datos


from prefect import flow, task
from data_extraction import extract_book_data
from data_extraction import extract_book_rating
from data_quality import prepare_book_data
from data_quality import prepare_book_rating
from data_transformation import transform_data
from data_load import load_data_analytics
from data_load import load_data_oring
import pandas as pd

@task(name='Data extraction process')
def task_extract_data():
    print('Extrayendo datos de los libros...')
    df_data = extract_book_data()
    print('Extracción de datos libros finalizada...')


    print('Extrayendo datos de rating de los libros...')
    df_dating = extract_book_rating()
    print('Extracción de datos de rating finalizada...')

    return df_data, df_dating


@task(name='Data quality process')
def task__data_quality(df_data: pd.DataFrame, df_rating: pd.DataFrame):
    if not isinstance(df_data, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    

    print('Iniciando proceso de limpieza de book data...')
    df_data = prepare_book_data(df_data)
    print('Limpieza finalizada de  book data...')

    print('Iniciando proceso de limpieza de  book rating...')
    df_rating = prepare_book_rating(df_rating)
    print('Limpieza finalizada de book rating...')


    return df_data, df_rating


@task(name='Data transformation process')
def task__data_transofrmation(df_data: pd.DataFrame, df_rating:pd.DataFrame, data_cleaned= True):
    print('Iniciando proceso de transformación de datos...')
    books, authors, ratings = transform_data(data_cleaned= True, df1= df_data, df2= df_rating)
    print('Transformación finalizada...')
    return books, authors, ratings


@task(name='Data load process')
def task__data_load(books_list, authors_list, ratings_list):
    print('Iniciando proceso de carga de datos de libros y ratings...')
    load_data_oring(books_dtos_list=books_list, authors_dtos_list=authors_list, ratings_dtos_list=ratings_list)
    print('Carga finalizada...')
    return 0


@flow(name='ETL Flow')
def etl_flow():
    print('Iniciando flujo de ETL')

    df_book_data, df_book_rating = task_extract_data()
    books, rating = task__data_quality(df_book_data, df_book_rating)
    books_dtos, authors_dtos, ratings_dtos = task__data_transofrmation(df_data= books, df_rating= rating, data_cleaned= True)
    task__data_load(books_dtos, authors_dtos, ratings_dtos)

    print('Flujo de ETL finalizado')


if __name__ == "__main__":
    etl_flow()


