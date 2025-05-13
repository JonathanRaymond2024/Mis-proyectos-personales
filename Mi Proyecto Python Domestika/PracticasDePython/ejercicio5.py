edad = int(input("Ingrese su edad por favor: "))
ingresos_usuario = int(input("Ingrese sus ingresos mensuales por favor. En euros: "))

if edad >= 16 and ingresos_usuario >= 1000:
    print("Usted tiene", edad ,"y cobra", ingresos_usuario, "euros mensuales")
    print("Usted tiene que tributar")

elif edad >= 16 and ingresos_usuario < 1000:
    print("Usted tiene", edad ,"y cobra", ingresos_usuario, "euros mensuales.")
    print("Usted no puede tributar porque sus ingresos son "+str(ingresos_usuario)+".")
    print("Para tributar debe ganar al menos 1000 euros.")

elif edad < 16:
    print("Usted es menor de edad, no puede tributar.")
else:
    print("Error, no se puedo procesar la informacion adquirida.")
    print("Intentelo de nuevo.")



