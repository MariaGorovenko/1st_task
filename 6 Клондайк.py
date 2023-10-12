# Клондайк
# Игровое поле: 
#    1 2 3 4 5 6 7 8 9 10
#  1 - - - - - - - - - -     a : 54
#  2 - - - - - - - - - -     b : 98
#  3 - - - - - - - - - -
#  4 - - - - - - - - - -
#  5 - - - a - - - - - -
#  6 - - - - - - - - - -
#  7 - - - - - - - - - -
#  8 - - - - - - - - - -
#  9 - - - - - - - b - -
# 10 - - - - - - - - - -

A = []
N = 10
M = 10
n = 0
for i in range(N):
    A.append(['-'] * M)
    
def output_A():
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end = ' ')
        print()
output_A()
while True:
    
    a = input('Введите координаты фишки: ')
    if len(a) != 2 or a.isalpha == False:
        print('Вы неверно ввели координаты')
        continue
    else:
        A[int(a[0])-1][int(a[1])-1] = '0'
        
    output_A()
    
    for i in range(1,9):
        for j in range(1,9):
            if A[i][j] == A[i][j+1] == '0':
                n += 1
            if A[i][j] == A[i][j-1] == '0':
                n += 1
            if A[i][j] == A[i+1][j] == '0':
                n +=1
            if A[i][j] == A[i-i][j] == '0':
                n += 1
            if A[i][j] == A[i+1][j+1] == '0':
                n += 1
            if A[i][j] == A[i-1][j-1] == '0':
                n += 1
            if A[i][j] == A[i-1][j+1] == '0':
                n += 1
            if A[i][j] == A[i+1][j-1] == '0':
                n += 1
    if n > 1:
        print('Вы проиграли')
        break
