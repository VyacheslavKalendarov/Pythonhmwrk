'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора
в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.'''

from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = cycle(['red', 'yellow', 'green'])

    def running_TrafficLight(self):
        for color in TrafficLight.__colors:
            print(color)
            if color == 'red':
                sleep(7)
            elif color == 'yellow':
                sleep(2)
            else:
                sleep(5)


t = TrafficLight()
t.running_TrafficLight()
