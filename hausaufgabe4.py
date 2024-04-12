import random

x = random.randint(0, 100)
y = -1
while x - y != 0:
    y = int(input('Введите число от 0 до 100: '))
    if x - y == 0:
        print('Вы выиграли')
        break
    if x - y > 10:
        print('Ваше число существенно меньше заданного')
    if x - y > 0 and x - y <= 10:
        print('Ваше число меньше заданного')
    if y - x > 10:
        print('Ваше число существенно больше заданного')
    if y - x > 0 and y - x <= 10:
        print('Ваше число больше заданного')

