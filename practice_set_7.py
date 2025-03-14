"""PRACTICE SET 7"""

'''Q1> Write a program to print multiplication table of a given number using for loop'''

number = int(input("Enter the number whose multiplication table you wanna see: "))
for i in range(0,10+1):
    print(f"{number} * {i} = {i * number}")
print("End of the program")

'''Q2> Write a program to greet all the persons name given in the list "l" and which starts with S.
       l = ["Hary", "Soham", "Sachin", "Rahul"]'''

l = ["Hary", "Soham", "Sachin", "Rahul"]
for i in l:
    if(i.startswith("S")):
        print(f"Good morning: {i}")

'''Q3> Attempt problem 1 using while loop.'''

number = int(input("Enter the number whose multiplication table you wanna see: "))
i = 0
while(i<=10):
    print(f"{number} * {i} = {i * number}")
    i += 1
print("End of the program")

'''Q4> Write a program to find whether the given number is prime number or not.'''

number = int(input("Enter a number: "))
if(number < 2):
    print(f"{number} is not a prime number")
else:    
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):        # number ** 0.5 calculates the square root of number and int(number ** 0.5) ensures we only take the integer part.
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


'''Q5> Write a program to find the sum of first n natural numbers using while loop.'''

n = int(input("Enter the value of n: "))
sum = 0
i = 1
while(i <= n):
    sum += i
    i+=1
print(f"The sum of the first {n} natural numbers is: {sum}")

'''Q6> Write a program to print the factorial of a given number using for loop.'''

number = int(input("Enter the number whose factorial you want: "))
fact = 1
for i in range(1,number+1):
    fact = fact * i
print(f"The factorial of the given number = {number} is: {fact}")


'''Q7> Write a program to print the following star pattern. 
      *
     ***
    *****     for n = 3'''

n = int(input("Enter the number of lines you want to see in the pattern: "))
for i in range(0,n+1):
    print(" "* (n-i),end = "")
    print("*"* (2*i-1),end = "")
    print("")

'''Q8> Write a program to print the following star pattern.
       *
       **
       ***      for n = 3'''

n = int(input("Enter the number of lines you want to see in the pattern: "))
for i in range(n+1):
    print("*"* i)

'''Q9> Write a program to print the following star pattern.
       * * *
       *   *
       * * *    for n = 3'''

n = int(input("Enter the number of lines you wish to see in the pattern: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("*" + " " * (2*n-3) + "*")

'''Q10> Write a program to print the multiplication of n using for loops but in reversed order.'''

number = int(input("Enter the number whose multiplication table you wish to see: "))

#using while loop
i=10
while(i>=0):
    print(f"{number} * {i} = {number * i}")
    i -= 1
print("End of program")

#using for loop
for i in range(10,0-1,-1):
    print(f"{number} * {i} = {number * i}")
print("End of the program")

#Another method
for i in range(1,11):
    print(f"{number} * {11-i} = {number *(11-i)}")
print("End of program")
