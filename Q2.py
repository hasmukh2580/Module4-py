'''Write a Python program to read an entire text file.'''



#open the existing text file using open method 
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\text1.txt","r")

#read all the content of file in 'txt' variable
txt = file.read()

#print the 'txt' variable
print(txt)

#close the file to free up the memory space acquired by that file
file.close()  