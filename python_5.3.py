with open('5.3.txt', encoding="utf-8") as f:
    avgsum = 0
    avgnum = 0
    while True:
        d = f.readline()
        if d == '':
            break
        d = d.split()
        if int(d[1]) < 20000:
            print(" ".join(d))
        avgsum += int(d[1])
        avgnum += 1
    print(f'Средний доход сотрудников - {avgsum/avgnum}')