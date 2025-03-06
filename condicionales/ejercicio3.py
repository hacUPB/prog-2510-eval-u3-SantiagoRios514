# Determine si un número ingresado por el usuario es par o impar.

num = int(input("Ingrese un número entero: "))
if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} es impar")