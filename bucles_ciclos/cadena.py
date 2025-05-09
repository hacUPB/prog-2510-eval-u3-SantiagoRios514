# Creamos una cadena de caracteres
cadena1 = "Hola"

# Asignamos la cadena a otra variable
cadena2 = cadena1

# Intentamos modificar la cadena2 (esto generará un error)
try:
    cadena2 += " Mundo"
except TypeError as e:
    print(f"Error: {e}")

# Imprimimos ambas cadenas
print("Cadena 1:", cadena1)
print("Cadena 2:", cadena2)