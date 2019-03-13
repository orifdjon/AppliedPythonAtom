#!/usr/bin/env python
# coding: utf-8

import random
import time
import os

from homeworks.homework_03.hw3_hashmap import HashMap
from homeworks.homework_03.hw3_hashset import HashSet
from homeworks.homework_03.hw3_lrucache import LRUCacheDecorator
from homeworks.homework_03.hw3_testing import MockOrdinaryFileWorker


def test_hashmap_01():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        assert hashmap._get_hash(k) == hash(k)
        assert hashmap._get_hash(v) == hash(v)
    for k, v in entries:
        assert hashmap._get_index(hashmap._get_hash(k)) == hash(k) % 10
        assert hashmap._get_index(hashmap._get_hash(v)) == hash(v) % 10


def test_hashmap_02():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        assert k in hashmap


def test_hashmap_03():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    inner_list_name = [k for k, v in hashmap.__dict__.items() if isinstance(v, list)][0]
    for k, v in entries:
        hashmap.put(k, v)
    for k, v in entries:
        assert HashMap.Entry(k, None) in hashmap.__dict__[inner_list_name][hashmap._get_index(hashmap._get_hash(k))]


def test_hashmap_04():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ()), ({"s": "v"}, {"v": "s"})]
    for k, v in entries:
        entry = HashMap.Entry(k, v)
        assert entry.get_key() == k
        assert entry.get_value() == v

    for i in range(len(entries)):
        entry_one = HashMap.Entry(entries[i][0], entries[i][1])
        for _ in range(10):
            j = random.randint(0, len(entries) - 1)
            p = random.randint(0, len(entries) - 1)
            entry_two = HashMap.Entry(entries[j][0], entries[p][1])
            if j == i:
                assert entry_one == entry_two
            else:
                assert entry_one != entry_two


def test_hashmap_05():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    for k, v in entries:
        assert hashmap.get(k) == v
    for _ in range(100):
        i = random.randint(0, len(entries) - 1)
        j = random.randint(0, len(entries) - 1)
        hashmap.put(i, j)
        assert hashmap.get(i) == j
    assert hashmap.get("nexit", "default") == "default"


def test_hashmap_06():
    try:
        hashmap = HashMap(10)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    output_values = set()
    output_keys = set()
    for v in hashmap.values():
        output_values.add(v)
    for k in hashmap.keys():
        output_keys.add(k)
    for k, v in entries:
        assert k in output_keys
        assert v in output_values
    output_values = set()
    output_keys = set()
    for k, v in hashmap.items():
        output_values.add(v)
        output_keys.add(k)
    for k, v in entries:
        assert k in output_keys
        assert v in output_values


def test_hashmap_07():
    try:
        hashmap = HashMap(2)
    except NotImplementedError:
        return True
    entries = [(5, 7), ("entries", 56), ("value", 54.), (1000, "t"), (HashMap(10), ())]
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        hashmap.put(k, v)
    assert len(hashmap) == 5
    for k, v in entries:
        assert k in hashmap


def test_hashset_01():
    try:
        hashset = HashSet()
    except NotImplementedError:
        return True
    entries = [5, 7, "entries", 56, "value", 54., 1000, "t", HashMap(10), ()]
    for i in entries:
        hashset.put(i)
    for i in entries:
        assert hashset.get(i)
        assert i in hashset


def test_hashset_02():
    try:
        hashset = HashSet()
    except NotImplementedError:
        return True
    entries = [5, 7, "entries", 56, "value", 54., 1000, "t", HashMap(10), ()]
    for i in entries:
        hashset.put(i)
    assert len(hashset) == len(entries)


def test_hashset_03():
    try:
        hashset = HashSet()
    except NotImplementedError:
        return True
    entries = [5, 7, "entries", 56, "value", 54., 1000, "t", HashMap(10), ()]
    for i in entries:
        hashset.put(i)
    output_values = set()
    for i in hashset.values():
        output_values.add(i)
    for i in entries:
        assert i in output_values


def test_hashset_04():
    try:
        hashset = HashSet()
    except NotImplementedError:
        return True
    hashset.put("entry")
    hashset.put("entry")
    assert len(hashset) == 1


