print("***********************************")
print("***  BIENVENIDO A   ***")
print("***  LA TIENDA DE MASCOTAS   ***")
print("***********************************")

nombre = input("Ingrese su nombre por favor:")
apellido = input("Ingrese su apellido por favor: ")

print("Hola", nombre, apellido, " gracias por visitarnos!!!!!")

print("Selecciona la opcion que desea: ")
print("1. Conocer cuantos animales hay en la tienda")
print("2. Comprar un animal")
print("0. Salir")

#Almacena la respuesta del usuario
respuesta = int(input())

num_perros = 14
num_gatos = 10
num_pajaros = 28

#Opcion 1: Conocer la cantidad de animales en la tienda
if respuesta == 1:
    print("En la tienda hay:", num_perros, "perros,", num_gatos, "gatos y", num_pajaros, "pajaros.")

    cant_animales = num_perros + num_gatos + num_pajaros
    print("En total hay: ", cant_animales, "animales")
#Opcion 2: Comprar un animal
elif respuesta == 2:
    print("Que animal desea comprar?")
    print("1. Perro")
    print("2. Gato")
    print("3. Pajaro")

    elecion = int(input())

    if elecion == 1:
        print("Bien, usted esta comprando un perro")
        print("El precio es de $500")
    elif elecion == 2:
        print("Bien, usted esta comprando un gato")
        print("El precio es de $300")
    elif elecion == 3:
        print("Bien, usted esta comprando un pajaro")
        print("El precio es de $100")
    else:
        print("No tenemos ese animal en la tienda")

elif respuesta == 0:
    print("Gracias por visitarnos, vuelva pronto")

else:
    print("Opcion incorrecta, por favor seleccione una de las opciones")

