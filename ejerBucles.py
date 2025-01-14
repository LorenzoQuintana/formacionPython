#Implementar una función que reciba un numero y devuelva su descomposición en números primos
def primes(number):
    factors = [] 
    divisor = 2  
    
    while number > 1:
        while number % divisor == 0:  
            factors.append(divisor)  
            number //= divisor  
        divisor += 1  
        if divisor * divisor > number:  
            if number > 1:  
                factors.append(number)
                break
    
    return factors

#Implementar una función que reciba dos números y devuelva el máximo común divisor
number = 320
result = primes(number)
print(f"Primes of {number}: {result}")

def greatestCommonDivisor(a, b):
    while b != 0:
        a, b = b, a % b  
    return a

num1 = 56
num2 = 98
result = greatestCommonDivisor(num1, num2)
print(f"GCD of {num1} and {num2}: {result}")