import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH 
from global_variables import CSV_BOOK_RATING_CLEANED_PATH 
from global_variables import CSV_ANALYTICS_PATH 
from global_variables import DB_HOST, DB_PASS, DB_PORT, DB_USER
from global_variables import DW_HOST, DW_PASS, DW_PORT, DW_USER
from dtos import get_engine, delete_all_data
from sqlalchemy.orm import sessionmaker

def load_data_oring(books_dtos_list, authors_dtos_list, ratings_dtos_list):

    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    print('Iniciando proceso de carga...')
    
    delete_all_data('book')
    print("[INFO] Cargar libros...")
    session.add_all(books_dtos_list)
    session.commit()
    print("[INFO] Libros cargados...")

    delete_all_data('author_book')
    print("[INFO] Cargar autores...")
    session.add_all(authors_dtos_list)
    session.commit()
    print("[INFO] Autores cargados...")

    delete_all_data('rating')
    print("[INFO] Cargar ratings...")
    session.add_all(ratings_dtos_list)
    session.commit()
    print("[INFO] Ratings cargados...")


    session.close()
    print("Carga finalizada...")

    return 0


def load_data_analytics():

    print('[TODO] Carga de analytics pendiente')
    return 0