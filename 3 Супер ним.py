# "Супер ним"
# Расшифровка координат:
#    0 1 2 3 4 5 6'7  
#  0 - - - - - - - 0     '3: r3
#  1 - - - - - - - 0     '7: c7
#  2 - - - - - - - 0      
# '3 0 - 0 - 0 0 - -      row - строка
#  4 - - - - - - - -      column - столбец
#  5 - - - - - - - -       A[i][j]
#  6 - - - - - - - 0       i - строка 
#  7 - - - - - - - -       j - столбец

import random
N = 8  # количество строк
M = 8  # количество столбцов 
A = []
for i in range(N):
    A.append([0]*M)
    
for i in range(N):                    # заполняем матрицу 
    for j in range(M):
        A[i][j] = random.choice('0-')
        
for i in range(len(A)):               # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):        # len(A[i]) - возвращает количество элементов в строке i, т е количество столбцов
        print(A[i][j], end = ' ')
    print()                           # делаем переход на новую строку 
        
while '0' in A[0] or '0' in A[1] or '0' in A[2] or '0' in A[3] or '0' in A[4] or '0' in A[5] or '0' in A[6] or '0' in A[7]:
    a = input('Введите координаты строки/столбца: ')
    if len(a) != 2:
        print('Координаты введены неверно')
        continue
    if a[0] == 'r':
        for i in range(0,8):
            A[int(a[1])][i] = '-'
    elif a[0] == 'c':
        for i in range(0,8):
            A[i][int(a[1])] = '-'
    else:
        print('Координаты введены неверно')
        continue
    for i in range(len(A)):           # Выводим матрицу
        for j in range(len(A[i])):        
            print(A[i][j], end = ' ')
        print()  
    continue
    
print('Игра завершена')
