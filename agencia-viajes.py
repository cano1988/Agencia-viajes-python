# Agencia de viajes
# Programa realizado por Andrés Cano Rave

# Constantes del destino
dest1 = "La Guajira"
dest2 = "El Cañón de Chicamocha"
dest3 = "Los Llanos Orientales"

# Variables de la suma de personas totales
totalGuajira = 0
totalChicamocha = 0
totaLlanosOrientales = 0

# Acumuladores de las personas que viajan
AdultosGua = 0
AdultosChi = 0
AdultosLla = 0
NiñosGua = 0
NiñosChi = 0
NiñosLla = 0

# Variables de los $ subtotales
subtotal = 0
subtotalGua = 0
subtotalChi = 0
subtotalLla = 0

# Acumuladores de dinero
totalDinGua = 0
totalDinChi = 0
totalDinLla = 0


# Constante de los precios para persona adulta
dest1ValAdu = 1450000
dest2ValAdu = 1600000
dest3ValAdu = 1200000
# Constante de los precios para Niños
dest1ValNi = 870000
dest2ValNi = 960000
dest3ValNi = 720000


print("")
print("****************************INICIO**********************************")
print("Programa que permite a una agencia la venta de paquetes turísticos\n")
print("Estos son nuestros paquetes turísticos:\n")

print(" -----------------------------------------------------------------")
print("|      Destino          Valor persona adulto   Valor persona niño |")
print("|  -------------------  --------------------   ------------------ |")
print("|1.  Guajira                  $1.450.000             $870.000     |")
print("|2.  Cañón de chicamocha      $1.600.000             $960.000     |")
print("|3.  Llanos Orientales        $1.200.000             $720.000     |")
print(" ----------------------------------------------------------------- ")


# Se le pregunta al cliente datos iniciales
while True:
    nom_cliente = str(
        input("Favor digite su nombre o digite 'no' para salir: "))
    if nom_cliente.lower().strip() == "no":
        break
    perso_adultas = int(
        input("Favor digite la cantidad de personas adultas que viajan: "))
    perso_niños = int(input("Favor digite la cantidad de niños que viajan: "))

    print("")
    print("Elija el destino que desea: ")
    print("1.  Guajira")
    print("2.  Cañón de chicamocha")
    print("3.  Llanos orientales")
    print("4.  Salir")
    print("")
    # El cliente debe escoger el nñumero de las tres opciones posibles
    dest = int(
        input("Digite el número del destino deseado o digite '4' para finalizar cotización: "))
    if dest == 4:
        print("********VUELVE PRONTO :)********")
        break
    elif dest == 1:  # Destino de viaje 1
        # Acumulador de la sumatoria de Adultos para la opción Guajira
        AdultosGua += perso_adultas
        NiñosGua += perso_niños  # Acumulador de la sumatoria de Niños para la opción Guajira
        totalGuajira = AdultosGua + NiñosGua

        print("El destino elegido es La Guajira")

    elif dest == 2:  # Destino de viaje 2
        # Acumulador de la sumatoria de Adultos para la opción Chicamocha
        AdultosChi += perso_adultas
        # Acumulador de la sumatoria de Niños para la opción Chicamocha
        NiñosChi += perso_niños
        totalChicamocha = AdultosChi + NiñosChi
        print("El destino es El cañón de chicamocha")

    elif dest == 3:  # Destino de viaje 3
        # Acumulador de la sumatoria de Adultos para la Llanos Orientales
        AdultosLla += perso_adultas
        # Acumulador de la sumatoria de Niños para la opción Llanos Orientales
        NiñosLla += perso_niños
        totaLlanosOrientales = AdultosLla + NiñosLla
        print("El destino elegido es Los llanos orientales")

    else:
        print("opción de destino incorrecta")
        break

    print("")
    print("Para continuar elija el número de la operación que desea realizar: ")
    print("1. Imprimir cotización del cliente")
    print("2. Realizar nueva cotización")
    print("3. Finalizar proceso e imprimir informe general")
    print("")
    # El cliente debe escoger
    ope = int(input("Digite el número de la operación que desea realizar: "))
    print("")

    if ope == 1:
        print("Su cotización es la siguiente: ")
        print(f"Nombre del cliente: {nom_cliente} ")
        if dest == 1:
            subtotalGua = ((dest1ValAdu * perso_adultas) +
                           (dest1ValNi * perso_niños))
            subtotal = subtotalGua
            totalDinGua += subtotalGua
            print(f"Nombre del destino: {dest1}")
        elif dest == 2:
            subtotalChi = ((dest2ValAdu * perso_adultas) +
                           (dest2ValNi * perso_niños))
            subtotal = subtotalChi
            totalDinChi += subtotalChi
            print(f"Nombre del destino: {dest2}")
        elif dest == 3:
            subtotalLla = ((dest3ValAdu * perso_adultas) +
                           (dest3ValNi * perso_niños))
            subtotal = subtotalLla
            totalDinLla += subtotalLla
            print(f"Nombre del destino: {dest3}")
        print(f"Número de personas adultas es: {perso_adultas}")
        print(f"Número de niños es: {perso_niños}")
        print(f"Subtotal es igual a:${subtotal}")
        print("")
        print("Nueva Cotización")

    elif ope == 2:
        if dest == 1:
            subtotalGua = ((dest1ValAdu * perso_adultas) +
                           (dest1ValNi * perso_niños))
            totalDinGua += subtotalGua
        elif dest == 2:
            subtotalChi = ((dest2ValAdu * perso_adultas) +
                           (dest2ValNi * perso_niños))
            totalDinChi += subtotalChi
        elif dest == 3:
            subtotalLla = ((dest3ValAdu * perso_adultas) +
                           (dest3ValNi * perso_niños))
            totalDinLla += subtotalLla
        print("Nueva Cotización")
    elif ope == 3:
        if dest == 1:
            subtotalGua = ((dest1ValAdu * perso_adultas) +
                           (dest1ValNi * perso_niños))
            totalDinGua += subtotalGua
        elif dest == 2:
            subtotalChi = ((dest2ValAdu * perso_adultas) +
                           (dest2ValNi * perso_niños))
            totalDinChi += subtotalChi
        elif dest == 3:
            subtotalLla = ((dest3ValAdu * perso_adultas) +
                           (dest3ValNi * perso_niños))
            totalDinLla += subtotalLla
        # impresión de informe general
        print("A continuación se imprime informe general:")
        print("")
        print("****INFORME GENERAL********")
        print("")
        print(
            f"Cantidad de personas que viajan a La Guajira es: {totalGuajira}")
        print(
            f"Cantidad de personas que viajan a El Cañón de Chicamocha:{totalChicamocha} ")
        print(
            f"Cantidad de personas que viajan a Los Llanos Orientales:{totaLlanosOrientales}")
        print(f"El total de dinero de los viajes a La Guajira:${totalDinGua} ")
        print(
            f"El total de dinero de los viajes a El Cañón de Chicamocha:${totalDinChi} ")
        print(
            f"El total de dinero de los viajes a Los Llanos Orientales:${totalDinLla} ")
        Adultos = AdultosGua + AdultosChi + AdultosLla
        print(f"Total de personas adultas:{Adultos} ")
        Niños = NiñosGua + NiñosChi + NiñosLla
        print(f"Total de Niños:{Niños} ")
        totalDinDesti = totalDinGua + totalDinChi + totalDinLla
        print(f"Total de dinero de todos los destinos:${totalDinDesti} ")
        print("")
        print("*****PROCESO TERMINADO***")
        break
