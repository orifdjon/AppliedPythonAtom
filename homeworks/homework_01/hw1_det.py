#!/usr/bin/env python
# coding: utf-8
import copy


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    if not is_valid_determinant(list_of_lists):
        return None
    return determinant(list_of_lists, len(list_of_lists))


def determinant(matrix, dim):
    '''
    Вычисляет определитель матрицы
    :param matrix: матрица
    :param dim: рамерность
    :return value_of_det: значение опеределителя matrix
    '''
    value_of_det = 0
    if dim == 1:
        return matrix[0][0]
    if dim == 2:
        return matrix[0][0] * matrix[1][1] - (matrix[1][0] * matrix[0][1])
    if dim > 2:
        for i in range(dim):
            elem, minor = get_minor_i(i, matrix)
            value_of_det += elem * determinant(minor, len(minor))
    return value_of_det


def get_minor_i(i, matrix):
    '''
    Получить минор и число, которое умножается на минор
    :param i: индекс числа из первой строки массива
    :param matrix: - список списков
    :return: (elem, list), где elem - число, для умножения
    с минором, list - минор размера (n - 1)
    '''
    dim = len(matrix)
    elem = (-1) ** i * matrix[0][i]
    minor = copy.deepcopy(matrix[1:][:])
    for k in range(dim - 1):
        for j in range(dim):
            if j == i:
                del (minor[k][j])
    return elem, minor


def is_valid_determinant(matrix):
    '''
    Проверка на валидность матрицы
    :param matrix: список списков - исходная матрица
    :return: True или False
    '''
    dim = len(matrix)
    for array in matrix:
        if len(array) != dim:
            return False
    return True