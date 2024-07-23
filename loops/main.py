import random


def average():
    numbers_count = 0
    sum_numbers = 0
    input_data = ''
    while input_data != 0:
        try:
            input_data = float(input("Введите число: "))
        except ValueError:
            print("Введенное значение не корректно")
            exit(0)
        sum_numbers += input_data
        numbers_count += 1
    else:
        if numbers_count > 1:
            print(f"Среднее арифметическое: {sum_numbers / (numbers_count - 1)}")
        else:
            print(f"Количество введенных чисел равно 0")


def output_range():
    for number in range(101):
        print(number)


def multiplication_table():
    for i in range(10):
        for z in range(10):
            print(f"{i} x {z} = {i * z}")


def output_list():
    data_list = [random.randint(0, 100) for _ in range(10)]
    for item in data_list:
        print(item)


def output_dict():
    data_dict = {z: random.randint(0, 100) for z in range(10)}
    for key, value in data_dict.items():
        print(f"{key}: {value}")


def output_multiples_three():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)


def summ_100():
    print(sum(range(1, 101)))


def multiplication_table_2():
    for i in range(1, 11):
        print(f"2 x {i} = {i * 2}")


def prime_numbers():
    lst = []
    for i in range(2, 51):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)


def sqrt_sums():
    sqrt_sum = 0
    for i in range(1, 11):
        sqrt_sum += i ** 2
    print(sqrt_sum)


def output_sqrt_numbers():
    i = 0
    while i <= 10:
        print(f"{i}^2 = {i ** 2}")
        i += 0.5


def get_factorial():
    fact = 1
    for i in range(1, 6):
        fact = fact * i
        print(f"Факториал {i}: {fact}")


if __name__ == '__main__':
    # average()
    # output_range()
    # print("Таблица умножения")
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
