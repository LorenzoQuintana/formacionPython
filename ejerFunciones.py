#Función que devuelve el mayor de un grupo de números
num1= 10
num2= 280
num3= 3.45
def highestNumber(*args):
   if not args:
      return "No numbers to compare"

   highest= args[0]
   
   for num in args[1:]:
      if num> highest:
         highest = num

   return f"{highest} is the highest number"

result= highestNumber(num1, num2, num3)
print(result)

#Función que devuelve si un carácter es una vocal
def isVowel(letter):
   vowelList=["a", "e", "i", "o", "u"]
   letter = letter.lower()
   if letter in vowelList:
      return f"{letter} is a vowel"
   
vowel= isVowel("a")
print(vowel)
   
