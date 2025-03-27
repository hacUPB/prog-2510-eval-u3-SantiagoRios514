def mcd(num, den):
    if num <= den:
        menor = num
    else:
        menor = den
    
    for i in range(menor, 0, -1):
        if num % i == 0 and den % i == 0:
            return i
            break

def imprime_fraccion(num, den, maximo):
    print(f"Fracción Original: {num}/{den}")
    num = num/maximo
    den = den/maximo
    print(f"Fracción Simplificada: {int(num)}/{int(den)}")

def main():

    num1 = int(input("Ingrese el numerador: "))
    num2 = int(input("Ingrese el denominador: "))
    maximo = mcd(num1, num2)
    print(f"Máximo Común Divisor: {maximo}")
    imprime_fraccion(num1, num2, maximo)

if __name__ == "__main__":
    main()