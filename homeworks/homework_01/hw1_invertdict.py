#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if not isinstance(source_dict, dict):
        return True
    inv_dict = {}
    for key, val in source_dict.items():
        do_invert(key, val, inv_dict)
    return inv_dict


def do_invert(key, val, inv_dict):
    if isinstance(val, list) or isinstance(val, set):
        for l_i in val:
            if isinstance(l_i, list) or isinstance(l_i, set):
                do_invert(key, l_i, inv_dict)
            else:
                add_to_inv_dict(key, l_i, inv_dict)
    elif isinstance(val, tuple):
        fst, snd = val
        if isinstance(fst, list) or isinstance(fst, set):
            do_invert(key, fst, inv_dict)
        else:
            add_to_inv_dict(key, fst, inv_dict)
        if isinstance(snd, list) or isinstance(snd, set):
            do_invert(key, snd, inv_dict)
        else:
            add_to_inv_dict(key, snd, inv_dict)
    # elif isinstance(val, dict):
    #     return invert_dict(val)
    else:
        add_to_inv_dict(key, val, inv_dict)


def add_to_inv_dict(key, val, inv_dict):
    if val in inv_dict:
        if isinstance(inv_dict[val], list):
            inv_dict[val].append(key)
        else:
            inv_dict[val] = [inv_dict[val], key]
    else:
        inv_dict[val] = key
