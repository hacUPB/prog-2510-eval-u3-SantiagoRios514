def determinar_dia(num):
    if num >= 1 and num <= 7:
        match num:
            case 1:
                dia = 'Lunes'
            case 2:
                dia = 'Martes'
            case 3:
                dia = 'Miércoles'
            case 4:
                dia = 'Jueves'
            case 5:
                dia = 'Viernes'
            case 6:
                dia = 'Sábado'
            case 7:
                dia = 'Domingo'
        return dia

def convertir_puntuacion(puntaje:int):
    if puntaje >= 0 and puntaje <= 100:
        if puntaje < 60:
            nota = 'F'
        elif puntaje < 70:
            nota = 'D'
        elif puntaje < 80:
            nota = 'C'
        elif puntaje < 90:
            nota = 'B'
        else:
            nota = 'A'
        return nota

def main():
    puntaje = int(input("Ingrese el puntaje numérico (0-100): "))
    nota = convertir_puntuacion(puntaje)
    if nota == None:
        print("Puntaje Inválido")
    else:
        print(f"La calificación correspondiente es: {nota}.")
    
    numDia = int(input("Ingrese un número de día: "))
    dia = determinar_dia(numDia)
    if dia == None:
        print("Número de día inválido.")
    else:
        print(f"El día {numDia} corresponde al {dia}.")

if __name__ == "__main__":
    main()