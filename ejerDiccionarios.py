#Función que reciba una lista de tuplas y devuelva un diccionario donde las claves son los primeros elementos de las tuplas y los valores una lista con los segundos elementos
def tupleToDict(tupleList):
    resultDict = {} 
    
    for key, value in tupleList:
        if key not in resultDict:
            resultDict[key] = []  
        resultDict[key].append(value) 
    
    return resultDict

tupleList = [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5), ("F", 6)]
result = tupleToDict(tupleList)
print(result)

#Función que reciba una cadena y devuelva un diccionario con la cantidad de repeticiones de cada palabra en la cadena
def wordCount(string):
    words = string.split()  
    wordDict = {}  
    
    for word in words:
        word = word.lower()  
        if word not in wordDict:
            wordDict[word] = 1  
        else:
            wordDict[word] += 1  
    
    return wordDict

inputString = "Esto esto esto aquello allí aquello"
result = wordCount(inputString)
print(result)