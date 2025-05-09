'''
El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de tener una idea sobre su vulnerabilidad. 
Diseñe un algoritmo que pida al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. Verifique que el usuario no ingrese valores menores a cero. 

Clasificación etaria de la población colombiana:
- Primera Infancia (0-5 años)
- Infancia (6 - 11 años)
- Adolescencia (12 - 18 años)
- Juventud (14 - 26 años)
- Adultez (27- 59 años)
- Persona Mayor (60 años o más) envejecimiento y vejez

Trata de escribir tu propia versión antes de revisar la solución.'
'''

edad = int(input("Ingrese su edad: "))

if edad >= 0:
    if edad <= 5:
        etapa = "Primera Infancia"
    elif edad <= 11:
        etapa = "Infancia"
    elif edad <= 14:
        etapa = "Adolescencia"
    elif edad <= 18:
        etapa = "Jóven Adolescente"
    elif edad <= 26:
        etapa = "Juventud"
    elif edad <= 59:
        etapa = "Adultez"
    else:
        etapa = "Persona mayor (Envejecimiento y vejez)"
else:
    print("Edad no válida.")