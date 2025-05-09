# Un almacén cobra $9 000 por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a $100 000. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.

envio = 9000
compra = int(input("Ingrese el valor de la compra: "))
if compra >= 100000:
    envio = 0
total = compra + envio
print(f"El total de la compra es {total}")