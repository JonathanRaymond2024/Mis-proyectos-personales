#Ciclos, interacion o bucle



#while
"""
i = 0
while i < 5:
    print("Hola Python")
    i += 1


numero = 0
while numero < 10:
   
    if numero < 5:
        
        print("Tu numero", numero," es menor a 5")
    else:
        print("Tu numero", numero, " es mayor a 5")

    numero = numero + 1

print("Termino el bublce")

"""
"""
for x in range(1, 11):
    print(x)

"""

while True:
    print("Escribe la opcion deseada")
    print("1: Saludar")
    print("2: Salir")

    respuesta = int(input())

    if respuesta == 1:
        print("Saludos terrícola!")
    elif respuesta == 2:
        break

print("Terminando programa")


