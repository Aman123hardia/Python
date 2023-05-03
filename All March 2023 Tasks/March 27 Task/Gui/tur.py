import turtle            
# import Tkinter
 
print( turtle.Screen()) 
print(turtle.Screen().bgcolor("yellow"))       # creates a graphics window
my_pen=turtle.Turtle() 
while True: 
    my_pen.forward(15)           
    my_pen.left(90)               
    my_pen.forward(75)
    my_pen.color("orange")
    my_pen.pensize(12)
