# "19"
# Игровое поле:
# '1 2 3 4 5 6 7 8 9    A[i][j]     Пара '1 имеет координаты: 1121
# '1 1 1 2 1 3 1 4 1    i - строка       '1
#  5 1 6 1 7 1 8 1 9    j - столбец
#  .....

import numpy as np
A = [[1,2,3,4,5,6,7,8,9], [1,1,1,2,1,3,1,4,1], [5,1,6,1,7,1,8,1,9]]
# Матрицы, которые понадобятся для "перезаписи игрового поля"
B = []
C = np.transpose(A)
    
# Переменные, которые понадобятся для "перезаписи игрового поля"    (if b == '': .......)
v = 3
l = 3                           # Количество строк игрового поля (начиная с нулевой и с учётом добавленной)
k = 0                           # Индекс элемента в строке 
n = 0                           # Счётчик на количество прибавленных строк

while True:

    for i in range(len(A)):                      # Вывод игрового поля
        for j in range(len(A[i])):  
            print(A[i][j], end = ' ')
        print()   

    a = input('Введите координаты для пары цифр, которые Вы хотите вычеркнуть: ')
    if len(a) != 4 or a.isalpha == False:
        print('Вы неверно ввели координаты')
    else:
        A[int(a[0])-1][int(a[1])-1] = '-'
        A[int(a[2])-1][int(a[3])-1] = '-'

    # "Перезапись игрового поля"
    for m in range(len(C)):
        if '-' in C[m]:
            C[m].remove('-')
    for m in range(len(A)):
        if '-' in A[m]:
            B.append(A[m].remove('-'))
        B.append(A[m])
        if B == []:
            print('Игра завершена')
            break
        for i in range(len(A)-1):
            for j in range(len(A[i])-1):
                for g in range(len(B)-1):
                    for d in range(len(B[g])-1):   
                        for m in range (len(C)-1):
                            for n in range(len(C[m])-1):
                                if B[g][d] + B[g][d+1] != 10 or A[i][j] + A[i+1][j] != 10 or B[g][d] != B[g+1][d] or A[i][j] != A[i+1][j] or C[m][n] + C[m][n+1] != 10 or C[m][n] + C[m+1][n] != 10:
                                    A.append([])                    # Добавляем пустую строку
                                    for i in range(v):
                                        for j in range(9):
                                            if A[i][j] != '-':
                                                A[l].append(A[i][j])
                                                k += 1
                                                if k == 9:
                                                    A.append([]) 
                                                    l += 1          # Переходим на новую строку
                                                    n += 1
                                                    k = 0
                                    v += n
