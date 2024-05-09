# stringa

my_string = "Mi cadena"
my_other_string = "Mi otra cadena"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linea"
print(my_new_line_string)
my_new_line_string_tab = "\tEste es un string con tab"
print(my_new_line_string_tab)
my_scape_string = "\tEste es un string \nescapado"
print(my_scape_string)

# formateo simplificado de codigo

name, surname, age = "Ivan", "Casavieja", 24

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

language_slice_ascendente = language[1:]
language_slice_limite = language[1:3]
language_slice_descendente = language[:3]
language_slice_desde_atras = language[-2]
print(
    language_slice_ascendente,
    language_slice_limite,
    language_slice_descendente,
    language_slice_desde_atras,
)

# reverse

reversed_language = language[::-1]
print(reversed_language)

#metodos y funciones

print(len(language))
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))