# "Лоскутное одеяло"
# Игровое поле:
#   0 1 2 3 4    A[i][j]
# 0 - - - - -    i - строка 
# 1 - - - - -    j - столбец
# 2 - - - - -
# 3 - - - - -
#
N = 4  # количество строк
M = 5  # количество столбцов 
A = []
for i in range(N):
    A.append(['-']*M)
    
for i in range(len(A)):               # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):        # len(A[i]) - возвращает количество элементов в строке i, т е количество столбцов
        print(A[i][j], end = ' ')
    print()                           # делаем переход на новую строку 
    
a1 = 0
b1 = 0
c1 = 0
n = 0
    
while '-' in A[0] or '-' in A[1] or '-' in A[2] or '-' in A[3]:      
    
    while True:
        a = input(' Игрок 1, введите координаты для символа &: ')
        if len(a) != 2 or a.isdigit() == False or int(a[0]) < 0 or int(a[1]) < 0 or int(a[0]) > 3 or int(a[1]) > 4:
            print('Координаты введены неверно')
            continue
        elif A[int(a[0])][int(a[1])] != '-':
            print('Это место уже занято')
            continue
        else:
            A[int(a[0])][int(a[1])] = '&'
        for i in range(len(A)-1):
            for j in range(len(A[i])-1):
                if A[i][j] == A[i][j+1] != '-':
                    a1 += 1
                if A[i][j] == A[i+1][j] != '-':
                    a1 += 1
                elif A[i][j] == A[i+1][j+1] != '-':
                    a1 += 1
                elif A[i+1][j] == A[i][j+1] != '-':
                    a1 += 1
        for i in range(len(A)):               
            for j in range(len(A[i])):       
                print(A[i][j], end = ' ')
            print()                      
        print(f'Количество штрафных отчков Игрока 1 = {a1}')  
        print()
        break

    while True:
        b = input(' Игрок 2, введите координаты для символа $: ')
        if len(b) != 2 or b.isdigit() == False or int(b[0]) < 0 or int(b[1]) < 0 or int(b[0]) > 3 or int(b[1]) > 4:
            print('Координаты введены неверно')
            continue
        elif A[int(b[0])][int(b[1])] != '-':
            print('Это место уже занято')
            continue
        else:
            A[int(b[0])][int(b[1])] = '$'
        for i in range(len(A)-1):
            for j in range(len(A[i])-1):
                if A[i][j] == A[i][j+1] != '-':
                    b1 += 1
                if A[i][j] == A[i+1][j] != '-':
                    b1 += 1
                elif A[i][j] == A[i+1][j+1] != '-':
                    b1 += 1
                elif A[i+1][j] == A[i][j+1] != '-':
                    b1 += 1
        for i in range(len(A)):               
            for j in range(len(A[i])):       
                print(A[i][j], end = ' ')
            print()       
        print(f'Количество штрафных отчков Игрока 2 = {b1}')    
        print()
        break

    while True:
        c = input(' Игрок 3, введите координаты для символа #: ')
        if len(c) != 2 or c.isdigit() == False or int(c[0]) < 0 or int(c[1]) < 0 or int(c[0]) > 3 or int(c[1]) > 4:
            print('Координаты введены неверно')
            continue
        elif A[int(c[0])][int(c[1])] != '-':
            print('Это место уже занято')
            continue
        else:
            A[int(c[0])][int(c[1])] = '#'
        for i in range(len(A)-1):
            for j in range(len(A[i])-1):
                if A[i][j] == A[i][j+1] != '-':
                    c1 += 1
                if A[i][j] == A[i+1][j] != '-':
                    c1 += 1
                elif A[i][j] == A[i+1][j+1] != '-':
                    c1 += 1
                elif A[i+1][j] == A[i][j+1] != '-':
                    c1 += 1

        for i in range(len(A)):               
            for j in range(len(A[i])):       
                print(A[i][j], end = ' ')
            print()       
        print(f'Количество штрафных отчков Игрока 3 = {c1}')    
        print()
        break
    
    continue
    
players = [a1, b1, c1]
print(f'Игрок {players.index(min(players)) + 1} выиграл')    
