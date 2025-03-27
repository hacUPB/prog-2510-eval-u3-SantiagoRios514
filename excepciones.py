num1 = 45
num2 = "e"

try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Estás ingresando un valor incorrecto.")
except:
    print("No se pudo ejecutar la acción.")

try:
    resultado = num1 / numero
except ZeroDivisionError:
    print("Resultado indeterminado.")
except:
    print("No se pudo ejecutar la acción.")