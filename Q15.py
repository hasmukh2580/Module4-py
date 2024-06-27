'''Write a Python class named Circle constructed by a radius and
two methods which will compute the area and the perimeter of a circle'''

#define class named Circle
class Circle():
    #define __init__ constructor with required parameters
    def __init__(self,r):
        # access radius and take pi value as 3.14
        self.r = r
        self.pi = 3.14
        
    #define method to calculate area of circle
    def ClArea(self):

        ans = self.pi*self.r**2

        print("Area of circle:",ans)

    #define method to calculate perimeter of circle
    def ClPerimeter(self):

        ans = 2*self.pi*self.r

        print("Perimeter of circle:",ans)

#take radius value from user
r = int(input("Enter radius:"))

#create instance of Circle class with radius paasing as argument
Cl = Circle(r)

#call the 'ClArea()' method using object
Cl.ClArea()

#call the 'ClPerimeter()' method using object
Cl.ClPerimeter()

    