'''Write a Python program to append text to a file and display the text'''



#open the existing text file using open method with the append mode
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\text1.txt","a")

#get text from user to append in existing file
txt = input("Enter text to append:")

#write the text to file 
file.write(txt)

#open the file again with the read mode
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\text1.txt","r")

#read all the content of file in 'txt' variable
txt = file.read()

#print the 'txt' variable
print(txt)

#close the file to free up the memory space acquired by that file
file.close()
