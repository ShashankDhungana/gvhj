'''
5. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students
in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has
21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students
. So, we need 32 desks in total.
'''
a = int(input("Enter the number of student in first class : "))
b = int(input("Enter the number of students in second class : "))
c= int(input("Enter the number of students in third class : "))
firstgroup = a//2
secondgroup = b//2
thirdgroup = c//2
remain_firstgroup = a%2
remain_secondgroup = b%2
remain_thirdgroup = c%2
totaldesk = firstgroup+secondgroup+thirdgroup+remain_firstgroup+remain_secondgroup+remain_thirdgroup
print(f"number of desk needed for class a:{firstgroup}")
print(f"number of desk needed for class b:{secondgroup}")
print(f"number of desk needed for class c:{thirdgroup}")
print(f"remaining desk for class a:{remain_firstgroup}")
print(f"remaining desk for class b:{remain_secondgroup}")
print(f"remaining desk for class c:{remain_thirdgroup}")
print(f"total number of desk needed:{totaldesk}")
