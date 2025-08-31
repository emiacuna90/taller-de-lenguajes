lista = [1,2,3,4,5,6,7,8,9,10]
pares = []
impares = []
for i in lista:
    if (i % 2 == 0):
        pares.append(i)
    else :
        impares.append(i)
    
print('Lista de numeros pares: ')
for j in pares:
    print(j)
    
print('Lista de numeros impares: ')
for k in impares:
    print(k)