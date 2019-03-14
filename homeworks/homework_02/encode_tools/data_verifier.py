import json
import csv


def def_enc(file: str) -> str:
    for enc in ['utf8', 'utf16', 'cp1251']:
        try:
            with open(file, 'r', encoding=enc) as f:
                f.readline()
            return enc
        except UnicodeError:
            continue
    raise UnicodeError


def is_tsv(file: str) -> bool:
    enc = def_enc(file)
    with open(file, 'r', encoding=enc) as f:
        data = []
        for row in list(csv.DictReader(f, dialect='excel-tab')):
            data.append(row)
    if len(data) != 0:
        return True
    raise ValueError


def is_json(file: str)-> bool:
    try:
        enc = def_enc(file)
        with open(file, 'r', encoding=enc) as f:
            data = json.load(f)
            if len(data) != 0:
                return True
            raise ValueError
    except json.JSONDecodeError:
        return False


def def_format(file):
    if is_json(file):
        return 0
    elif is_tsv(file):
        return 1
    else:
        raise UnicodeDecodeError


def is_valid_data(data):
    if not all([len(i) == len(data[0]) for i in data]):
        raise ValueError

    if not all([data[0].keys() == i.keys() for i in data]):
        raise ValueError
