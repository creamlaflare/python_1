'''Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
sum = 0
with open("5_5.txt", "w", encoding="utf-8") as f_obj:
    print('4 5 6 7 8 9 0 2 3 1', file = f_obj)
with open("5_5.txt", "r", encoding="utf-8") as f_obj:
    str = f_obj.readline()
    str = str.split()
for i in range(len(str)):
    sum += int(str[i])
print(f'Сумма чисел из файла равна {sum}')