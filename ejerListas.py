#Función que suma los valores de una lista
def listTotal(list):
    total=0
    for num in list:
        total=total+num
    
    return total

list= [1, 2, 3]
print(listTotal(list))

#Función que devuelve una lista inversa a la que recibe
def reverseList(list):
    newList=list[::-1]
    
    return newList

print(reverseList(list))