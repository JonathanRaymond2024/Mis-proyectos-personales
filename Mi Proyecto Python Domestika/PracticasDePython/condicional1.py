
edad = int(input("Ingrese su edad: "))

if edad >= 21:
    print("Usted tiene", edad, ", es mayor de edad y adulto")

elif edad >= 18:
    print("Usted tiene", edad, ", es mayor de edad")

elif edad < 18:
    print("Usted tiene", edad, ", es menor de edad")

else:
    print("Dato incorrecto")