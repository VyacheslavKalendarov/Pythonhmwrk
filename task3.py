# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = int(input('Введите любое число больше 0 и меньше 10: '))
while num < 0 or num >= 10:
    num = int(input('Введите любое число больше 0 и меньше 10: '))

print(num + (num * 10 + num) + (num * 100 + num * 10 + num))
