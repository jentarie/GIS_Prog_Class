#GEOS 3103/5073 Homework 1 Script H
#Jen Beals
#30 Jan 2020

#this function prints the centroid coordinates of a rectangle given user input corner x,y coordinates
def centroidRectangle():
    print('Please enter coordinates of the rectangle (comma-separated):') #query the user for coordinates
    lMinCoord = input('Minimum x,y >>> ').split(',') #store the coordinates of one corner of the rectangle by quertying the user for input of the minimum (x,y) coordinate pair of the 4 vertices of the rectangle
    lMaxCoord = input('Maximum x,y >>> ').split(',') #store the coordinates of the opposite corner of the rectangle
    sX = str((float(lMinCoord[0])+float(lMaxCoord[0]))/2.0) #calculate the mean x coordinate value and store in variable
    sY = str((float(lMinCoord[1])+float(lMaxCoord[1]))/2.0) #calculate the mean y coordinate value and store in variable
    print('\nThe x,y centroid coordinates of the rectangle are: '+sX+','+sY) #print the centroid coordinates of the rectangle
centroidRectangle() #call the function
