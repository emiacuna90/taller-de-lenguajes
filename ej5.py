lista = [1,2,3,4,5,6,-7,8,9,10]
for i in lista:
    if (i > 0 and i % 2 == 0):
        print('El numero',i,'es par')
    elif  (i < 0):
        print('El numero',i,'es negativo')
        break