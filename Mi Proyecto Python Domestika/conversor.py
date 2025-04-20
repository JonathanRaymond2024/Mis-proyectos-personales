# CONVERSOR

print("Bienvenido al conversor de millas a kilometros")

print("Escribe un numero en millas: ")
millas = input()

print(type(millas))
millas = float(millas)
print("Millas ingresadas:", millas)
print(type(millas))


# 1 milla = 1.609 kms

kilometros = millas * 1.609

print("Kilometros: ", kilometros)
