### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [32, 5, 21, 22, 23, 50, 50]
print(my_list.count(50))  # cuenta la cantidad de veces se repite un elemento

print(my_list)
print(len(my_list))

my_other_list = [35, 1.17, "Ivan", "Casavieja"]
print(my_other_list)
print(type(my_other_list))
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list[3])

# desestructuramos una lista en variables
age, height, name, surname = my_other_list
age, height, name, surname = (
    my_other_list[0],
    my_other_list[1],
    my_other_list[2],
    my_other_list[3],
)  # se puede desestructurar tambien de esta forma y cambiarincluso los ordenes
print(age)

# se pueden sumar listas
print(my_list + my_other_list)

my_other_list.append("KilometroCero")
print(my_other_list)

my_other_list.insert(1, ":(")  # insertar un indice entre medio
print(my_other_list)

my_other_list[1] = ":)"
print(my_other_list)

my_other_list.remove(":)")  # elimina un elemento que se que existe
print(my_other_list)

my_list.remove(50)  # solo remueve el primer elemento no todos
print(my_list)

my_list.pop()
print(my_list)
print(my_list.pop())
print(my_list.pop(2))

my_pop_element = my_list.pop(
    2
)  # forma de eliminar un elemento en concreto y alojarlo en una variable
print(my_pop_element)
print(my_list)

del my_list[1]  # forma de eliminarlo y nada mas
print(my_list)

my_new_list = my_list.copy()

my_list.clear()  # elimina todo
print(my_list)
print(my_new_list)

my_new_list.append(50)
my_new_list.append(1)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_short_list_new = my_new_list[1:3]
print(my_short_list_new)