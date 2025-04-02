print("-"*50)
print("Simulación de desintegración orbital de un satélite en la atmósfera")
print("-"*50)

altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en kilómetros): "))
coef_arrastre_inicial = float(input("Introduzca el coeficiente de arrastre inicial (valor decimal pequeño, ej. 0.01): "))
altitud_minima_segura = float(input("Ingrese la altitud mínima segura (en kilómetros): "))

altitud_actual = altitud_inicial
coef_arrastre = coef_arrastre_inicial
estabilizacion = 0.005
orbitas = 0

print("\nSimulando la desintegración orbital...")
while True:
    orbitas += 1
    
    altitud_perdida = coef_arrastre * altitud_actual
    altitud_actual -= altitud_perdida
    
    coef_arrastre += 0.0001
    
    print(f"Órbita {orbitas}: Altitud actual = {altitud_actual:.4f} km, Coeficiente de arrastre = {coef_arrastre:.4f}")
    
    if altitud_actual <= altitud_minima_segura:
        print(f"\nEl satélite ha reingresado en la atmósfera terrestre después de {orbitas} órbitas.")
        break
    elif altitud_perdida < estabilizacion:
        print(f"\nEl satélite se ha estabilizado en una órbita a {altitud_actual:.4f} km después de {orbitas} órbitas.")
        break