#Implementar un generador que devuelva los números pares
def evenNumbers(limit=None):
    num = 0
    while limit is None or num <= limit:  
        yield num
        num += 2

print("First 10 even numbers:")
for even in evenNumbers(25): 
    print(even)

#Implementar un generador que reciba un número y devuelva los múltiplos de 3 de ese número
def multiplesOfThree(num, limit=None):
    current = num
    while limit is None or current <= limit:  
        if current % 3 == 0:  
            yield current
        current += num  

print("Multiples of 3, up to 70:")
for multiple in multiplesOfThree(5, 70):  
    print(multiple)