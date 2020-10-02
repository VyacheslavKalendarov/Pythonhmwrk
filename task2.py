'''2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.'''

def my_data(name, surname, year, city, email, tel):
    return (name, surname, year, city, email, tel)

print(my_data(name='alex', surname='flex', year=1990, city='spb', email='mail.ru', tel=+79999999))


