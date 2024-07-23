def centimeters_to_meters(L):
    """Количество полных метров"""
    return L // 100


def kilograms_to_tons(M):
    """Количество тон"""
    return M // 1000


def bytes_to_kbytes(b):
    """Количество килобайт"""
    return b // 1024


def segments_count(a, b):
    """Количество отрезков"""
    return a // b


def segment_free_part(a, b):
    """Свободная часть отрезка"""
    return a % b


def left_right_part(a):
    """Вывод левой и правой части двухзначного числа"""
    print(a // 10)
    print(a % 10)


def summ_digit(a):
    """Сумма цифр двухзначного числа"""
    return (a // 10) + (a % 10)


def multiplication_digit(a):
    """Произведение цифр двухзначного числа"""
    return (a // 10) * (a % 10)


def first_digit(a):
    """Вывод первой цифры трехзначного числа"""
    print(a // 100)


def last_second_digit(a):
    """Вывод последней и второй цифры трехзначного числа"""
    print(a % 10)
    print((a % 100) // 10)


if __name__ == "__main__":
    print(first_digit(254))
