print("#####  TIENDA   #####")
print("#####    DE   #####")
print("#####  BIZCOCHOS   #####")
print("#################################################")

nombre_completo = input("Buenos dias, ingrese su nombre completo por favor:")
print("Hola ",nombre_completo, "gracias por visitarnos.")

while True:

    print("Seleccione una opción")
    print("1. Comprar Bizcohcos")
    print("2. Ver cuantos bizcochos hay en la tienda")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        while True:
            print("¿Que quiere comprar?")
            print("1. Margaritas")
            print("2. Pan con grasa")
            print("3. Corazones dulce")
            print("0. Salir")
            
            seleccion = int(input())
            if seleccion == 1:
                margarita_compra = int(input("Cuantas margaritas quiere: "))
                print("Bien, usted compro ", margarita_compra, "margaritas")
            elif seleccion == 2:
                pan_con_grasa_compra = int(input("Cuantos pan con grasa quiere: "))
                print("Bien, usted compro ", pan_con_grasa_compra, "pan con grasa")
            elif seleccion == 3:
                corazon_dulce_compra = int(input("Cuantos corazones dulce quiere: "))
                print("Bien, usted compro ", corazon_dulce_compra, "corazones dulce")
            elif seleccion == 0:
                print("Volviendo a la pantalla principal")
                break
            else:
                print("Opcion incorrecta, vuleva a intentarlo")
                
    elif opcion == 2:

        margarita = 100
        pan_con_grasa = 80
        corazon_dulce = 90

        total_bizcochos = margarita + pan_con_grasa + corazon_dulce

        print("En la tienda hay:", margarita, "margaritas,", pan_con_grasa,"pan con grasa y", corazon_dulce, "corazones dulces")
        print("En total hay:", total_bizcochos, "bizcochos")

    elif opcion == 0:
        print("Saliendo de la tienda, vuelva pronto.")
        break

    else:
        print("Opcion incorrecta, vuleva a intentarlo")

