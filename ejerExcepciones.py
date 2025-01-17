#Implementar una función que reciba una lista y un elemento y devuelva una lista con el elemento añadido al final de la lista. 
#Si el elemento ya existe en la lista se generará un error de tipo ValueError y se mostrará un mensaje descriptivo
def addElementToList(list, element):
    if element in list:
        raise ValueError(f"{element} already exists in the list.")
    list.append(element)
    return list

try:
    list = [1, 2, 3, 4, 5]
    print(addElementToList(list, 7))  
    print(addElementToList(list, 2))  
except ValueError as e:
    print(e)

#Implementar una función que reciba un diccionario y una clave y devuelva el valor contenido en el diccionario de esa clave.
#Si la clave no está se generará un error de tipo ValueError y se mostrará un mensaje descriptivo
def getValueFromDict(dictionary, key):
    if key not in dictionary:
        raise ValueError(f"The key '{key}' does not exist in the dictionary.")
    return dictionary[key]

try:
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print(getValueFromDict(my_dict, 'b'))  
    print(getValueFromDict(my_dict, 'x'))  
except ValueError as e:
    print(e)