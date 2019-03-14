import sys

from encode_tools.creator_of_table import create_table
from encode_tools.data_verifier import def_format
from encode_tools.creator_of_data import json_reader, tsv_reader

# Ваши импорты

if __name__ == '__main__':
    filename = sys.argv[1]

    # Ваш код
    try:
        data_format = def_format(filename)
        if data_format == 0:
            create_table(json_reader(filename))
        if data_format == 1:
            create_table(tsv_reader(filename))
    except FileNotFoundError:
        print('Файл не найден')
    except (UnicodeDecodeError, UnicodeError) or ValueError:
        print('Данные не валидны')

