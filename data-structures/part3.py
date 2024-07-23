def is_positive(a):
    """Проверка на положительное число"""
    print(a > 0)


def is_odd(a):
    """Проверка нечетное число"""
    print(a % 2 > 0 and a != 0)


def is_even(a):
    """Проверка четное число"""
    print(a % 2 == 0 and a != 0)


def logic1(a, b):
    """Проверка условия A > 2 и B ≤ 3"""
    print(a > 2 and b <= 3)


def logic2(a, b):
    """Проверка условия A ≥ 0 или B < −2"""
    print(a >= 0 and b < -2)


def logic3(a, b, c):
    """Проверка условия A < B < C"""
    print(a < b < c)


def logic4(a, b, c):
    """Проверка условия B находится между числами A и C"""
    print(((a < b < c) or (a > b > c)))


def logic5(a, b):
    """Каждое из чисел A и B нечетное"""
    print(a % 2 > 0 and b % 2 > 0 and a != 0 and b != 0)


def logic6(a, b):
    """Хотя-бы одно из чисел A и B нечетное"""
    print((a % 2 > 0 and a != 0) or (b % 2 > 0 and b != 0))


def logic7(a, b):
    """Одно из чисел A и B нечетное"""
    print((a % 2 > 0 and a != 0 and b % 2 == 0) or (b % 2 > 0 and b != 0 and a % 2 == 0))


if __name__ == "__main__":
    logic5(0, 0)
    # logic6(2, 3)
    # logic7(3, 0)
