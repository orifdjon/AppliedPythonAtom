#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
    if len(input_string) % 2 != 0:
        return False
    stack = []
    for elem in input_string:
        if elem == '(' or elem == '[' or elem == '{':
            stack.append(elem)
        else:
            pair_brack = {
                ')': '(',
                '}': '{',
                ']': '['
            }[elem]
            try:
                if pair_brack != stack.pop():
                    return False
            except IndexError:
                return False
    return True
