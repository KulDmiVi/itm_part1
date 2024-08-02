import random


def average():
    numbers_count = 0
    sum_numbers = 0
    input_data = ''

    while input_data != 0:
        try:
            input_data = float(input("Введите число: "))
        except ValueError:
            return "Введенное значение не корректно"
        sum_numbers += input_data
        numbers_count += 1
    else:
        if numbers_count > 1:
            return f"Среднее арифметическое: {sum_numbers / (numbers_count - 1)}"
        else:
            return f"Количество введенных чисел равно 0"


def output_range():
    result = []
    for number in range(101):
        result.append(number)
    return result


def multiplication_table():
    result = []
    for i in range(10):
        for z in range(10):
            result.append(f"{i} x {z} = {i * z}")
    return result



def output_list():
    result = []
    data_list = [random.randint(0, 100) for _ in range(10)]
    for item in data_list:
        result.append(item)
    return result


def output_dict():
    result = []
    data_dict = {z: random.randint(0, 100) for z in range(10)}
    for key, value in data_dict.items():
        result.append(f"{key}: {value}")
    return result


def output_multiples_three():
    result = []
    for i in range(1, 101):
        if i % 3 == 0:
            result.append(i)
    return result

def summ_100():
    return sum(range(1, 101))


def multiplication_table_2():
    result = []
    for i in range(1, 11):
        result.append(f"2 x {i} = {i * 2}")
    return " ".join(result)


def prime_numbers():
    lst = []
    for i in range(2, 51):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def sqrt_sums():
    sqrt_sum = 0
    for i in range(1, 11):
        sqrt_sum += i ** 2
    return sqrt_sum


def output_sqrt_numbers():
    i = 0
    result = []
    while i <= 10:
        result.append(f"{i}^2 = {i ** 2}")
        i += 0.5
    return " ".join(result)


def get_factorial():
    fact = 1
    result = []
    for i in range(1, 6):
        fact = fact * i
        result.append(f"{i}: {fact}")
    return " ".join(result)


if __name__ == '__main__':
    # average()
    # output_range()
    # return "Таблица умножения")
    # multiplication_table()
    # output_list()
    # output_dict()
    # output_multiples_three()
    # summ_100()
    # multiplication_table_2()
    # prime_numbers()
    # sqrt_sums()
    # output_sqrt_numbers()
    get_factorial()
