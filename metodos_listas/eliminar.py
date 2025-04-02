carros = ['Porsche 911 Carrera S', 'Ferrrari Daytona', 'Spyker C8 Aileron', 'Mercedes Benz AMG GT63S', 'BMW M4 Competition']

# Eliminar un elemento por valor
carros.remove(3)

# Eliminar un elemento por índice y obtener su valor
valor_eliminado = carros.pop(1)

# Eliminar todos los elementos de la lista
carros.clear()

print(carros)
print("Valor Eliminado:", valor_eliminado)