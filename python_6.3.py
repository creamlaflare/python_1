class Worker:
    def __init__(self, name, surname, position, dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict["wage"] + dict["bonus"]

class Position(Worker):
    def get_total_income(self):
        print(f'Доход работника: {self._income}')
    def get_full_name(self):
        print(f'Полное имя работника - {self.name} {self.surname}')

worker1 = Position('Антон', 'Казаченко', 'Ведущий программист', {"wage": 120000, "bonus": 20000})

worker1.get_full_name()
worker1.get_total_income()