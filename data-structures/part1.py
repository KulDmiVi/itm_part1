

def square_perimetr(a: int) -> int:
    """Периметр квадрата"""
    return 4 * a


def square_area(a: int) -> int:
    """Площадь квадрата"""
    return a ** 2


def rectangle_area(a: int, b: int) -> int:
    """Площадь прямоугольника"""
    return a * b


def rectangle_perimetr(a: int, b: int) -> int:
    """Периметр прямоугольника"""
    return 2 * (a + b)


def d_circumference(d: int) -> float:
    """Нахождение длинны окружности"""
    Pi = 3.14
    return Pi * d


def cube_volume(a: int) -> int:
    """Объем куба"""
    return a ** 3


def parallelepiped_volume(a: int, b: int, c: int) -> int:
    """Объем прямоугольного параллелепипеда"""
    return a * b * c


def parallelepiped_square(a: int, b: int, c: int) -> int:
    """Площадь прямоугольного параллелепипеда"""
    return 2 * (a * b + b * c + a * c)


def r_circumference(r: int) -> float:
    """Нахождение длинны окружности по заданному радиусу"""
    Pi = 3.14
    return 2 * Pi * r


def arithmetic_mean(a: int, b: int) -> float:
    """Нахождение среднего арифметического"""
    return (a + b) / 2


def geometric_mean(a: int, b: int) -> float:
    """Нахождение среднего геометрического двух чисел"""
    return (a * b) ** 0.5


def sum_squares(a: int, b: int) -> int:
    """Нахождение суммы квадратов двух чисел"""
    return a ** 2 + b ** 2


def difference_squares(a: int, b: int) -> int:
    """Нахождение разности квадратов двух чисел"""
    return a ** 2 - b ** 2


def multiplication_squares(a: int, b: int) -> int:
    """Нахождение произведения квадратов двух чисел"""
    return a ** 2 * b ** 2


def division_squares(a: int, b: int) -> float:
    """Нахождение частного квадратов двух чисел"""
    return a ** 2 / b ** 2


if __name__ == "__main__":
    print(division_squares(2, 2))
