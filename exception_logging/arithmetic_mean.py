from exception_logging import logger_conf

my_logger = logger_conf.get_logger(__name__, 'arithmetic_mean.log')


def get_input_data():
    string_list = input('Введите числа через запятую: ').split(',')
    try:
        numbers = tuple(map(float, string_list))
        my_logger.info(f"Введена последовательность {numbers}")
        return numbers
    except ValueError:
        my_logger.error("Ошибка ввода данных")


def calc_arithmetic_mean(numbers):
    average = sum(numbers) / len(numbers)
    my_logger.info(f"Вычислено среднее арифметическое")
    return average


def main():
    numbers = get_input_data()
    if numbers:
        return calc_arithmetic_mean(numbers)


if __name__ == '__main__':
    my_logger.info("Старт программы")
    result = None
    while not result:
        result = main()
    else:
        print(f"Cреднее арифметическое чисел: {result}")
        my_logger.info("Работа завершена")
