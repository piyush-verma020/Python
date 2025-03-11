#PRACTICE SET 5

'''Q1> Write a program to create a dictionary of Hindi words with values of their English translation. Provide user with an option to look it up.'''

dict = {"Namaste" : "Hello", "Sab Bariya" : "Everything good", "Kayesse ho!" : "How are you!", "Darna" : "Afraid", "Maa" : "Mother", "Baap" : "Papa"}
print(dict.keys())      #This line prints the values of the keys which makes easier to search according to the dictiobary
word_search = input("Enter the word you wish to search: ")      #User input the word which he wishes to search
print(dict.get(word_search, "Not Found"))                       #It gets the words if word does not exists it will return "Not Found"
rate = float(input("How would you rate this dictionary: "))     #Optional it just to get user rating
print(f"Thank you for rating this dictionary :) {rate}")        #Optinal it just displays the user rating along with some warm regards

'''Q2> Write a prorgam to input 8 numbers from the user and display all the unique numbers(once).'''

s = set()
num1 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num1)
num2 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num2)
num3 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num3)
num4 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num4)
num5 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num5)
num6 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num6)
num7 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num7)
num8 =int(input("Enter any number(repeatitions are allowed): "))
s.add(num8)
print(f"The numbbers you have given but only unique number can be printed{s}")

'''Q3> Can we have set with 18(int) and '18'(str) as a value in it.'''
    # # Yes you can have set along integer along with a string values eg-
     set = {18, "18", "yes you can", 4,5}
     print(type(set))
     print(set)

'''Q4> What will the length of the following set s:
    s = set()
    s.add(20)
    s.add(20.0)
    s.add('20") #lengeth of s after these operations?   '''

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
#The output is 2 since set doesnot except duplicate values which here is 20 and 20.0 but if it was 20.9 or something else the length would have been 3

'''Q5> s = {}
    What is the type of 's'?    '''

s = {}
print(type(s))
#The type is a dictionary because an empty set is defined as --
s1 = set()
print(type(s1))

'''Q6> Create an empty dictionary. Allow 4 friends to enter their favourite languages as their values and use key as their names. Assume their names are unique.'''

dict = {}
print("DO NOT ENTER ANY DUPLICATE NAMES!!")
name1 = input("Enter your name my friend number 1: ")
key1 = input("Enter the language you like: ")
name2 = input("Enter your name my friend number 2")
key2 = input("Enter the language you like: ")
name3 = input("Enter your name my friend number 3: ")
key3 = input("Enter the language you like : ")
name4 = input("Enter your name my friend number 4: ")
key4 = input("Enter the language you like: ")
dict.update({name1 : key1, name2 : key2, name3 : key3, name4 : key4})       #This line vasically updates the dictionary with the new input values
print(dict)
print("Are you satisfied with the result")

'''Q7> If the names of two friends are same; What will happen to python program in problem 6?'''

dict = {}
print("Duplicacy is allowed in the names of friends")
name1 = input("Enter your name my friend number 1: ")
key1 = input("Enter the language you like: ")
name2 = input("Enter your name my friend number 2")
key2 = input("Enter the language you like: ")
name3 = input("Enter your name my friend number 3: ")
key3 = input("Enter the language you like : ")
name4 = input("Enter your name my friend number 4: ")
key4 = input("Enter the language you like: ")
dict.update({name1 : key1, name2 : key2, name3 : key3, name4 : key4})       #This line vasically updates the dictionary with the new input values
print(dict)
print(dict.keys())
print(dict.values())
  While printing the values of the dictionary therr was a problem found related to the same name of the friends a single friends name was regintered 
although the key values were different so neither the name or the key value was printed
as you can see in the output given below
"""OUTPUT:"""
# Duplicacy is allowed
# Enter your name my friend number 1: jef
# Enter the language you like: eng
# Enter your name my friend number 2jef
# Enter the language you like: hindi
# Enter your name my friend number 3: salman
# Enter the language you like : hindi
# Enter your name my friend number 4: morri
# Enter the language you like: urdu
# {'jef': 'hindi', 'salman': 'hindi', 'morri': 'urdu'}
# dict_keys(['jef', 'salman', 'morri'])
# dict_values(['hindi', 'hindi', 'urdu'])

'''Q8> If languages of 2 friends are same: What will happen to python program in problem 6?'''

dict = {}
print("Duplicacy is allowed in the keys values")
name1 = input("Enter your name my friend number 1: ")
key1 = input("Enter the language you like: ")
name2 = input("Enter your name my friend number 2")
key2 = input("Enter the language you like: ")
name3 = input("Enter your name my friend number 3: ")
key3 = input("Enter the language you like : ")
name4 = input("Enter your name my friend number 4: ")
key4 = input("Enter the language you like: ")
dict.update({name1 : key1, name2 : key2, name3 : key3, name4 : key4})       #This line vasically updates the dictionary with the new input values
print(dict)
print(dict.keys())
print(dict.values())

#   There was no problem found while the two different names of friends had same languages of inteest
#   As you can see the output
'''OUTPUT:'''
# Duplicacy is allowed in the keys values
# Enter your name my friend number 1: jef
# Enter the language you like: eng
# Enter your name my friend number 2jef2
# Enter the language you like: eng
# Enter your name my friend number 3: jef3
# Enter the language you like : hindi
# Enter your name my friend number 4: jef4
# Enter the language you like: urdu
# {'jef': 'eng', 'jef2': 'eng', 'jef3': 'hindi', 'jef4': 'urdu'}
# dict_keys(['jef', 'jef2', 'jef3', 'jef4'])
# dict_values(['eng', 'eng', 'hindi', 'urdu'])

'''Q9> Cam you change the values inside a list which is contained in set s?
    s = {8, 7, "Python", [1, 2]}        '''

s = {0, 7, "Python", [1,2]}
print(type(s))

# This code is wrong since a set is immutable but there is a list involved which is thereby mutable so this shows an error
# Even if there was no list involved changing a set is not ecceptable since a set is immutable
