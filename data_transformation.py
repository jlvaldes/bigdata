import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH, CSV_BOOK_DATA_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH, CSV_BOOK_RATING_PATH
from dtos import Book, Rating, AuthorBook
import os
from dtos import create_tables


def to_dtos(): #(df_data: pd.DataFrame, df_rating: pd.DataFrame):
    books = []
    authors = []
    ratings = []
    
    
    pd.set_option('display.max_colwidth', None)
    ruta_data_csv = CSV_BOOK_DATA_PATH
    ruta_rating_csv = CSV_BOOK_RATING_PATH

    ruta_data_absoluta = os.path.abspath(ruta_data_csv)
    ruta_rating_absoluta = os.path.abspath(ruta_rating_csv)

    df_data = pd.read_csv(ruta_data_absoluta)
    print('Dataset de libros cargado...')
    df_rating = pd.read_csv(ruta_rating_absoluta)
    print('Dataset de rating cargado...')

    for index, row in df_data.iterrows():
        book = Book(title= row['Title'], 
            description= row['description'], 
            publisher= row['publisher'], 
            categories= row['categories'], 
            ratingsCount= row['ratingsCount'],
            publishedDate= row['publishedDate'])

        authors_errors = 0
        if row['authors'] != None:
            try:
                authors_name = eval(str(row['authors']))
                for author in authors_name:
                    authors.append(
                        AuthorBook(name=author, title= book.title)
                    )
            except:
                authors_errors += 1
        
        books.append(book)
    
    for index, row in df_rating.iterrows():
        ratings.append(
            Rating(title= row['Title'], 
                price= row['Price'], 
                score= row['review/score'],
                time= row['review/time'], 
                summary=row['review/summary'],
                text= row['review/text'])
        )

    return books, authors, ratings




#Retorna una lista de objetos DTOs para cargar a la base de datos 
def transform_data(df: pd.DataFrame):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se espera un objeto DataFrame de pandas")
    
    
    #poner acá el código de transformación, generar un nuevo CSV con la data a cargar

    return 0

