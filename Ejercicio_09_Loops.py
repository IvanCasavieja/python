### Loops

# While

my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("hola pepito")
        break
else:
    print("mi condicion es mayor o igual a diez")

my_list = [35, 24, 62, 52, 30, 30, 17]

# for

for element in my_list:
    print(element)

my_tuple = (35, 24, 62, 52, 30, 30, 17)
my_set = {35, 24, 62, 52, 30, 30, 17}
my_dict = {
    "edad": 35,
    "Años": 24,
    "age": 62,
}
for element in my_tuple:
    print(element)
print("-")
for element in my_set:
    print(element)
print("-")
for element in my_dict:
    # devuelve solo las keys, pero podemos poner my_dict.values() para traer los valores
    print(element)
    if element == "edad":
        print("se para en edad")
        continue  # se puede detener y el else no se emite
    elif element =="Años":
        print("Años ivan")
        break
else:
    print("el bucle for a finalizado")
