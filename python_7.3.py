class Cell:
    def __init__(self,quant):
        self.quant = quant
    def __add__(self, other):
        print(f'Cумма ячеек общей клетки {self.quant + other.quant}')
    def __sub__(self, other):
        if (self.quant - other.quant) < 0:
            print(f'Число ячеек общей клетки меньше нуля!')
        else:
            print(f'Число ячеек общей клетки {self.quant - other.quant}')
    def __mul__(self, other):
        print(f'Число ячеек общей клетки {self.quant * other.quant}')
    def __truediv__(self, other):
        print(f'Число ячеек общей клетки {self.quant // other.quant}')
    def make_order(self, num):
        for i in range(self.quant):
            if ((i % (num)) == 0) and (i != 0):
                print('\n*',end='')
            else:
                print('*', end='')
cell1 = Cell(15)
cell2 = Cell(28)
cell1 + cell2
cell2 - cell1
cell2 / cell1
cell1 * cell2
cell1.make_order(8)