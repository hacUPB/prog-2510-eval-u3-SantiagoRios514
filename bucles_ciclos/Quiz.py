s_restante = 50
print(f"Bienvenido al sistema de inventario. Stock disponible: {s_restante}")
while s_restante > 0:
    comprar = int(input("¿Cuántos productos quieres comprar? "))
    if comprar <= s_restante and comprar > 0:
        s_restante -= comprar
        print(f"Compra realizada. Stock restante: {s_restante}")
    elif comprar > s_restante:
        print("No hay suficientes productos disponibles.")
    elif comprar < 0:
        print("Ingrese un valor positivo.")
    else:
        break
if s_restante == 0:
    print("Inventario agotado.")