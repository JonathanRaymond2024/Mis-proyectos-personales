


print("Escribe tu nombre: ")
nombre = input()
print("Escribe tu edad: ")
edad = int(input())

#elif
#Operadores logicos
#and (y): todas las condiciones deben ser verdaderas para que se ejecute el bloque de codigo
#or (o): al menos una condicion debe ser verdadera para que se ejecute el bloque de codigo
# > <   <= >=

if nombre == "Joe" and edad >= 21:
    print("Bienvenido Joe, eres un adulto")
elif nombre == "Joe" and edad < 21:
    print("Bienvenido Joe, eres un joven")    
else:
    print("Saludos")


nombre2 = input("Escribe tu nombre: ")

if nombre2 == "Joe" or nombre2 == "Jonathan":
    print("Me gusta tu nombre")
else:
    print("Que nombre tan raro")

