"""PRACTICE SET 2 ANSWERS"""

''' Q1> Code for addition'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The first number is: ",a)
print("The second number is: ",b)
print("Addition of the given numbers a + b =",a + b)
  
'''Q2> Code for division'''
a = int(input("Enter any numerator value: "))
z = int(input("Enter the denominator value: "))
div = a/z
print("The divison according to the values is: ",float(div))

'''Q3> Print the remainder'''
a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))
z = a % b
print("The remainder of the given numbers is: ",z)

'''Q4> Check the data type where the user gives input'''
a = input("Enter any variation of number: ")
ty = type(a)
print(ty)

'''Q5> Using comparison operator to compare the values of two different variables'''
a = int(input("Enter the first number which is to checked "))
b = int(input("Enter the second number which is to checked "))
print("Checking if a >b or not.....")
print(a>b)

'''Q6> Find the average two numbers given by the user'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
avg = (a+b)/2
print("The average of the given two numbers are: ",avg)

'''Q7> Print the square of a number given by the user'''
a = int(input("Enter the number whose square you wanna see: "))
sq = a * a
print("The  square of the number is: ",sq)
