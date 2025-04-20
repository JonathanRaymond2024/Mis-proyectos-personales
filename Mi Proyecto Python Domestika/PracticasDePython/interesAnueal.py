###
"""
inversion = int(input("¿Cuánto dinero quieres invertir? "))
interes = float(input("¿Qué porcentaje de interés anual tiene tu banco? "))
anos = int(input("¿Cuántos años quieres invertir tu dinero? "))

"""


cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
