#!/usr/bin/env python
# coding: utf-8


def find_indices(array, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param array: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    tmp_cash = {}
    for i in range(len(array)):
        # the remainder of the subtraction
        rest_num = n - array[i]
        if array[i] in tmp_cash:
            return tmp_cash[array[i]], i
        else:
            tmp_cash[rest_num] = i
    return None
