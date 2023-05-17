import pandas as pd
from global_variables import CSV_BOOK_DATA_PATH
from global_variables import CSV_BOOK_RATING_PATH
from global_variables import CSV_BOOK_DATA_CLEANED_PATH
from global_variables import CSV_BOOK_RATING_CLEANED_PATH
from global_variables import PERCENT

#generar un nuevo CSV con la información de los libros, solo con las columnas de interés
def extract_book_data( percent = PERCENT):
    df = pd.DataFrame()

    #leer el csv original CSV_BOOK_DATA_PATH
    #eliminiar del df las columnas que no usamos
    #almacenas ese df en un nuevo csv (localmente, el raiz del proyecto)

    df.to_csv(CSV_BOOK_DATA_CLEANED_PATH)

    return df


#generar un nuevo CSV con la información de los libros, solo con las columnas de interés
def extract_book_rating(percent = PERCENT):
    df = pd.DataFrame()
    print("prueba")
    #leer el csv original CSV_BOOK_RATING_PATH
    #eliminiar del df las columnas que no usamos
    #almacenas ese df en un nuevo csv (localmente, el raiz del proyecto)

    df.to_csv(CSV_BOOK_RATING_CLEANED_PATH)

    return df



if __name__ == "__main__":
    extract_book_data()
    extract_book_rating()