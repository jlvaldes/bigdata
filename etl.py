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
def task__data_transofrmation(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    

    print('Iniciando proceso de transformación de datos...')
    transform_data(df)
    print('Transformación finalizada...')
    return 0


@task(name='Data load process')
def task__data_load():
    print('Iniciando proceso de carga de datos de libros y ratings...')
    load_data_oring()
    print('Carga finalizada...')

    print('Iniciando proceso de carga de datos de analítica...')
    load_data_analytics()
    print('Carga finalizada...')


    return 0


@flow(name='ETL Flow')
def etl_flow():
    print('Iniciando flujo de ETL')

    df_book_data, df_book_rating = task_extract_data()
    df1, df2 = task__data_quality(df_book_data, df_book_rating)
    task__data_transofrmation(df1)
    task__data_load()

    print('Flujo de ETL finalizado')


if __name__ == "__main__":
    etl_flow()


