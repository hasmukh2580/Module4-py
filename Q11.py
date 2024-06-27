'''Write a Python program to write a list to a file'''

#open existing file with 'w+' method
file = open("C:\\Users\\HASMUKH\\Desktop\\Assignmentss\\Text file\\text7.txt","w+")

#create a list of items
phones = ['samsung','iphone','vivo','oneplus','oppo']

#run a for loop through each items in list
for i in phones:
    #write each item in file
    file.write(i)
    file.write('\n')

#point the cursor at the begining of file
file.seek(0)

#now read the content of file
txt = file.read().split()

#print the content of file
print(txt)