#!/usr/bin/env python
# coding: utf-8

import random
import time
import os

from homeworks.homework_03.hw3_hashmap import HashMap
from homeworks.homework_03.hw3_hashset import HashSet
from homeworks.homework_03.hw3_lrucache import LRUCacheDecorator
from homeworks.homework_03.hw3_testing import MockOrdinaryFileWorker, LLNode
from homeworks.homework_03.hw3_event_stats import TEventStats
from homeworks.homework_03.hw3_revert_linked_list import revert_linked_list
from homeworks.homework_03.hw3_groupping_anagramms import groupping_anagramms


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


def test_hashset_05():
    try:
        hashset = HashSet()
    except NotImplementedError:
        return True
    hashset_2 = HashSet()
    entries = [5, 7, "entries", 56, "value", 54., 1000, "t", HashMap(10), ()]
    for k in entries:
        hashset.put(k)
        hashset_2.put(k)
    hashset_3 = hashset.intersect(hashset_2)
    assert hashset_3 is not hashset
    assert hashset_3 is not hashset_2
    assert len(hashset_3) == len(entries)


def test_hashset_05():
    try:
        hashset = HashSet()
    except NotImplementedError:
        return True
    hashset_2 = HashSet()
    entries = [5, 7, "entries", 56, "value", 54., 1000, "t", HashMap(10), ()]
    for i, k in enumerate(entries):
        if i % 2 == 0:
            hashset.put(k)
            continue
        hashset_2.put(k)
    hashset_3 = hashset.intersect(hashset_2)
    assert hashset_3 is not hashset
    assert hashset_3 is not hashset_2
    assert len(hashset_3) == len(entries)


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
            nonlocal my_global_vars
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


def test_groupping_anagramms_01():
    try:
        groupping_anagramms([])
    except NotImplementedError:
        return True

    words = """Аз есмь строка живу я мерой остр
               За семь морей ростка я вижу рост
               Я в мире сирота
               Я в Риме Ариост""".split()

    correct_res = [
        ['Аз', 'За'], ['Ариост', 'сирота'],
        ['Риме', 'мире'], ['Я', 'Я', 'я', 'я'],
        ['в', 'в'], ['вижу', 'живу'],
        ['есмь', 'семь'], ['мерой', 'морей'],
        ['остр', 'рост'], ['ростка', 'строка']
    ]

    res = groupping_anagramms(words)
    res = sorted(sorted(x) for x in res)
    assert all(x == y for x, y in zip(res, correct_res))


def test_groupping_anagramms_02():
    try:
        groupping_anagramms([])
    except NotImplementedError:
        return True

    words = []
    correct_res = []

    res = groupping_anagramms(words)
    assert res == correct_res


def test_groupping_anagramms_03():
    try:
        groupping_anagramms([])
    except NotImplementedError:
        return True

    words = """Лунь
               нуль
               Воз
               зов
               Чертог
               горечь
               Днесь
               снедь""".split()

    correct_res = [
        ['Воз', 'зов'], ['Днесь', 'снедь'],
        ['Лунь', 'нуль'], ['Чертог'], ['горечь']
    ]

    res = groupping_anagramms(words)
    res = sorted(sorted(x) for x in res)
    assert all(x == y for x, y in zip(res, correct_res))


def test_event_stats_01():
    try:
        TEventStats()
    except NotImplementedError:
        return True

    correct_res = [2, 1, 1, 0]

    event_stats = TEventStats()

    for user_id, ts in [
        (122, 1552565081), (123, 1552565082),
        (124, 1552565092), (124, 1552565093),
        (123, 1552565100), (125, 1552565482)
    ]:
        event_stats.register_event(user_id, ts)

    res = [
        event_stats.query(2, 1552565101), event_stats.query(1, 1552565493),
        event_stats.query(1, 1552565181), event_stats.query(0, 1552565181)
    ]

    assert all(x == y for x, y in zip(res, correct_res))


def test_revert_linked_list_01():
    try:
        revert_linked_list(None)
    except NotImplementedError:
        return True

    correct_repr = "value: 4; next_node: (value: 3; next_node: (value: 2; next_node: (value: 1; next_node: (None))))"

    n1 = LLNode(1, None)
    n2 = LLNode(2, None)
    n3 = LLNode(3, None)
    n4 = LLNode(4, None)

    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4

    res = revert_linked_list(n1)

    assert res.__repr__() == correct_repr


def test_revert_linked_list_02():
    try:
        revert_linked_list(None)
    except NotImplementedError:
        return True

    # test LL with single node
    head = LLNode(0, None)

    res = revert_linked_list(head)
    assert res is head and head.next_node is None


def test_revert_linked_list_03():
    try:
        revert_linked_list(None)
    except NotImplementedError:
        return True

    correct_repr = "value: 12; next_node: (value: 42; next_node: (None))"

    n1 = LLNode(42, None)
    n2 = LLNode(12, None)

    n1.next_node = n2

    res = revert_linked_list(n1)

    assert res.__repr__() == correct_repr
