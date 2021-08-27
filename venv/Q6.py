'''
6. Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments.
When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.
'''
height = float(input("enter height in cm"))
weight = float(input("enter wieight in kgr"))
BMI = weight / (height*100)**2
print(f"The Body mass index of a person is: {BMI}")

