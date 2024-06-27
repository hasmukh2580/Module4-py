'''Write a Python program to count the frequency of words in a file'''

#open a new text file with read mode
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\Text file\\text6.txt","r")

#read and split each words in variable
lines = file.read().split()

#create empty dictionary
fdict = {}

#run a for loop through each word 
for line in lines:
    #check if word is present in dictionary
    if line in fdict:
        #if true then take word as dictionary key and increase its value by 1
        fdict[line] += 1

    else:
        #if false then assign 1 as value
        fdict[line] = 1

#print the dictionary
print(fdict)

file.close()


