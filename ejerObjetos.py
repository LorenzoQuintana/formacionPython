from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("The denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, otherFraction):
        new_numerator = self.numerator * otherFraction.denominator + otherFraction.numerator * self.denominator
        new_denominator = self.denominator * otherFraction.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, otherFraction):
        new_numerator = self.numerator * otherFraction.numerator
        new_denominator = self.denominator * otherFraction.denominator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        return self  

fraction1 = Fraction(4, 6)
fraction2 = Fraction(1, 2)

print("Fraction 1:", fraction1)
print("Fraction 2:", fraction2)

#Addition
sum_result = fraction1.add(fraction2)
print("Sum:", sum_result)

#Multiplication
product_result = fraction1.multiply(fraction2)
print("Product:", product_result)

#Simplification
originalFraction=(fraction1.numerator, fraction1.denominator)
fraction1.simplify()
print(f"Simple form of {originalFraction[0]}/{originalFraction[1]}: {fraction1}")