import json
import csv
from .data_verifier import def_enc


def tsv_reader(file):
    enc = def_enc(file)
    with open(file, "r", encoding=enc) as f:
        data = []
        for row in list(csv.DictReader(f, dialect='excel-tab')):
            data.append(row)
    return data


def json_reader(file):
    enc = def_enc(file)
    with open(file, "r", encoding=enc) as f:
        data = json.load(f)
    return data


def to_comfort_format(data):
    hat = data[0].keys()
    list_of_val = []
    for i in data:
        list_of_val.append(list(i.values()))
    return list(hat), list_of_val
