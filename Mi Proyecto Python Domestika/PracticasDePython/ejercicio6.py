nombre = input("Ingrese su nombre por favor: ")
sexo = input("Ingrese su sexo por favor. Masculino (M) o Femenino (F): ")

if (sexo == "F" and nombre.lower() < 'm') or (sexo == "M" and nombre.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)

