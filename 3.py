import numpy as np

# Создание массива из трех строк и четырех столбцов
arr_2d = np.random.normal(loc=0.0, scale=1.0, size=(3, 4))

# Получение одномерного массива с таким же атрибутом size
arr_1d = arr_2d.flatten()

print("Исходный двумерный массив:")
print(arr_2d)
print("\nПреобразованный одномерный массив:")
print(arr_1d)