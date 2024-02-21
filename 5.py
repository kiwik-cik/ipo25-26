import numpy as np

# Создание массива А размером 5x2
A = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

# Получение матрицы АТ путем транспонирования матрицы А
AT = A.T

print("Исходная матрица A:")
print(A)
print("\nТранспонированная матрица AT:")
print(AT)