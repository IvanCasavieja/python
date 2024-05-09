# sets
# es una estructura desordenada y no admite repetidos

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # inicialmente es un diccionario

my_other_set = {"ivan", "casavieja", 24, 1.78}
print(type(my_other_set))

my_other_set.add("Ivcas")
print(my_other_set)

print("Ivcas" in my_other_set)
print("Robertito" in my_other_set)

my_other_set.remove("Ivcas")
print(my_other_set)

nombre = "Ivancito"
my_other_set.add(nombre)
print(my_other_set)

my_other_set.clear()  # borra todo el set
print(len(my_other_set))

my_set = {"ivan", "casavieja", 24, 1.78}
my_list = list(my_set)
print(my_list)
# cada vez que ejecuto de un set a una lista es arriesgado, ya que cada vez que utilizo el programa el set cambia de posicion

my_other_set = {"python", "javaScript", "sql"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))
