#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet:

    def __init__(self):
        self._hashmap = HashMap()
        self.__def_mock = 1

    def get(self, key, default_value=None):
        return key in self._hashmap

    def put(self, key):
        self._hashmap.put(key, self.__def_mock)

    def __len__(self):
        return self._hashmap.__len__()

    def values(self):
        return self._hashmap.keys()

    def __contains__(self, item):
        return item in self._hashmap

    def intersect(self, another_hashset):
        new_hash_set = HashSet()
        for el in another_hashset.values():
            if el in self:
                new_hash_set.put(el)
        return new_hash_set

    def __repr__(self):
        return self._hashmap.keys().__repr__()
