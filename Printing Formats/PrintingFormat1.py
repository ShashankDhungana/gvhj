name = input("enter your name:")
age = int(input("enter age:"))
print("hello my name is " + name +" and i am " + str(age) + " years old")
print("hello my name is", name, "and i am", age, "years old")
print("hello my name is %s nad i am %d years old" % (name, age))
print("hello my name is {} nad i am {} years old" .format(name, age))
print(f"hello my name is {name} and i am {age} years old")