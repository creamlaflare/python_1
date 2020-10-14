import json
space = '\n'
profit_dict = {}
loss_dict = {}
avg_dict = {}
avg = 0
num = 0
sum = 0
with open("5_7.txt", encoding="utf-8") as f:
    str_s = f.readlines()
    for i in range(len(str_s)):
        str = str_s[i]
        str = str.split()
        if int(str[2]) > int(str[3]):
            profit_dict.update({str[0]:int(str[2])-int(str[3])})
            num+=1
            sum += int(str[2])
        elif int(str[2]) < int(str[3]):
            loss_dict.update({str[0]:int(str[3])-int(str[2])})
    avg_dict.update({"Average profit": sum / num})
    all = [profit_dict, loss_dict, avg_dict]
with open("5_7.json", "w", encoding="utf-8") as f:
    json.dump(all ,f)