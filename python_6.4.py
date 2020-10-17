class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        if (direction == 'left'):
            print('Машина поворачивает налево')
        elif (direction == 'right'):
            print('Машина поворачивает налево')
        else:
            print('Машина не поварачивает')
    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}')
    def policecheck(self):
        if self.is_police :
            print('Вас преследует полиция')
        else:
            print('Вас не преследует полиция')

class TownCar(Car):
    def cartype(self):
        print('Ваша машина - городская')
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете скорость! Ваша скорость равна {self.speed}')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class SportCar(Car):
    def cartype(self):
        print('Ваша машина - спортивная')

class WorkCar(Car):
    def cartype(self):
        print('Ваша машина - рабочая')
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превышаете скорость! Ваша скорость равна {self.speed}')
        else:
            print(f'Текущая скорость автомобиля {self.speed}')

class PoliceCar(Car):
    def cartype(self):
        print('Ваша машина - полицейская')
    def policecheck(self):
        if self.is_police:
            print('Вас преследует полиция. Вы точно полицейские?')
        else:
            print('Вы и есть полиция! Вас не преследуют')

car_1 = WorkCar(61,'red', 'Mazda', False)
car_1.cartype()
car_1.go()
car_1.stop()
car_1.show_speed()
car_1.turn('left')
car_1.policecheck()
