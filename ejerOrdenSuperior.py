#Función lambda que devuelva el área de un triángulo
triangleArea = lambda b, h: (b * h) / 2


#Función, utilizando map, que reciba una lista de números y devuelva la lista con todos sus elementos multiplicados por 5.
numbersList = [13, 7, -6, 2, 1]
multiplyBy5 = lambda x: x * 5
resultList = list(map(multiplyBy5, numbersList))


#Función con filter para obtener múltiplos de 3
isMultipleOf3 = lambda x: x % 3 == 0
multiplesOf3 = list(filter(isMultipleOf3, numbersList))




print(f"Area of the triangle: {triangleArea(3, 7)}")  
print(f"List multiplied by 5: {resultList}")
print(f"Multiples of 3: {multiplesOf3}")