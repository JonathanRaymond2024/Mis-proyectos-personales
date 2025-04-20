

print("### TIENDA DE MANZANAS ###")

nombre_completo = input("Ingrese su nombre y apellido por favor: ")
print("Bienvenido", nombre_completo, "!!!!!!!!")

print("Tienes un total de 20 manzanas disponibles, cada una por el precio de $5 peso.")

manzanas = 20
pregunta_manz = input("Cuantas manzanas quiere: ")
pregunta_manz = int(pregunta_manz)
precio_manzana = 5

suma = pregunta_manz * precio_manzana
print("Usted compro: " + str(pregunta_manz) + " manzanas", " y valio un total de $" + str(suma) +" pesos")

resta = manzanas - pregunta_manz

print("Le quedaron: "+ str(resta) + " manzanas en la tienda")



