import numpy as np

# Создаем одномерный массив А из 12 последовательных целых чисел от 12
A = np.arange(12, 24)

# Преобразуем массив А в двумерные массивы разной формы
array_3x4 = A.reshape(3, 4)
array_4x3 = A.reshape(4, 3)
array_2x6 = A.reshape(2, 6)

# Выводим результаты
print("Одномерный массив A:")
print(A)
print("\nДвумерный массив 3x4:")
print(array_3x4)
print("\nДвумерный массив 4x3:")
print(array_4x3)
print("\nДвумерный массив 2x6:")
print(array_2x6)