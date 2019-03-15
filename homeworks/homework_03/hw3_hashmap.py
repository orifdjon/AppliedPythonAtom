#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''

    class Entry:
        def __init__(self, key, value):
            self.__key = key
            self.__value = value

        def get_key(self):
            return self.__key

        def get_value(self):
            return self.__value

        def __eq__(self, other):
            return self.__value == other.__value

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        raise NotImplementedError
        self.__arr: [Entry] = [None] * bucket_num
        self.__bucket_num = bucket_num
        self.__size = 0

    def get(self, key, default_value=None):
        raise NotImplementedError
        hash_key = key.__hash__()
        bucket = self.__arr[self.__bucket_num % hash_key]
        if bucket is not None:
            return bucket
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        raise NotImplementedError
        hash_key = key.__hash__()
        bucket = self.__arr[self.__bucket_num % hash_key]
        if bucket is None:
            self.__arr[self.__bucket_num % hash_key] = [Entry(key, value)]
            self.__size += 1
        else:
            len_of_bucket = len(bucket)
            count = 0
            for entry in bucket:
                if count < len_of_bucket:
                    if entry.__key == key:
                        entry.__value = value
                    else:
                        bucket.append(Entry(key, value))
                        self.__size += 1
                    count += 1

    def __len__(self):
        raise NotImplementedError
        return self.__size

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        raise NotImplementedError
        return key.__hash__()

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        raise NotImplementedError
        tmp = self.__bucket_num % hash_value
        return tmp


    def values(self):
        # TODO Должен возвращать итератор значений
        raise NotImplementedError

    def keys(self):
        # TODO Должен возвращать итератор ключей
        raise NotImplementedError

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        raise NotImplementedError

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        raise NotImplementedError

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        raise NotImplementedError

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        raise NotImplementedError
