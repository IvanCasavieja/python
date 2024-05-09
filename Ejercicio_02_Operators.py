# operadores aritmeticos

print(3 + 5)
print(3 / 5)
print(3 * 6)
print(4 - 5)
print(10 // 5)  # da la aproximacion de un entero del resultado de la division
print(10 % 5)
print(2**3)

print("Hola" + "Python")
print("Hola" + " " + "Python")
print("Hola " + "5 " + str(5))
print("Hola " * 5)
print("Hola " * (2**3))

""" impresion por float """
""" si quiero imprimir tantas veces una palabra, debe ser por un tipo int, no lo hara en tipo float """

# print("hola " * 2.5) esto dara error
# print("hola " * (2.5*2)) tambien da error, ya que el resultado es tipo float. La multiplicacion es 2.5 * 2.0
""" Entonces lo correco seria:  """

my_variable_apoyo = 2.5 * 2
print("hola " * int(my_variable_apoyo))


# Operadores comparativos:

print(3 > 4)
print(3 < 4)
print(4 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 < 4 > 1)
print(3 < 4 == 3)
print(3 < 4 == 4)


# Es por ordenacion alfabetica por ascii
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# Operadores logicos

print(3 > 4 and "hola" > "python")
print(3 > 4 or "hola" > "python")
print(3 < 4 and "hola" < "python")
print(3 < 4 or "hola" > "python")
print(not (3 < 4))  # da el contrario
