sec = int(input('Введите время в секундах: '))
min = sec // 60
sec -= min*60
hrs = min // 60
min -= hrs*60
print(f'{hrs}:{min}:{sec}')