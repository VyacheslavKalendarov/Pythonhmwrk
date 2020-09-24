# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах: '))
sec = time % 60
time = time - sec
hours = int(time / 3600)
time = time - (hours * 3600)
min = int(time / 60)
print(f'{hours}:{min}:{sec}')

# import time
# print(time.strftime('%H:%M:%S', time.gmtime(int(input('Введите время в секундах: '))))) #2й способ более удачный, с использованием модуля time
