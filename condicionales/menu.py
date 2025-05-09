# Operaciones Aritméticas
a = int(input("Escoja el primer número: "))
b = int(input("Escoja el segundo número: "))

print("S. suma\nR. Resta\nD. División\nM. Multiplicación")
opcion = input("Elija una opción: ")

if opcion == 'S':
    resultado = a + b
elif opcion == 'R':
    resultado = a - b
elif opcion == 'D':
    resultado = a / b
elif opcion == 'M':
    resultado = a * b
else:
    print("Valor no válido")

print(resultado)