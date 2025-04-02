print("Tabla de Conversión de Temperatura")
print("-"*40)
print("Grados Celsius  | Grados Fahrenheit")
print("-"*40)

for celsius in range(0,101,10):
    temp = (celsius * 9/5) + 32
    print(f"{celsius}\t\t|   {temp}")
print("-"*40)