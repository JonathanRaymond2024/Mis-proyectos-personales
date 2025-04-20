"""CONVERSOR DE IMC """

print("Calculadora de IMC (Indice de Masa Corporal)")

peso = input("Ingrese su peso en kilogrmos: ")
altura = input("Ingrese su altura en metros: ")

peso = int(peso)
altura = float(altura)
imc = peso / (altura ** 2)

print(f"Su indice de masa corporal es: {imc:.2f}")

#print("Su indice de masa corporal es: ", imc)
