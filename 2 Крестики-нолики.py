# Расшифровка координат 

#   0 1 2    a имеет координаты 12
# 0 - - -    1 - строка, 2 - столбец
# 1 - - a
# 2 - - -

Ls0 = ['-','-','-']
Ls1 = ['-','-','-']
Ls2 = ['-','-','-']
n = 0

while '-' in Ls0  or  '-' in Ls1  or  '-' in Ls2:
    if n != 0:
            print(' Следующий ход')
            
    while True:
        try:
            a = input('Введите координаты x: ')
            for i in range(0,2):
                if int(a[i]) not in range(0,3): 
                    n -= 1
                    print('Вы неверно ввели координаты для x')
                    continue
            if int(a[0]) == 0:                     # берем строку s0
                if Ls0[int(a[1])] == '-':
                    Ls0[int(a[1])] = 'x'
                else:
                    print('Это место уже занято')
                    continue
            if int(a[0]) == 1:                     # берем строку s1
                if Ls1[int(a[1])] == '-':
                    Ls1[int(a[1])] = 'x'
                else:
                    print('Это место уже занято')
                    continue
            if int(a[0]) == 2:                     # берем строку s2
                if Ls2[int(a[1])] == '-':
                    Ls2[int(a[1])] = 'x'
                else:
                    print('Это место уже занято')
                    continue
            n += 1
            break
        except ValueError as err:
                print(err)
            
    while True:
        try:
            b = input('Введите координаты 0: ')        
            for i in range(0,2):       
                if int(b[i]) not in range(0,3):
                    print('Вы неверно ввели координаты для 0')
                    continue
            if int(b[0]) == 0:                     # берем строку s0
                if Ls0[int(b[1])] == '-':
                    Ls0[int(b[1])] = '0'
                else:
                    print('Это место уже занято')
                    continue
            if int(b[0]) == 1:                     # берем строку s1
                if Ls1[int(b[1])] == '-':
                    Ls1[int(b[1])] = '0'
                else:
                    print('Это место уже занято')
                    continue
            if int(b[0]) == 2:                     # берем строку s2
                if Ls2[int(b[1])] == '-':
                    Ls2[int(b[1])] = '0'
                else:
                    print('Это место уже занято') 
                    continue
            break
        except ValueError as err:
            print(err)
            
    print(*Ls0, sep = ' ')
    print(*Ls1, sep = ' ')
    print(*Ls2, sep = ' ')
    continue 
    
if n == 5:                              # Это означает, что игра окончена и нужно определить, есть ли победитель и кто он
    for i in range(0,3):                # Проверка по столбцам
        if Ls0[i] == Ls1[i] == Ls2[i]:  
            print('Выиграл ',Ls0[i])  
            
    if len(set(Ls0)) == 1:              # Проверка по строкам
        print('Выиграл ',Ls0[0])
    if len(set(Ls1)) == 1:
        print('Выиграл ',Ls1[0])    
    if len(set(Ls2)) == 1:
        print('Выиграл ',Ls2[0])
        
    if Ls0[0] == Ls1[1] == Ls2[2]:       # Проверка по диагоналям
        print('Выиграл ',Ls0[0])
    if Ls0[2] == Ls1[1] == Ls2[0]:
        print('Выиграл ',Ls0[2])
    else:
        print('Ничья')
