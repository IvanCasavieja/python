my_variable_string = "Mi string variable"
print(my_variable_string)

my_variable_int = 2
print(my_variable_int)

my_variable_bool = True
print(my_variable_bool)

my_variable_int_str = str(my_variable_int)
print(type(my_variable_int_str))


print(my_variable_string, my_variable_int_str, my_variable_bool)
print(len(my_variable_string))
print("Este es el valor de:", my_variable_bool)

# variables en una sola linea
name, lastname, alias, age = "Ivan", "Casavieja", "ivi", 24
print("Me llamo:", name, lastname, ",", "Mi edad es:", age, ". Mi alias es:", alias)


# input
""" first_name = input("What is your name?")
age_input = input("How old are you?")

print(first_name, age_input) """


# forzamos el tipo? no
address: str = "El iniciador"
address = 32
print(address)
