def task_1():
    """Вывод первого и третьего элемент списка и среза из первых трех элементов"""
    input_lst = [1, 2, 3, 4, 5]
    print(input_lst[1])
    print(input_lst[3])
    print(input_lst[:3])


def task_2():
    """Замена элемента списка вывод значений"""
    input_lst = ['Ростов', '+', 'на', '-', 'Дону']
    input_lst[1] = '-'
    print(input_lst[0], input_lst[1], input_lst[2], input_lst[3], input_lst[4])


def task_3():
    """Разбеение списка на два"""
    input_lst = ['a', 's', '1', 'a', '32', '23']
    symbols = [input_lst[0], input_lst[1], input_lst[3]]
    digits = [input_lst[2], input_lst[4], input_lst[5]]
    return digits, symbols


def task_4():
    """Удаление элемента из списка и реверсия списка"""
    _, symbols = task_3()
    symbols.pop(-1)
    symbols.reverse()
    return symbols


def task_5():
    """Преобразования списка в множество"""
    input_lst = ['a', 's', '1', 'a', '32', '23']
    print(set(input_lst))


if __name__ == "__main__":
    task_1()
    task_2()
    print(task_3())
    print(task_4())
    task_5()
