from random import randint


def bubble_sort(array):
    """Сортировка пузырьком"""
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def binary_search(array, value):
    """Бинарный поиск"""
    low = 0
    high = len(array) - 1
    mid = len(array) // 2

    array.sort()

    while array[mid] != value and low <= high:
        if value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print('No value')
    else:
        print('ID =', mid)


if __name__ == "__main__":
    a = [randint(1, 10) for n in range(10)]
    print(a)
    bubble_sort(a)
    print(a)
    binary_search(a, 5)
