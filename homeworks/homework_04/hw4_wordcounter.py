#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
import os


def count_words(path_to_dir, filename, queue):
    with open(f'{path_to_dir}/{filename}', 'r', encoding='utf8') as f:
        queue.put((filename, 0))
        for words in f.readlines():
            queue.put((filename, len([w for w in words.split(' ') if w != '\n'])))


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    manager = Manager()
    queue = manager.Queue()
    tasks = []
    for f in os.listdir(path_to_dir):
        print(f)
        p = Process(target=count_words, args=(path_to_dir, f, queue))
        p.start()
        tasks.append(p)

    for task in tasks:
        task.join()

    hash_map = {}
    len_of_queue = queue.qsize()
    for _ in range(len_of_queue):
        key, value = queue.get()
        if key in hash_map:
            hash_map[key] += value
        else:
            hash_map[key] = value
    hash_map['total'] = sum(hash_map.values())
    return hash_map
