#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''

    if x is None or y is None: return None

    try:
        x = float(x)
        y = float(y)
    except ValueError as e:
        return None

    if operator == 'plus':
        return x + y
    if operator == 'minus':
        return x - y
    if operator == 'mult':
        return x * y
    if operator == 'divide':
        if y != 0:
            return x / y
    return None
