# import fraccion
# from fraccion import mcd, imprime_fraccion
from fraccion import *

# Función principal
def main():
    num1 = int(input("Ingrese el numerador: "))
    num2 = int(input("Ingrese el denominador: "))
    maximo = mcd(num1, num2)
    print(f"Máximo Común Divisor: {maximo}")
    imprime_fraccion(num1, num2, maximo)

if __name__ == "__main__":
    main()