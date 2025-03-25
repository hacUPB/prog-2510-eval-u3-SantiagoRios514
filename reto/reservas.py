import random

tit = input("Ingrese su título (Sr., Sra., etc.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print(f"{tit} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!\n")

ciudad_o = input("Ingrese la ciudad de origen de su vuelo (Medellín, Bogotá, Cartagena): ")
ciudad_d = input("Ingrese la ciudad de destino de su vuelo (Medellín, Bogotá, Cartagena): ")
dia_s = input("Ingrese el día de la semana (por ejemplo, lunes): ").lower()
dia_m = int(input("Introduzca el día del mes (1-30): "))
print("Tipos de asiento:\nC. Pasillo \nA. Ventana\nB. Sin preferencia")
tipo_asiento = input("¿Qué asiento prefiere? ").upper()

if (ciudad_o == 'Medellín' and ciudad_d == 'Bogotá') or (ciudad_o == 'Bogotá' and ciudad_d == 'Medellín'):
    dist = 240
elif (ciudad_o == 'Medellín' and ciudad_d == 'Cartagena') or (ciudad_o == 'Cartagena' and ciudad_d == 'Medellín'):
    dist = 461
elif (ciudad_o == 'Bogotá' and ciudad_d == 'Cartagena') or (ciudad_o == 'Cartagena' and ciudad_d == 'Bogotá'):
    dist = 657
else:
    print("Vuelo inválido")

if dist < 400:
    precios = [79900, 119900]
else:
    precios = [156900, 213000]

if dia_s == ('viernes' or 'sábado' or 'domingo'):
    precio = precios[1]
else:
    precio = precios[0]

num_asiento = random.randint(1,29)

print(f"Tu vuelo de {ciudad_o} a {ciudad_d} el {dia_s} {dia_m} de abril está reservado.")
print(f"Precio del boleto: ${precio}")
print(f"Tu asiento es: {num_asiento}{tipo_asiento}")