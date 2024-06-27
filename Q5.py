'''Write a Python program to read last n lines of a file'''

#open the existing text file using read method
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\Text file\\text2.txt","r")

#read all the lines using readlines() method
lines = file.readlines()

#get the number from the user
n = int(input("Enter number to read lines:"))

#run a loop from 'n' to last lines using slicing and print it
for line in lines[-n:]:

        print(line)

file.close()