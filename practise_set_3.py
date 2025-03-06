"""PRACTICE SET 3"""

'''Q1> Write a program to display a user entered name followed by Good Afternoon using input() function'''
name = input("Enter your name: ")
print(f"Good Afternoon, {name}")

"""Q2> Write a program to fill in a letter template given below along with the name date 
        # Dear <|Name|>,
        # You are selected!
        # <|Date|>
        # '''     
        """
name = input("Enter you name: ")
date = input("Enter todays date dd mm yy: ")
print(f"Dear {name},\nYou are selected!\n{date} \n''' ")
                # OR
name = input("Enter your name: ")
date = input("Enter today's date: ")
letter = """Dear <|Name|>,
You are selected!
<|Date|>"""
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))

'''Q3> Write a program to detect double space in a string'''
string = input("Enter a string: ")
print(("No double space found.", "Double space detected!")[ "  " in string ])
            #OR
string = input("Enter any string to check for double spaces: ")
print(f"Doubles spaces are found in this {string.find("  ")} index number")         #if the output shows -1 then there is no double space found

'''Q4> Replace the double space from problem 3 with single spaces'''
string = input("Enter a string which also includes double spaces: ")
print(string.replace("  "," "))         #in this line of code it's replacing extra spaces with a single space
print(string.strip())                   #strip is not valid cause it cannot detect extra spaces between the strings but strip can remove extra spaces in the front of the string and in the back of the string

'''Q5> Write a program to format the following letter using escape sequence characters.
        Letter = "Dear NAME, this python program is nice. Thanks!"'''

name = input("Enter your name: ")
print("Dear ", name, "\b,\n\tThis python program is nice. Thanks!")  #You can use this or you can just use the f string same as in the previous question 