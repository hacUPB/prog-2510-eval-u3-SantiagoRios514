# Condicional simple: Si al solicitarle el número de teléfono a una persona y el número de dígitos es diferente a 10, imprimir en pantalla: "No es un número valido"

'''
num = input("Ingrese el número telefónico: ")
c = 0
for digito in num:
    c = c + 1
if c != 10:
    print("No es un número válido.")
'''

# En un hospital quieren saber cuántos de los niños nacidos en 2024 son niños o niñas para regalar a los padres un descuento de 50 dólares en la cuenta del hospital si son niñas.
# En caso contrario, solo tendrá un descuento de 30 dólares. Solicite a los padres el sexo del niño y calcule el descuento.

cuenta = float(input("Ingrese la cuenta a pagar"))
sexo = input("Ingrese 1 si su recién nacido es niña y 0 si su recién nacido es niño: ")
if sexo == 1:
    descuento = cuenta - 50
else:
    descuento = cuenta - 30
print(f"El descuento en la cuenta es de: {descuento}")