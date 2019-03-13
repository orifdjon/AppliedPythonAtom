#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet:

    def __init__(self):
        # TODO Сделать правильно =)
        raise NotImplementedError

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        raise NotImplementedError

    def put(self, key, value):
        # TODO метод put, нужно переопределить данный метод
        raise NotImplementedError

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        raise NotImplementedError

    def values(self):
        # TODO возвращать итератор значений
        raise NotImplementedError

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        raise NotImplementedError
