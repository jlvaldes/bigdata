import re
from unidecode import unidecode

#normalizar un texto, eliminando caracteres extraños y eliminando espacios
def normalized(text:str):
    text = re.sub(r'[^a-zA-Z\s]', '', unidecode(text))
    text = re.sub(r'[^a-zA-Z]', '', text)
    return text