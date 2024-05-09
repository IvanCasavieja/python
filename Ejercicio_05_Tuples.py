# Las tuplas son valores constantes, no se pueden cambiar

my_tuple = tuple()
my_other_tuple = (31, 35, 31)

my_tuple = (24, 1.78, "Ivan", "Casavieja")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
""" print(my_tuple[4])   #no existe
print(my_tuple[-6]) """  # no existen

print(my_tuple.count("Casavieja"))  # me da la cantidad de veces que tenga ese valor
print(my_tuple.index("Casavieja"))  # posicion del valor


# si pueden sumarse
my_plus_tuple = (
    my_tuple + my_other_tuple
)  # si la tupla a sumar,  tiene solo un elemento, debo agregarle coma para que se sume.
print(my_plus_tuple)

print(my_plus_tuple[3:6])

# se puede reasignar la tupla a una lista

my_tuple = list(my_tuple)
print(type(my_tuple))
my_tuple[3] = "hola"
print(my_tuple)
my_tuple.insert(1, "azul")

# y de tupla a lista
print(tuple(my_tuple))
my_tuple = tuple(my_tuple)
print(type(my_tuple))

""" Elimina la tupla
del my_tuple
print(my_tuple) """