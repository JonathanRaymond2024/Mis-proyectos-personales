#Funciones vistas en el curso
#Pre-definidas, print(), type(), range(), input()


# def es para crear y definir funciones.
#pass sirve para dejar una funcion funcionando sin ningun tipo de dato, ayuda para evitar errores de codigo de otras lineas.
def saludar(nombre):
    print("Hola", nombre)

#Celsius a Fahrenheit: (C * 1.8) + 32
def convertir_a_fahrenheit(c):
    #regrese un valor
    return (c * 1.8) + 32


#saludar("Joe")
#saludar("Matias")
#saludar("Lucia")
#saludar("Sofia")

print(convertir_a_fahrenheit(10) )
print(convertir_a_fahrenheit(25) )
print(convertir_a_fahrenheit(50) )

