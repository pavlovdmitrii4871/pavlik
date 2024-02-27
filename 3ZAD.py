import random
import time

# Генерация случайной матрицы
def generate_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = [random.randint(0, 100) for _ in range(m)]
        matrix.append(row)
    return matrix

# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Сортировка вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Турнирная сортировка
def tournament_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def build_max_heap(arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)

    def tournament(arr):
        n = len(arr)
        build_max_heap(arr)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)

    tournament(arr)
    return arr

# Замер времени работы алгоритма сортировки
def measure_time_sort(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Замер времени работы стандартной функции сортировки
def measure_time_sorted(arr):
    start_time = time.time()
    sorted_arr = sorted(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Генерация случайной матрицы размером 5x5
matrix = generate_matrix(5, 5)
print("Исходная матрица:")
for row in matrix:
    print(row)

# Перевод матрицы в одномерный список
arr = [num for row in matrix for num in row]

# Сортировка выбором
sorted_arr, duration = measure_time_sort(selection_sort, arr)
print("\nРезультат сортировки выбором:")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка вставкой
sorted_arr, duration = measure_time_sort(insertion_sort, arr)
print("\nРезультат сортировки вставкой:")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка пузырьком
sorted_arr, duration = measure_time_sort(bubble_sort, arr)
print("\nРезультат сортировки пузырьком:")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка Шелла
sorted_arr, duration = measure_time_sort(shell_sort, arr)
print("\nРезультат сортировки Шелла:")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)

# Быстрая сортировка
sorted_arr, duration = measure_time_sort(quick_sort, arr)
print("\nРезультат быстрой сортировки:")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)

# Турнирная сортировка
sorted_arr, duration = measure_time_sort(tournament_sort, arr)
print("\nРезультат турнирной сортировки:")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка с использованием стандартной функции sorted()
sorted_arr, duration = measure_time_sorted(arr)
print("\nРезультат сортировки с использованием стандартной функции sorted():")
print(sorted_arr)
print("Время работы алгоритма: %.6f сек" % duration)