class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def findmass(self):
        self.mass = self._length * self._width * 25 * 5 / 1000
        print(f'Масса асфальта - {self.mass}')

road = Road(20, 5000)
road.findmass()