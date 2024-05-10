"""Condicionales"""

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 1 * 1

if my_condition > 10:
    print("Es mayor que diez")
else:
    print("Es menor o igual")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que diez y menor que veinte")
else:
    print("Es menor o igual")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que diez y menor que veinte")
elif my_condition == 1:
    print("Es igual a uno")
else:
    print("Es menor o igual")

print("La ejecucion continua")


my_string = "mi cadena de texto"

if my_string:
    print("mi cadena de texto no es vacia")

my_string = ""

if not my_string:
    print("mi cadena de texto no es vacia")
