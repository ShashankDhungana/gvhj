'''8. Given a three-digit number. Find the sum of its digits'''
number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)