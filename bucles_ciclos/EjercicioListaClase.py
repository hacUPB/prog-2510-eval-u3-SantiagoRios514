# Crear una lista con su top 5 de canciones favoritas
# Crea otra lista con el artista que la interpreta
canciones = ['GOLDEN GUN', 'LOYALTY', 'Oe Bebé', 'FKU', 'Chica Virtual']
artistas = ['Álvaro Díaz', 'Kendrick Lamar y Rihanna', 'Maluma y Blessd', 'Feid', 'Arcángel']

# Se está inicializando el índice en 0. Después, mientras el índice sea menor que cinco imprime la canción en la posición [indice], 
# seguida por el intérprete en la posición [indice].
# Finalmente le suma 1 a la variable indice.
indice = 0
while indice < 5:
    print(f"{canciones[indice]}, Interpretada por: {artistas[indice]}")

# El bucle range por defecto inicia la variable i en 0 y la aumenta de 1 en 1, hasta la posición n-1, en este caso: 4.
for i in range(5):
    print(f"{canciones[i]}, Interpretada por: {artistas[i]}")

# 
for cancion in canciones:
    print(cancion)