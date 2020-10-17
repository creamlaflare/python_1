class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')

painting1 = Pencil("карандошом")
painting1.draw()
painting2 = Pen('ручкой')
painting2.draw()
painting3 = Handle('маркером')
painting3.draw()