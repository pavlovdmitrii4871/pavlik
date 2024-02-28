import random

def generateRandomMatrix(m=None, n=None, min_limit=0, max_limit=100):
    if not m:
        m = random.randint(1, 10)  # случайное значение для количества строк
    if not n:
        n = random.randint(1, 10)  # случайное значение для количества столбцов

    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = random.randint(min_limit, max_limit)
            row.append(num)
        matrix.append(row)

    return matrix


m = int(input("Количество строк в матрице: "))
n = int(input("Количество столбцов в матрице: "))
min_limit = int(input("Минимальное значение элементов в матрице: "))
max_limit = int(input("Максимальное значение элементов в матрице: "))

random_matrix = generateRandomMatrix(m, n, min_limit, max_limit)
print("Результат: ")
for row in random_matrix:
    print(row)
