#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''

    class Entry:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def get_key(self):
            return self._key

        def get_value(self):
            return self._value

        def __eq__(self, other):
            return self._key == other.get_key()

        def __str__(self):
            return 'key={}, value={}'.format(self._key, self._value)

        def __repr__(self):
            return '({},{})'.format(self._key, self._value)

    def __init__(self, bucket_num=64, load_factory=0.75):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.__table = [None] * bucket_num
        self.__capacity = bucket_num
        self.__threshold = int(self.__capacity * load_factory)
        self.__size = 0

    def get(self, key, default_value=None):
        hash_value = key.__hash__()
        bucket = self.__table[self._get_index(hash_value)]
        if bucket is not None:
            for entry in bucket:
                if entry.get_key() == key:
                    return entry.get_value()
        return default_value

    def put(self, key, value):
        if self.__size >= self.__threshold:
            self._resize()
        self.__size = self.__put_in_specific_table(key, value, self.__table, self.__size)

    def __put_in_specific_table(self, key, value, table, size):
        hash_value = key.__hash__()
        bucket = table[self._get_index(hash_value)]
        if bucket is None:
            table[self._get_index(hash_value)] = [self.Entry(key, value)]
            size += 1
        else:
            for entry in bucket:
                if entry.get_key() == key:
                    entry._value = value
                    return size
            bucket.append(self.Entry(key, value))
            size += 1
        return size

    def __len__(self):
        return self.__size

    def _get_hash(self, key):
        return key.__hash__()

    def _get_index(self, hash_value):
        return hash_value % self.__capacity

    def values(self):
        values = []
        for bucket in self.__table:
            if bucket is not None:
                for entry in bucket:
                    values += [entry.get_value()]
        return values

    def keys(self):
        keys = []
        for bucket in self.__table:
            if bucket is not None:
                for entry in bucket:
                    keys += [entry.get_key()]
        return keys

    def items(self):
        items = []
        for i in range(len(self.__table)):
            if self.__table[i] is not None:
                for entry in self.__table[i]:
                    items += [(entry.get_key(), entry.get_value())]
        return items

    def _resize(self):
        new_table = [None] * self.__capacity * 2
        self.__threshold *= 2
        self._transfer(new_table)
        self.__table = new_table

    def _transfer(self, new_table):
        self.__size = 0
        for key, val in self.items():
            self.__size = self.__put_in_specific_table(key, val, new_table, self.__size)

    def __str__(self):
        string = ''
        for k, v in self.items():
            string += str(k) + ': ' + str(v) + ', \n'
        return string

    def __repr__(self):
        string = '{'
        for k, v in self.items():
            string += str(k) + ': ' + str(v) + ', '
        return string + "}"

    def __contains__(self, item):
        if self.get(item) is None:
            return False
        return True
