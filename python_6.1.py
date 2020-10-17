import time

class TrafficLight:
    def __init__(self):
        self.__color = 'red'
    def running(self):
        while True:
            if self.__color == 'red':
                print('Горит красный сигнал светофора')
                self.__color = 'yellow'
                time.sleep(7)
            elif self.__color == 'yellow':
                print('Горит желтый сигнал светофора')
                self.__color = 'green'
                time.sleep(2)
            else:
                print('Горит зеленый сигнал светофора')
                self.__color = 'red'
                time.sleep(4)
                break

traffic = TrafficLight()
traffic.running()