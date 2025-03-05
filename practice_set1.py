"""PRACTICE SET 1"""

'''Q1> Write a program to print twinkle twinkle little star poem in python'''
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.''')

'''Q2> Use REPL and print the table of 5'''
#In order to complete this task you need to go to you cmd prompt and type python and hit enter and manually press 5*1 and the hit enter like this way you can print the whole table and you can also perform complex mathematical problems in it like 856-6465*5859

'''Q3> Install an external module and use it to perfrom an operation of your interest'''

## In order to install an external module in you respective system you need to write pip install pyttsx3 write this on your terminal
"""THE MODULE I PICKED IS TEXT TO SPEACH MODULE"""

# import pyttsx3
# engine = pyttsx3.init() # object creation

# # RATE
# rate = engine.getProperty('rate')   # getting details of current speaking rate if you want it faster then set the rate from 10 to 110
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 10)     # setting up new voice rate


# # VOLUME
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# # VOICE
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World! I am just sharing these questions because i have just started  learning about python. if you are wondering why this voice is so slow cause I'm to old ")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# # Saving Voice to a file
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()

'''Q4> Write a python program to print the contents of the directory using the os module. Search online for the functions which doeas that and also lable the program with comments'''

import os

# Specify the directory path
directory_path = '/path/to/directory'  #if you just enter / it will give all the names of the drive (or mabe folder) you have in that folder

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
