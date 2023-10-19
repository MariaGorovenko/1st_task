# Максит
# Игровое поле:     3 имееет кординаты: 12
#   6 3 5
#   1 0 8 
#   7 4 9

import random
N = 3
M = 3
A = []
a1 = 0
b1 = 0
r = 0
c = 0
for i in range(N):
    A.append(random.choice('123456789') * M)
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()

while True:    
    a = input('Игрок 1, введите координаты числа: ')
    if len(a) != 2 or a.isalpha == False:
        print('Вы неверно ввели координаты')
        continue
    else:
        a1 += int(A[int(a[0])-1][int(a[1])-1])
        A[int(a[0])-1][int(a[1])-1] = '-'    # Эта строка непонятно от чего не работает!!! Хотя в предыдущей задаче работала
        c = int(a[1])-1            # Из какого стобца игрок 2 дальше должнем будет выбрать число
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = ' ')
        print()
    break
    
while True:
    while True:
        b = input(f'Игрок 2, введите номер числа из {c} столбца: ')
        if len(b) != 1 or b.isalpha == False or A[int(b)-1][c] == '-':
            print('Вы неверно ввели координаты')
            continue
        else:
            b1 += int(A[int(b)-1][c])
            A[int(b)-1][c] = '-'
            r = int(b)-1           # Из какой строки игрок 1 дальше должен будет выбрать число 
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], end = ' ')
            print()
        break
         
    while True:    
        a = input(f'Игрок 1, введите номер числа из {r} строки: ')
        if len(a) != 1 or a.isalpha == False or A[r][int(a)-1] == '-':
            print('Вы неверно ввели координаты')
            continue
        else:
            a1 += int(A[r][int(a)])
            A[r][int(a)] = '-'
            c = int(a)-1
        for i in range(len(A)):
            for j in range(len(A[i])):
                print(A[i][j], end = ' ')
            print()
        break
