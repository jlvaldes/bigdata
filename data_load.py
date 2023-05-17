import pandas as pd
from global_variables import CSV_BOOK_DATA_CLEANED_PATH 
from global_variables import CSV_BOOK_RATING_CLEANED_PATH 
from global_variables import CSV_ANALYTICS_PATH 
from global_variables import DB_HOST, DB_PASS, DB_PORT, DB_USER
from global_variables import DW_HOST, DW_PASS, DW_PORT, DW_USER

def load_data_oring():

    df_data = pd.read_csv(CSV_BOOK_DATA_CLEANED_PATH)
    df_rating = pd.read_csv(CSV_BOOK_RATING_CLEANED_PATH)

    #implementar carga
    #se sugiere buscar una estrategia eficiente
    #revisar computacipón distribuida

    return 0


def load_data_analytics():

    df = pd.read_csv(CSV_ANALYTICS_PATH)
    #implementar carga
    #se sugiere buscar una estrategia eficiente
    #revisar computacipón distribuida
    return 0