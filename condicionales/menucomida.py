# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 15:21:51 2025

@author: B09S202est
"""
# Crear un menú con diferentes platos
# Cuando el usuario selecciona uno, se debe imprimir que contiene el plato

print("*" * 60)
print("Restaurante")
print("*" * 60)

print("L. Lasaña\nA. Arroz con Pollo\nP. Pollo frito")
plato = input("Ingrese el plato que desea: ").upper()

match plato:
    case 'L':
        print("\n El plato contiene: \n- Pasta de lasaña\n- Salsa Bechamel casera\n- Carne molida de res\n- Pollo Desmechado\nEstá acompañado de dos panes")
    case 'A':
        print("\n El plato contiene: \n- Arroz blanco\n- Salsa de la casa\n- Pollo desmechado\n- Arvejas\n- Zanahoria\nEstá acompañado de chips de arracacha")
    case 'P':
        print("\n El plato contiene: \n- 2 presas de pollo\n- Papas Fritas\n- Salsas a tu elección")