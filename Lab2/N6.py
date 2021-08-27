'''6. Given an integer number, print its last digit.'''
number = int(input("Please Enter any Number: "))
last_digit = number % 10
print("The Last Digit in a Given Number %d = %d" %(number, last_digit))