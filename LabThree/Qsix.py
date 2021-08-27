def reverse_string(str):
    strR = ""
    for i in str:
        strR = i + strR
    return strR
str = "Shashank"
print("The string is:", str)
print("The reversed string is",reverse_string(str))
