my_str = open("5_1.txt", "w")
my_str.close()
while True:
    my_str = input('Введите строку, для выхода нажмите Enter\n')
    if my_str == '':
        break
    else:
        with open("text.txt", "a", encoding="utf-8") as f_obj:
            print(f'{my_str}', file = f_obj)
