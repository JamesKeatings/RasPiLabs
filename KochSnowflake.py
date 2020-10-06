# Python program to print complete Koch Curve. 
from turtle import *
  
# function to create koch snowflake or koch curve 
def snowflake(lengthSide, levels): 
    if levels == 0: 
        forward(lengthSide) 
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
    right(120) 
    snowflake(lengthSide, levels-1) 
    left(60) 
    snowflake(lengthSide, levels-1) 
  
# main function 
if __name__ == "__main__": 
    # defining the speed of the turtle 
    speed(200)                    
    length = 400.0   
  
    # Pull the pen up  no drawing when moving. 
    # Move the turtle backward by distance, opposite 
    # to the direction the turtle is headed. 
    # Do not change the turtles heading.            
    penup()                      
  
    backward(length/2.0) 
  
    # Pull the pen down  drawing when moving.         
    pendown()            
    for i in range(3):     
        snowflake(length, 5)
        right(120) 
  
     # To control the closing windows of the turtle 
    mainloop() 
