# syntax for reading a file->
f = open("myfile.txt","r")             #well it's not neccesary to write "r" because in default mode it will take it as read
data = f.read()
print(data)
f.close()


# syntax for writing in a file->
f = open("file.txt","w")               #writing w is neccesary
#If a file with such a name doesnot exist in your folder then it will create a file with the same name
st = input("Enter the string you wish to add on the file: ")
f.write(st)
f.close()
#Well closing the file every time is not neccesary but this is a good practice to close the file or else some other code won't be able to access it


#syntax for appending a string inside a file->
f = open("file.txt","a")               #writing a is neccesary
st = input("Enter the string which you wish to append: ")
f.write(st)
f.close()

#well if you are tired of closing the file then use the following syntax and if you are not tired then ..... well i am tired so look below->
with open("myfile.txt") as fi:
    print(fi.read())
#same can be done for appending and writing into a file

#syntax for printing a single line one at a time with a return type as string
with open("myfile.txt") as re:
    line = re.readline()
    while(line != ""):            #this condition will print all the lines one by one until it finds nothing 
        print(line)
        re.readline()
