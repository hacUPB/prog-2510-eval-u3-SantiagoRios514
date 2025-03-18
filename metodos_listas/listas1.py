# Ejercicio: 
# 1. Solicitar al usuario una frase de al menos 30 palabras
# 2. Contar cuántas palabras hay en la frase
# 3. Contar cuantos caracteres, incluyendo espacios en blanco que hay en el texto
# 4. Contar los caracteres sin espacios en blanco
# 5. Contar cuántas veces se repite la vocal A y la vocal E
# Regla para el resto del semestre:
# NO se permite el uso de list comprehensions, ni de funciones avanzadas

caracteres = 0

frase = input("Ingrese una frase de al menos 30 palabras: ")

lista_palabras = frase.split()
palabras = len(lista_palabras)

caracteres = len(frase)

blanco = frase.count(" ")
caracSin = caracteres - blanco

nA = frase.lower().count("a") + frase.lower().count("á")
nE = frase.lower().count("e") + frase.lower().count("é")

if palabras >= 30:
    print(f"En la frase hay {palabras} palabras")
    print(f"Hay {caracteres} caracteres en la frase")
    print(f"Hay {caracSin} caracteres (sin espacios)")
    print(f"La vocal 'A' aparece {nA} veces en la frase")
    print(f"La vocal 'E' aparece {nE} veces en la frase")
else:
    print("Ingrese una lista más larga")