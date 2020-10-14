f = open('5.2.txt', encoding="utf-8")
str = f.readlines()
quant_str = int(len(str))
quant_words = 0
for i in range(quant_str):
    quant_words += int(len(str[i].split()))
print(f'Количество строк в файле - {quant_str}\nКоличество слов в файле - {quant_words}')
f.close()