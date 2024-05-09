my_dict = dict()
my_other_dict = {}
print(type(my_dict), type(my_other_dict))

my_other_dict = {"nombre": "Ivan", "Apellido": "Casavieja", "Edad": 35, 1: "Python"}
print(type(my_other_dict))
print(my_other_dict)

my_dict = {
    "Nombre": "Ivan",
    "Apellido": "Casavieja",
    "Edad": 35,
    "Lenguages": {"Python", "Swift", "Kotlin"},
    1: 1.78,
}
print(my_dict)
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict)

my_dict["Nombre"] = {"Pedro", "Ivan"}
print(my_dict)

my_dict["Calle"] = "El iniciador"
print(my_dict)

# my_dict.clear() Funciona, pero lo comento para tener el diccionario con datos
# print(my_dict)

del my_dict["Calle"]  # elimina un solo elemento
print(my_dict)

print("Nombre" in my_dict)
print("Ivan" in my_dict["Nombre"])

print(my_dict.items())  # retorna todo
print(my_dict.keys())  # retorna las llaves
print(my_dict.values())  # retorna los valores de las llaves

# crea un nuevo diccionario en base a las keys de uno ya creado, pero sin valores
my_new_dict = my_other_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict_2 = dict.fromkeys(my_list)
print(my_new_dict_2)

my_other_dict_3 = dict.fromkeys(my_dict)
print(my_other_dict_3)

my_other_dict_4 = dict.fromkeys(my_dict, ("Ivan", "Casavieja"))
print(my_other_dict_4)
# tiene sentido de esta forma, ya que nos imprime el valor que le demos en parentesis a todas las keys
my_other_dict_5 = dict.fromkeys(my_dict, ("Ivan"))
print(my_other_dict_5)

my_values = my_other_dict.values()
print(type(my_values))
print(list(my_other_dict.values()))

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
