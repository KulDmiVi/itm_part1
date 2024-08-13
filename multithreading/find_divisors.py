import concurrent.futures
import time
import cProfile
import pstats
from io import StringIO


def find_divisors_range(n, start, end):
    divisors = []
    for i in range(start, end):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def get_divisors(n):
    divisors = []
    left_range = int(n ** 0.5) + 1
    step = 1000
    ranges = [(i, min(i + step, left_range)) for i in range(1, left_range, step)]
    ranges[-1] = (ranges[-1][0], left_range)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_range = {executor.submit(find_divisors_range, n, start, end): (start, end) for start, end in ranges}
        for future in concurrent.futures.as_completed(future_to_range):
            divisors.extend(future.result())

    return sorted(set(divisors))


def get_divisors_line(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return sorted(divisors)


def main():
    number = 12_345_678
    if 1_000_000 <= number <= 20_000_000:
        start_time = time.time()
        divisors = get_divisors(number)
        print(f"Целочисленные делители числа {number}: {divisors}")
        print(f"Затраченное время многопоточное: {time.time() - start_time:.4f} секунд.")

        start_time = time.time()
        divisors = get_divisors_line(number)
        print(f"Целочисленные делители числа {number}: {divisors}")
        print(f"Затраченное время однопоточное: {time.time() - start_time:.4f} секунд.")
    else:
        print("Число должно быть в диапазоне от 1_000_000 до 20_000_000.")


if __name__ == "__main__":
    # Профилирование по CPU
    pr = cProfile.Profile()
    pr.enable()  # Начать профилирование

    main()  # Вызов основной функции

    pr.disable()  # Остановить профилирование
    s = StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    print("\n--- Результаты профилирования по CPU ---")
    print(s.getvalue())
