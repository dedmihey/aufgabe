N = int(input('Введите интервал поиска от 0 до '))
k = 3
m = 2
print(0)
print(1)
print(2)
while k < N:
    if k % m != 0 and k != m:
        m += 1
    else:
        if k % m == 0 and k == m:
            print(k)
            k += 1
            m = 2
        else:
            k += 1
            m = 2



