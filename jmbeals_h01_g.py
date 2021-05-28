#GEOS 3103/5073 Homework 1 Script G
#Jen Beals
#23 Jan 2020

#this function returns the length of a line segment given the x and y coordinates of its endpoints as lists of two x-coords and 2 y-coords.
def lenLineSeg(lXCoord,lYCoord):
    nDX = float(lXCoord[1])-float(lXCoord[0]) #calculate the difference between the two x-coords as a floating(decimal) value and assign it to a variable
    nDY = float(lYCoord[1])-float(lYCoord[0])#calculate the difference between the two y-coords as a floating(decimal) value and assign it to a variable
    nLenSeg = ((nDX**2)+(nDY**2))**(1/2.0) #calculate the length of the line segment and assign it to a variable
    return nLenSeg #return the value of the length of the line segment in the form of a usable input for another function or call

#this function prints the summed total length of two contiguous line segments
def lenTwoLineSeg():
    lXCoord = input('Please enter three x coordinates (comma-separated) >>>').split(',') #input and store the 3 x coords in a list
    lYCoord = input('Please enter three y coordinates (comma-separated) >>>').split(',') #input and store the 3 y coords in a list
    nLenSeg1 = lenLineSeg(lXCoord[0:2],lYCoord[0:2]) #calculate the length of the first line segment by calling the lenLineSeg function using the first pair of coordinates - element indices 0 and 1 in lists. Then assign the calculated value to a variable.
    nLenSeg2 = lenLineSeg(lXCoord[1:3],lYCoord[1:3]) #calculate and store the length of the second line segment by same method as above - element indices 1 and 2 in lists
    print('\nThe total length of the two line segments is '+str(nLenSeg1+nLenSeg2)) #print the summed length of both line segments
lenTwoLineSeg() #call the function
