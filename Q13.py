'''Write a Python class named Rectangle constructed by a length and width
 and a method which will compute the area of a rectangle'''

#define class named Rectangle
class Rectangle():
    #define __init__ constructor with required parameters
    def __init__(self,lt,wt):
        #access the values of parameters with instance of class 'self'
        self.lenght = lt
        self.width = wt

    #define method to calculate area of rectangle
    def RectArea(self):
        #multiply the lenght with width and store answer in variable
        ans = self.lenght * self.width
        #print the answer
        print("Area of Rectangle:",ans)

#take length and width from user
lt = int(input("Enter length of Rectangle:"))
wt = int(input("Enter width of Rectangle:"))

#Create instance of Rectangle class with arguments taken from user
RA = Rectangle(lt,wt)

#call the defined method with created object
RA.RectArea()
