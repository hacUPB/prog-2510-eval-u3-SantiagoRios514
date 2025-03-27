# Creamos una lista mutable
lista1 = [32, 64, 35]

# Asignamos la lista a otra variable
lista2 = lista1
lista3 = lista2.copy()

# Modificamos la lista2
lista2.append(4)

# Imprimimos ambas listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)