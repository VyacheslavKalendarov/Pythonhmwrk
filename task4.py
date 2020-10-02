'''4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.'''


def my_func1(x, y):
    val = 1/x
    for i in range(1, abs(y), 1):
        val *= 1/x
    return val


def my_func(x, y):
    return x ** y

print(my_func1(float(input('Введите действительное положительное число: ')),
                   int(input('Введите целое отрицательное число: '))))
