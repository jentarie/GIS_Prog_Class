#GEOS 3103/5073 Homework 1 Script c
#Jen Beals
#30 Jan 2020

#this function finds the length of a line segment given two x and two y coordinates

#import the math dictionary to use the square root function contained therein
import math
#define variables
x = [20,24]
y = [23,26]
#define function with two parameters containing lists of 2 x and 2 y coordinates, respectively
def lenLineSeg(x,y):
    c = math.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2) #calculate length of line segment and assign it to a variable
    print('The length of the line segment is ' + str(c)) #print the length as a statement by converting the numerical value of the variable to a string #okay as float or shoult it be converted to int??? str(int(c))

#call function using user-defined variables
lenLineSeg(x,y)
