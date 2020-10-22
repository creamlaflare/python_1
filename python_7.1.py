class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
        self.clone = []
    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
    def __add__(self, other):
        print('Cуммарная матрица:')
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(f'{self.matrix[i][j] + other.matrix[i][j]}\t', end='')
            print('')
matrix_1 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
matrix_2 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(matrix_1)
matrix_1 + matrix_2