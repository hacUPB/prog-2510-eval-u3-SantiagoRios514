print("*" * 60)
print("Restaurante de Comida Rápida")
print("*" * 60)

print("Menú:\nH. Hamburguesa\nP. Pollo Frito\nS. Sándwich de Pollo")
plato = input("Ingrese el plato que desea: ").upper()

match plato:
    case 'H':
        print("\nAcompañamientos disponibles:\n0. Sin acompañamiento\n1. Papas fritas\n2. Aros de cebolla\n3. Ensalada")
        print("\nBebidas disponibles:\n0. Sin bebida\n1. Coca-Cola\n2. Jugo de naranja\n3. Té helado\n4. Agua")
        acompaniamiento = int(input("Seleccione un acompañamiento (1-3): "))
        bebida = int(input("Seleccione una bebida (1-4): "))
        match acompaniamiento:
            case 1:
                print("Ha elegido: Papas fritas")
                ac_final = "Papas fritas"
            case 2:
                print("Ha elegido: Aros de cebolla")
                ac_final = "Aros de cebolla"
            case 3:
                print("Ha elegido: Ensalada")
                ac_final = "Ensalada"
            case _:
                print("No eligió ningún acompañamiento")
                ac_final = ""
        match bebida:
            case 1:
                print("Ha elegido: Coca-Cola")
                bebida_final = "Coca-Cola"
            case 2:
                print("Ha elegido: Jugo de naranja")
                bebida_final = "Jugo de naranja"
            case 3:
                print("Ha elegido: Té helado")
                bebida_final = "Té helado"
            case 4:
                print("Ha elegido: Agua")
                bebida_final = "Agua"
            case _:
                print("No eligió ninguna bebida")
                bebida_final = ""
    case 'P':
        print("\nAcompañamientos disponibles:\n0. Sin acompañamiento\n1. Ensalada\n2. Puré de papa\n3. Arroz")
        print("\nBebidas disponibles:\n0. Sin bebida\n1. Coca-Cola\n2. Jugo de naranja\n3. Té helado\n4. Agua")
        acompaniamiento = int(input("Seleccione un acompañamiento (1-3): "))
        bebida = int(input("Seleccione una bebida (1-4): "))
        match acompaniamiento:
            case 1:
                print("Ha elegido: Ensalada")
                ac_final = "Ensalada"
            case 2:
                print("Ha elegido: Puré de papa")
                ac_final = "Puré de papa"
            case 3:
                print("Ha elegido: Arroz")
                ac_final = "Arroz"
            case _:
                print("No eligió ningún acompañamiento")
                ac_final = ""
        match bebida:
            case 1:
                print("Ha elegido: Coca-Cola")
                bebida_final = "Coca-Cola"
            case 2:
                print("Ha elegido: Jugo de naranja")
                bebida_final = "Jugo de naranja"
            case 3:
                print("Ha elegido: Té helado")
                bebida_final = "Té helado"
            case 4:
                print("Ha elegido: Agua")
                bebida_final = "Agua"
            case _:
                print("No eligió ninguna bebida")
                bebida_final = ""
    case 'S':
        print("\nAcompañamientos disponibles:\n0. Sin acompañamiento\n1. Papas fritas\n2. Aros de cebolla\n3. Ensalada")
        print("\nBebidas disponibles:\n0. Sin bebida\n1. Coca-Cola\n2. Jugo de naranja\n3. Té helado\n4. Agua")
        acompaniamiento = int(input("Seleccione un acompañamiento (1-3): "))
        bebida = int(input("Seleccione una bebida (1-4): "))
        match acompaniamiento:
            case 1:
                print("Ha elegido: Papas fritas")
                ac_final = "Papas fritas"
            case 2:
                print("Ha elegido: Aros de cebolla")
                ac_final = "Aros de cebolla"
            case 3:
                print("Ha elegido: Ensalada")
                ac_final = "Ensalada"
            case _:
                print("No eligió ningún acompañamiento")
                ac_final = ""
        match bebida:
            case 1:
                print("Ha elegido: Coca-Cola")
                bebida_final = "Coca-Cola"
            case 2:
                print("Ha elegido: Jugo de naranja")
                bebida_final = "Jugo de naranja"
            case 3:
                print("Ha elegido: Té helado")
                bebida_final = "Té helado"
            case 4:
                print("Ha elegido: Agua")
                bebida_final = "Agua"
            case _:
                print("No eligió ninguna bebida")
                bebida_final = ""
    case _:
        print("Plato no válido")
        ac_final = ""
        bebida_final = ""

eliminar = input("¿Desea eliminar algún ingrediente? (S/N): ").upper()

if eliminar == 'S':
    print("\nIngredientes actuales:")
    match plato:
        case 'H':
            print("Pan\nCarne de res\nLechuga\nTomate\nQueso\nSalsa especial")
        case 'P':
            print("2 presas de pollo\nPapas fritas\nSalsas a tu elección")
        case 'S':
            print("Pan\nPollo desmechado\nLechuga\nTomate\nQueso")
    ing_el = input("Ingrese el ingrediente a eliminar: ").capitalize()

print("\nSu pedido final es:")
match plato:
    case 'H':
        print(f"Plato: Hamburguesa")
        if ing_el != "":
            print(f"Sin {ing_el}")
    case 'P':
        print(f"Plato: Pollo Frito")
        if ing_el != "":
            print(f"Sin {ing_el}")
    case 'S':
        print(f"Plato: Sándwich de Pollo")
        if ing_el != "":
            print(f"Sin {ing_el}")
if ac_final != "":
    print(f"Acompañamiento: {ac_final}")
if bebida_final != "":
    print(f"Bebida: {bebida_final}")