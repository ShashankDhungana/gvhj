'''7. Given a positive real number, print its fractional part.'''
import math
num = float(input("Enter any positive real numbers : "))
fractional = math.modf(num)
print(f"Fractional part is {fractional}")