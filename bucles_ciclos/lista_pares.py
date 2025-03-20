numeros_pares = []
n = int(input("Ingresa la cantidad de números pares a imprimir: "))
num = 0

for i in range(n):
    numeros_pares.append(num)
    num += 2

print(numeros_pares)