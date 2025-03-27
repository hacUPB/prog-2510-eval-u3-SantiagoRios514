num = int(input("Ingrese un número entero positivo, para hacer la tabla de multiplicar: "))
contador = 1
print(f"Tabla de multiplicar del {num}:")
while contador <= 10:
    resultado = num * contador
    print(f"{num} x {contador} = {resultado}")
    contador += 1