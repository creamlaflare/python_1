num = int(input('Введите целое положительное число '))
max = 0
while num > 0:
    if max < (num % 10):
        max = num % 10
    num = num // 10
print('Самая большая цифра в числе - ', max)