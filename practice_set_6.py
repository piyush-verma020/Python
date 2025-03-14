"""PRACTICE SET 6"""

'''Q1> Write a program to find the greatest numbers entered by the user.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the forth number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"{num1} is the greatest number")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f"{num2} is the greatest number")
elif(num3>num2 and num3>num1 and num3>num4):
    print(f"{num3} is the greatest number")
elif(num4>num2 and num4>num3 and num1<num4):
    print(f"{num4} is the greatest number")
print("End pf program")

'''Q2> Write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each aiject to pass. Assume 3 aijects and take marks as an input from the user.'''

maths = int(input("Enter the marks of Maths: "))
science = int(input("Enter the marks of Science: "))
ai = int(input("Enter the marks of Artificial Intelligence: "))
total_percentage = (100*(maths + science + ai)/300)

if(total_percentage >= 40 and total_percentage <= 100 and maths >= 33 and science >= 33and ai >= 33):
    print("Congratulations!")
    print(f"You have passed the exam with {total_percentage}")
else:
    print(f"You have failed the exam with {total_percentage}.\nBetter luk next time")

'''Q3> A spam comment is defined as a text contining following keywords:
       "Make a lot of money", "Buy now", "aiscribe this", "Click this". Write a programs to detect these spams.'''

spam_in_check = input("Enter a spam_in_check which might be a spam: ")
if(spam_in_check == " Make a lot of money" or spam_in_check == "Buy now" or spam_in_check == "aiscribe this" or spam_in_check == "Click this"):
    print(f"The given spam_in_check: \"{spam_in_check}\" is a spam comment")
else:
    print(f"The given spam_in_check: \"{spam_in_check}\" is not a spam")

'''Q4> Write a program to find whether a given username contains lesser than 10 characters or not.'''

username = input("Enter your name user: ")
if(len(username) < 10):
    print("The username is contains lesser than 10 characters")
elif(len(username) >= 10):
    print("The characters in a username is greater than or equals to 10")
else:
    print("Please enter something valid")

'''Q5> Write a program which finds out whether a given name is present in a list or not.'''

list = []
list.append("Peter")
name = input("Enter the name you wanna search for in the list: ")
if(name in list):
    print("The name is already present in the list")
else:
    print("The entered name is not present in the list")
    print("Do you wish to add it to the list")
    n = input("Then press 1: ")
    list.append(name)         #or you could also use list.insert(name)
    print(f"The lisrt after the insertion is: {list}")
print("END OF PROGRAM")

'''Q6> Write a program to calculate the grade of a student form his marks from the following scheme:
       90 - 100 -> O
       80 - 90 -> A
       70 - 80 -> B
       60 - 70 -> C
       50 - 60 -> D
       < 50 -> F        '''

name = input("Enter your name: ")
grade = int(input("Enter your grade: "))
if(grade <= 100 and grade >=90):
    print("That's an outstanding performance\nkeep it up")
elif(grade <= 90 and grade >=80):
    print("You got  A rating\nkeep it up")
elif(grade <= 80 and grade >= 70):
    print("Yor got B rating\nkeep it up")
elif(grade <= 70 and grade >= 60):
    print("You got C rating\nMaybe you should try for a B")
elif(grade <=60 and grade >= 50):
    print("You got D rating\nwork harder")
elif(grade < 50 and grade >= 0):
    print("I am sorry to say but you have failed the exam\nbetter luck next time")
else:
    print(f"Please enter a valid grade marks!Mr.{name}")

'''Q7> Write a program to find out whether a given post is talking about "python" or not.'''

post = input("Enter the post: ")

if("Python".lower() in post.lower()):
    print("Yes the post is talking about python")
else:
    print("The post is not talking about pyhton")
