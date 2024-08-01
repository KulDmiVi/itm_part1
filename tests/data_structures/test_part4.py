from data_structures.part4 import *

def test_task_1():
    output = task_1()
    assert output == (2, 4, [1, 2, 3])

def test_task_2():
    output = task_2()
    assert output == ('Ростов', '-', 'на', '-', 'Дону')

def test_task_3():
    output = task_3()
    assert output == (['1', '32', '23'], ['a', 's', 'a'])

def test_task_4():
    output = task_4()
    assert output == ['s', 'a']

def test_task_5():
    output = task_5()
    assert output == {'1', '23', '32', 'a', 's'}