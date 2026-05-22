import timeit
import random

# 1. Линейный поиск O(n)
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 2. Бинарный поиск O(log n)
def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- НАСТРОЙКА БЕНЧМАРКА ---
# Создаем огромный отсортированный массив из 10 миллионов чисел
SIZE = 10_000_000
test_array = list(range(SIZE))

# Ищем число, которое находится в самом конце (худший случай для линейного поиска)
TARGET = 9_999_999

print(f"Запуск теста на массиве из {SIZE:,} элементов...")

# Замеряем линейный поиск (запускаем 5 раз для точности)
time_linear = timeit.timeit(lambda: linearSearch(test_array, TARGET), number=5)

# Замеряем бинарный поиск (запускаем 5 раз для точности)
time_binary = timeit.timeit(lambda: binarySearch(test_array, TARGET), number=5)

# --- ВЫВОД РЕЗУЛЬТАТОВ ---
print("-" * 50)
print(f"Линейный поиск: {time_linear:.6f} секунд")
print(f"Бинарный поиск: {time_binary:.6f} секунд")
print("-" * 50)
print(f"Результат: Бинарный поиск быстрее в {int(time_linear / time_binary):,} раз(а)!")

## РЕЗУЛЬТАТ
Запуск теста на массиве из 10,000,000 элементов...
--------------------------------------------------
Линейный поиск: 2.145525 секунд
Бинарный поиск: 0.000030 секунд
--------------------------------------------------
Результат: Бинарный поиск быстрее в 71,517 раз(а)!

Process finished with exit code 0