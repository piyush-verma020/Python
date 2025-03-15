"""PRACTICE SET 8"""

'''Q1> Write a program using functions to find the greatest of three numbers.'''

def greatest(a, b, c):
    if(a>b and a>c):
        return (f"{a} is the greatest number of all three.")
    elif(b>a and b>c):
        return (f"{b} is the greatest number of all three")
    elif(c>a and c>b):
        return (f"{c} is the greatest number of all three")
    else:
        return 0          #this line is optional to be honest we don't need this line

x = int(input("Enter the value of the first variable: "))
y = int(input("Enter the value of the second variable: "))
z = int(input("Enter the value of the third variable: "))
print(greatest(x, y, z))          #i am just supplying the values of x, y, z inside the function as a, b, c respectively

'''Q2> Write a python program to convert Celcious to fahrenheit.'''

def celcious_to_fahrenheit(cel):
    return ((cel / 5) * 9 ) + 32          #this is the basic formula of convertion

celcious = float(input("Enter the tempurature in celcious: "))
fahrenheit = celcious_to_fahrenheit(celcious)
print(f"The temperature given in {celcious}°C after convertion is: {fahrenheit}°F")

'''Q3> How do you prevent python print() function to print a new line at the end.'''


print("Hello World",end = "")               #The end ="" argument prevents print function to print a new line at the very end 
print("! Good Morning Everyone",end ="")

'''Q4> Write a recursive funtion to print the sum of first n natural numbers.'''

def sum(n):
    if(n == 0):
        return 0
    else:
        return n + sum(n-1)
    
n = int(input("Enter the value of n: "))
print(f"The sum of the first {n} natural numbers is: {sum(n)}")

'''Q5> Write a python function to print first n lines of the following pattern:
    * * *
    * *
    *           for n = 3'''

def pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

n = int(input("Enter the number of rows you need for the patterns: "))
print(pattern(n))

# OR

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

n = int(input("Enter the number of rows you need for the pattern: "))
pattern(n)

'''Q6> Write a python program to convert inches to centimeters.'''

def inc_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter the length in inches: "))
print(f"The convertion of {inch} inch into centimeters is: {inc_to_cm(inch)} cm")

'''Q7> Write a python function to remove a given word from the list and strip at the same time.'''

def remove(l, word):
    n = []
    for item in l:
        if(item != word):
            n.append(item.strip(word))
    return n
l = ["Python", "Ruby", "C", "C++","Java", "y"]
word = input("Enter the word which you wish to remove from the list: ")
print(remove(l, word))

'''Q8> Write a python function to print the multiplication table of a given number.'''

def multiplication(n):
    for i in range(11):
        print(f"{n}  *  {i}  =  {n * i}")

n = int(input("Enter the number whose multiplication table you wish to see: "))
multiplication(n)