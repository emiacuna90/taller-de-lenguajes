numeros = []

while True:
    n = int(input("Ingrese un número (-1 para terminar): "))
    if n == -1:
        break
    numeros.append(n)

# Filtramos los que NO sean múltiplos de 3
filtrados = [num for num in numeros if num % 3 != 0]

# Convertimos a string y unimos con guiones
resultado = "-".join(map(str, filtrados))

print("Resultado:", resultado)
