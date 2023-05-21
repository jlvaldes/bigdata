import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH 
from global_variables import CSV_BOOK_RATING_CLEANED_PATH 
from global_variables import CSV_ANALYTICS_PATH 
from global_variables import DB_HOST, DB_PASS, DB_PORT, DB_USER
from global_variables import DW_HOST, DW_PASS, DW_PORT, DW_USER
from dtos import get_engine, delete_all_data
from sqlalchemy.orm import sessionmaker
import datetime
from dtos import get_engine


def load_data_oring(books_dtos_list, authors_dtos_list, ratings_dtos_list):

    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    print('Iniciando proceso de carga...')
    start_time = datetime.datetime.now()
    
    delete_all_data('author_book')
    delete_all_data('rating')
    delete_all_data('book')

    print("[INFO] Cargar libros...")
    #session.add_all(books_dtos_list)
    #session.bulk_save_objects(books_dtos_list)
    partitioned_data_load(books_dtos_list, session)
    session.commit()
    print("[INFO] DONE...")

    print("[INFO] Cargar autores...")
    #session.add_all(authors_dtos_list)
    #session.bulk_save_objects(authors_dtos_list)
    partitioned_data_load(authors_dtos_list, session)
    session.commit()
    print("[INFO] DONE...")

    
    print("[INFO] Cargar ratings...")
    #session.add_all(ratings_dtos_list)
    #session.bulk_save_objects(ratings_dtos_list)
    partitioned_data_load(ratings_dtos_list, session)
    session.commit()
    print("[INFO] DONE...")

    session.close()
    print("Carga finalizada...")

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(f"Resumen:\n - Se cargaron\n {len(books_dtos_list)} libros\n {len(authors_dtos_list)} libros\n {len(ratings_dtos_list)} ratings\n - Tiempo transcurrido para la carga:", elapsed_time)

    return 0


def partitioned_data_load(objects, session):
    page_size = int(len(objects) * 0.3)
    total_pages = (len(objects) // page_size) + 1
    for page_id, _ in enumerate(range(total_pages)):
        inicio = page_id * page_size
        fin = (page_id + 1) * page_size
        pagina_objetos = objects[inicio:fin]
        session.add_all(pagina_objetos)
        session.commit()
        print(f'Page {page_id} to {total_pages} [{page_id/total_pages*100} %]')
    return



def load_data_analytics():

    print('[TODO] Carga de analytics pendiente')
    return 0