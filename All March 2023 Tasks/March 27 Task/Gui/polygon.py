import turtle    
import time         
polygon = turtle.Pen()
my_num_sides = 6
my_side_length = 70
my_angle = 360.0 / my_num_sides
for i in range(my_num_sides):
   polygon.backward(my_side_length) 
   time.sleep(4)          
   polygon.down(my_angle) 
turtle.done()