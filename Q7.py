'''Write a Python program to read a file line by line store it into a variable'''

#create a variable with strings
txt = 'Mango\nOrange\nBanana\n'

#open a new file with write mode
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\Text file\\text4.txt","w")

#write the content of variable into file using 'writelines()' method
file.writelines(txt)

#open the same file again with the read mode
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\Text file\\text4.txt","r")

#read the content of file using 'readlines()' method
lines = file.readlines()

#assign 1 to counter variable
c = 1

#run a for loop to print the content line by line
for line in lines:

    print("Line",c,":",line)
    #increment counter by 1 after each line
    c+=1

file.close()