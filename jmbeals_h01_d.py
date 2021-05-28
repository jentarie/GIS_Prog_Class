#GEOS 3103/5073 Homework 1 Script d
#Jen Beals
#30 Jan 2020

#this function finds the centroid of a triangle given its 3 x,y coordinate pairs in the form of x and y coordinate lists

#define function with two parameters containing lists of x and y coordinates - 3 each
def centroidTriangle(xC,yC):
    #average the values of the x coordinates
    xCent = (xC[0] + xC[1] + xC[2])/3
    #average the values of the y coordinates
    yCent = (yC[0] + yC[1] + yC[2])/3
    #print the centroid coordinate value
    print('The x,y coordinate of the centroid is ' + str(xCent) + ',' + str(yCent))
#initialize variables
xCoord = [3,6,9]
yCoord = [5,10,15]
#call function
centroidTriangle(xCoord,yCoord)
