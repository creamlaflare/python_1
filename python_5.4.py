nums = ['Первое', 'Второе', 'Третье', 'Четвёртое']
with open('5.4.txt','r+', encoding="utf-8") as f:
    origin = f.readlines()
f = open("5.4(2).txt", 'w')
f.close()
with open("5.4(2).txt", 'r+', encoding="utf-8") as f:
    for i in range(len(origin)):
        word = origin[i].split()
        word[0] = nums[i]
        origin[i] = ' '.join(word)
        print(origin[i], file=f)