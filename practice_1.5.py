costs = int(input('Введите сумму издержек фирмы: '))
gain = int(input('Введите сумму выручки фирмы: '))
if gain > costs:
    print('Прибыль фирмы составила ', gain - costs)
elif costs > gain:
    print('Убыток фирмы составил ', costs - gain)
else:
    print('Издержки равны выручке')