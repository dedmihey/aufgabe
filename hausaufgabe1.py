year_ = int(input('Введите год '))
if year_ % 4 == 0 and (year_ % 100 != 0 or year_ % 400 == 0):
        print('Год високосный')
else:
    print('Год невисокосный')
