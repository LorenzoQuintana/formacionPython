#Devuelva los dos primeros caracteres.
def first_two_chars(string):
    return string[:2]

#Devuelva los tres últimos caracteres
def last_three_chars(string):
    return string[-3:]

#Devuelva la cadena cada dos caracteres.
def every_two_chars(string):
    return string[::2]

#Devuelva la cadena en sentido inverso.
def reverse_string(string):
    return string[::-1]


input_string = "Esto, esto, esto. aquello: allí, aquello!"

print("First two characters:", first_two_chars(input_string))
print("Last three characters:", last_three_chars(input_string))
print("Every two characters:", every_two_chars(input_string))
print("Reversed string:", reverse_string(input_string))