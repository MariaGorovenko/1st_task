import random
line = ['0','1','2','3','4','5','6','7','8','9']
b = ''
n = 1
while n <= 4:
    a = random.choice(line)
    b += a
    n += 1
biki = 0
korovi = 0
c = 0
while True:
    chislo = input(' Введите число из четырёх символов: ')
    if len(chislo) != 4:
        print('Вы ввели число неверной длины!')
        continue
    if chislo.isdigit() == False:
        print('Вы ввели число неверного формата!')
        continue
    c += 1
    if chislo == b:
        print('Победа!')
        break
    for i in range(0,4):
        if chislo[i] == b [i]:
            biki += 1
        if chislo[i] in b:
            korovi += 1
    print('быки = ',biki)
    print('коровы = ',korovi)
    if biki == korovi == 0:
        print('Не угадали')
    print('Количество ходов = ',c)
    print('Продолжаем игру!')
    biki = 0
    korovi = 0
    continue
