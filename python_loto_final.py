import random

class LotoCard():
    def __init__(self, name, quant):
        self.name = name
        self.quant = int(quant)
        self.total_list = [[' ' for _ in range(10)] for _ in range(self.quant)]
        self.output = []
        self.print = ''
        if self.name.lower() == 'игрок':
            self.output.append('______Ваша карточка______\n')
        elif self.name.lower() == 'компьютер':
            self.output.append('___Карточка компьютера___\n')
        self.lots = random.sample([i for i in range(20)], k=(self.quant*3))
        j = 0
        for k in range(len(self.total_list)):
            bubble = self.total_list[k]
            self.output.append('|')
            for i in range(3):
                bubble[i] = str(self.lots[j])
                if int(bubble[i]) < 10:
                    self.output.append(' ')
                j += 1
            random.shuffle(bubble)
            for i in range(len(bubble)):
                self.output.append(bubble[i])
                self.output.append(' ')
            self.output.append('|' + '\n')
        for i in self.output:
                self.print += str(i)
    def __str__(self):
        self.print = ''
        for i in self.output:
                self.print += str(i)
        return self.print

class Game():
    def __init__(self, card1, card2):
        self.num1 = card1.quant * 3
        self.num2 = card2.quant * 3
        self.nums = [i for i in range(20)]
        random.shuffle(self.nums)
        flag = 0
        for i in self.nums:
            if flag == 1:
                print('Вы проиграли!')
                break
            if (self.num1 == 0) and (self.num2 != 0):
                print('Вы победили!')
                break
            elif (self.num2 == 0) and (self.num1 != 0):
                print('Компьютер победил!')
                break
            elif (self.num2 == 0) and (self.num1 == 0):
                print('Ничья!')
                break
            print(card1)
            print(card2)
            answer = input(f'Есть ли у вас число {i}?\n')
            try:
                index = card1.output.index(str(i))
                if (answer == 'y'):
                    if int(card1.output[index]) > 9:
                        card1.output[index] = '- '
                    else:
                        card1.output[index] = '-'
                    self.num1 -= 1
                else:
                    print('Вы проиграли!')
                    break
            except ValueError:
                if (answer == 'n'):
                    pass
                else:
                    print('Вы проиграли!')
                    break
            try:
                index = card2.output.index(str(i))
                if int(card2.output[index]) > 9:
                    card2.output[index] = '- '
                else:
                    card2.output[index] = '-'
                self.num2 -= 1
            except ValueError:
                pass
strings = int(input('Введите количество строк: '))
player = LotoCard('Игрок',strings)
computer = LotoCard('Компьютер', strings)
game1 = Game(player,computer)

