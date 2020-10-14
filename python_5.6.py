name = ''
num_s = ''
num = ''
sum = 0
dict = {}
with open("5_6.txt", encoding="utf-8") as f:
    str_s = f.readlines()
    for i in range(len(str_s)):
        str = str_s[i]
        str = str.split()
        name = str[0]
        name = name[:-1]
        for j in range(1,4):
            num_s = str[j]
            num = num_s.split("(")
            num = num[0]
            if num.isdigit():
                sum+=int(num)
        dict.update({name: sum})
print(dict.items())