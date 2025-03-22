# Q1> Write a program to read text from a given file 'poem.txt' and find out whether it contains the word "twinkle".

with open("poem.txt") as f:
    for line in f:  
        if ("Twinkle" in line):  # Check if "Twinkle" exists in the current line
            print("Yes, the word 'Twinkle' is present in the file poem.txt")
            break  # Stop checking further once found
        else:
            print("There was no such word found in the file poem.txt")