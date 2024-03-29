import numpy as np#Эта строка импортирует библиотеку NumPy, которая предоставляет возможности для работы с многомерными массивами.

# Функция для вычисления определителя матрицы
def det(matrix):#Этот блок кода определяет функцию det, которая принимает матрицу в качестве аргумента и использует функцию np.linalg.det() из библиотеки NumPy для вычисления определителя матрицы
    return np.linalg.det(matrix)

# Функция для решения системы уравнений
def solve(matrix, vector):#Этот блок кода определяет функцию solve, которая принимает матрицу и вектор в качестве аргументов и использует функцию np.linalg.solve() из библиотеки NumPy для решения системы линейных уравнений.
    return np.linalg.solve(matrix, vector)
# Создаем матрицу
matrix = np.array([[1, 2], [3, 4]])#Эта строка создает двумерный массив (матрицу) с указанными элементами с помощью функции np.array() из библиотеки NumPy

#Вычисляем определитель. Этот блок кода вычисляет определитель для созданной матрицы, используя ранее определенную функцию det, и выводит результат на экран.
determinant = det(matrix)
print("Определитель матрицы:")
print(determinant)

# Создаем вектор
vector = np.array([1, 2])#Эта строка создает одномерный массив (вектор) с указанными элементами с помощью функции np.array() из библиотеки NumPy

# Решаем систему уравнений. Этот блок кода использует ранее определенную функцию solve для решения системы линейных уравнений с помощью созданной матрицы и вектора и выводит результат на экран.
solution = solve(matrix, vector)
print("Решение системы уравнений:")
print(solution)