"""PROBLEM SET 4"""

'''Q1> Write a program to store seven fruits name in a list entered by the user '''

fruits = []
f1 = input("Enter any fruits name: ")
fruits.append(f1)
f2 = input("Enter any fruits name: ")
fruits.append(f2)
f3 = input("Enter any fruits name: ")
fruits.append(f3)
f4 = input("Enter any fruits name: ")
fruits.append(f4)
f5 = input("Enter any fruits name: ")
fruits.append(f5)
f6 = input("Enter any fruits name: ")
fruits.append(f6)
f7 = input("Enter any fruits name: ")
fruits.append(f7)
print(fruits)

'''Q2> Write a program to accept marks of 6 students and display them in the sorted manner'''

marks = []
m1 = input("Enter the marks of the first student: ")
marks.append(m1)
m2 = input("Enter the marks of the second student: ")
marks.append(m2)
m3 = input("Enter the marks of the third student: ")
marks.append(m3)
m4 = input("Enter the marks of the fourth student: ")
marks.append(m4)
m5 = input("Enter the marks of the fifth student: ")
marks.append(m5)
m6 = input("Enter the marks of the sixth student: ")
marks.append(m6)

descending_marks = sorted(marks, reverse = True)
ascending_marks = sorted(marks)
print("The marks of the students in ascending order is: ",ascending_marks)
print("The marks of the student in decending order is: ",descending_marks)

'''Q3> Check that a type cannot be changed in python'''

a = (1,2,4,5,3,6,8,"BOOM")
a[7] = "KABOOM"     #The occurence of the error shows that the a tuple is immutable and it's value cannot be changed
print(type(a))

'''Q4> Write a program to sum a list with 4 numbers'''

num = []
n1 = int(input("Enter the first number of the first index of a list: "))
num.append(n1)
n2 = int(input("Enter the second number of the second index of a list: "))
num.append(n2)
n3 = int(input("Enter the thrid number of the thrid index of a list: "))
num.append(n3)
n4 = int(input("Enter the fourth number of the fourth index of a list: "))
num.append(n4)
print("The entered numbers in the list are: ",num)
print("Sum of the list is:",sum(num))
            #OR
num = [] 
for i in range(4):
    n = int(input(f"Enter number for index {i}: ")) 
    num.append(n)

print("The entered numbers in the list are:", num)
print("Sum of the list is:", sum(num))


'''Q5> Write a program to count the number of zeros in the following tuple: 
        a = (7,0,8,0,0,9)                   '''

a = (7,0,8,0,0,9)
print(a.count(0))