def test_lrucache_01():

    try:
        @LRUCacheDecorator(maxsize=3, ttl=None)
        def get_sq(s):
            time.sleep(2)
            return s ** 2
    except NotImplementedError:
        return True

    t_start = time.time()
    get_sq(1)
    assert time.time() - t_start > 0.5

    t_start = time.time()
    get_sq(1)
    assert time.time() - t_start < 0.5


def test_lrucache_02():
    try:
        @LRUCacheDecorator(maxsize=3, ttl=None)
        def get_sq(s):
            time.sleep(2)
            return s ** 2
    except NotImplementedError:
        return True

    get_sq(1)
    get_sq(2)
    get_sq(3)
    get_sq(1)
    get_sq(4)
    get_sq(5)

    t_start = time.time()
    get_sq(1)
    assert time.time() - t_start < 0.5


def test_lrucache_03():
    try:
        @LRUCacheDecorator(maxsize=4, ttl=None)
        def get_sq(s):
            time.sleep(1)
            return s ** 2
    except NotImplementedError:
        return True

    t_start = time.time()
    get_sq(1)
    assert time.time() - t_start > 0.5
    t_start = time.time()
    get_sq(1)
    assert time.time() - t_start < 0.5
    l = [5, 6, 7]
    for i in l:
        t_start = time.time()
        get_sq(i)
        assert time.time() - t_start > 0.5
    l = [1, 5, 6, 7]
    for i in l:
        t_start = time.time()
        get_sq(i)
        assert time.time() - t_start < 0.5
    l = [7, 5, 6, 1]
    for i in l:
        t_start = time.time()
        get_sq(i)
        assert time.time() - t_start < 0.5
    l = [15]
    for i in l:
        t_start = time.time()
        get_sq(i)
        assert time.time() - t_start > 0.5
    l = [1, 6, 5, 15]
    for i in l:
        t_start = time.time()
        get_sq(i)
        assert time.time() - t_start < 0.5
    l = [7]
    for i in l:
        t_start = time.time()
        get_sq(i)
        assert time.time() - t_start > 0.5


def test_lrucache_04():
    my_global_vars = {}
    try:
        @LRUCacheDecorator(maxsize=3, ttl=10)
        def get_sq(s):
            time.sleep(2)
            global my_global_vars
            my_global_vars[s] = s ** 2
            return my_global_vars[s]
    except NotImplementedError:
        return True

    get_sq(3)
    t_start = time.time()
    get_sq(3)
    assert time.time() - t_start < 2
    assert my_global_vars[3] == get_sq(3) == 9

    for i in my_global_vars:
        my_global_vars[i] += 1

    t_start = time.time()
    get_sq(3)
    assert time.time() - t_start < 2
    assert my_global_vars[3] != get_sq(3)

    time.sleep(10)
    get_sq(3)
    assert my_global_vars[3] == get_sq(3)


def test_testing_01():
    try:
        mock = MockOrdinaryFileWorker()
    except NotImplementedError:
        return True
    assert "tmpf" in os.listdir(".")
    mock.transfer_to_local("filename")
    with open("./tmpf/filename", "r") as f:
        file_1 = f.readline()
    with open("./homeworks/homework_03/test_dir/filename.tmp", "r") as f:
        file_2 = f.readline()
    assert file_1.strip() == file_2.strip()
    del mock
    assert "tmpf" not in os.listdir(".")


def test_testing_02():
    try:
        mock = MockOrdinaryFileWorker()
    except NotImplementedError:
        return True
    assert "tmpf" in os.listdir(".")
    mock.transfer_to_remote("filename")
    with open("./tmpf/filename.tmp", "r") as f:
        file_1 = f.readline()
    with open("./homeworks/homework_03/test_dir/filename", "r") as f:
        file_2 = f.readline()
    assert file_1.strip() == file_2.strip()
    del mock
    assert "tmpf" not in os.listdir(".")


def test_testing_03():
    try:
        mock = MockOrdinaryFileWorker()
    except NotImplementedError:
        return True
    assert "tmpf" in os.listdir(".")
    mock_2 = MockOrdinaryFileWorker()
    assert "tmpf" in os.listdir(".")
    del mock_2
    assert "tmpf" not in os.listdir(".")
