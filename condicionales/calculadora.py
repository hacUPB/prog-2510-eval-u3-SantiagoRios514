# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:21:33 2025

@author: B09S202est
"""
# Que se repita la ejecución del programa hasta que se elija E
operador = "0"
resultado = 0
opcion = "A"

while opcion != "E":
    print("*" * 60)
    print("Calculadora")
    print("*" * 60)

    print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potencia\nE. Salir")
    opcion = input("Elija la opción: ").upper()

    num1 = float(input("Ingrese el número 1: "))
    num2 = float(input("Ingrese el número 2: "))
    
    match opcion:
        case 'S':
            resultado = num1 + num2
            operador = "+"
        case 'R':
            resultado = num1 - num2
            operador = "-"
        case 'M':
            resultado = num1 * num2
            operador = "*"
        case 'D':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Indefinido"
            operador = "/"
        case 'P':
            resultado = num1 ** num2
            operador = "^"
        case _:
            print("Opción no válida")
    
    print(f"{num1} {operador} {num2} = {resultado}\n")