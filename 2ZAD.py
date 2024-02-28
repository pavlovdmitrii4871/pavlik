importimport random

def generateRandomMatrix(m=None, n=None, min_limit=None, max_limit=None):
    if not m:
        m = random.randint(1, 10)  # случайное значение для количества строк
    if not n:
        n = random.randint(1, 10)  # случайное значение для количества столбцов
    if not min_limit:
        min_limit = random.randint(0, 10)  # случайное значение для минимального лимита
    if not max_limit:
        max_limit = random.randint(10, 20)  # случайное значение для максимального лимита

    matrix = []
    
    for i in range(m):
        row = []
        for j in range(n):
            num = random.randint(min_limit, max_limit)
            row.append(num)
        matrix.append(row)

    return matrix

m_input = input("Количество строк в матрице (Enter для случайного значения): ")
n_input = input("Количество столбцов в матрице (Enter для случайного значения): ")
min_limit_input = input("Минимальное значение элементов в матрице (Enter для случайного значения): ")
max_limit_input = input("Максимальное значение элементов в матрице (Enter для случайного значения): ")

m = int(m_input) if m_input else None
n = int(n_input) if n_input else None
min_limit = int(min_limit_input) if min_limit_input else None
max_limit = int(max_limit_input) if max_limit_input else None

random_matrix = generateRandomMatrix(m, n, min_limit, max_limit)
print("Результат: ")
for row in random_matrix:
    print(row)
