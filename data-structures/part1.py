Pi = 3.14


def square_perimetr(a):
    """Периметр квадрата"""
    return 4 * a


def square_area(a):
    """Площадь квадрата"""
    return a ** 2


def rectangle_area(a, b):
    """Площадь прямоугольника"""
    return a * b


def rectangle_perimetr(a, b):
    """Периметр прямоугольника"""
    return 2 * (a + b)


def d_circumference(d):
    """Нахождение длинны окружности"""
    return Pi * d


def cube_volume(a):
    """Объем куба"""
    return a ** 3


def parallelepiped_volume(a, b, c):
    """Объем прямоугольного параллелепипеда"""
    return a * b * c


def parallelepiped_square(a, b, c):
    """Площадь прямоугольного параллелепипеда"""
    return 2 * (a * b + b * c + a * c)


def r_circumference(r):
    """Нахождение длинны окружности по заданному радиусу"""
    return 2 * Pi * r


def arithmetic_mean(a, b):
    """Нахождение среднего арифметического"""
    return (a + b) / 2


def geometric_mean(a, b):
    """Нахождение среднего геометрического двух чисел"""
    return (a * b) ** 0.5


def sum_squares(a, b):
    """Нахождение суммы квадратов двух чисел"""
    return a ** 2 + b ** 2


def difference_squares(a, b):
    """Нахождение разности квадратов двух чисел"""
    return a ** 2 - b ** 2


def multiplication_squares(a, b):
    """Нахождение произведения квадратов двух чисел"""
    return a ** 2 * b ** 2


def division_squares(a, b):
    """Нахождение частного квадратов двух чисел"""
    return a ** 2 / b ** 2


if __name__ == "__main__":
    print(division_squares(2, 2))

