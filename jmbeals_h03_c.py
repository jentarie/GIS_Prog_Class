#		1. Read point data in a csv file that has 1,354 points along with PID, NAME, POP2000, X, and Y coordinates;
#		please use the following data file titled cities.csv:
#		2. Generate a single pair of random x, y coordinates within the given range: X ( -104, -79) , Y (31, 45),
#		print x, y, and print the total number of points read in from the CSV file.
#		3. Find the nearest 10 points (from those obtained through step 1) to the randomly generated point (from step 2),
#		#and print the result including PID, distance, name, and POP2000.
#		4. Among these 10 points, find the one that has the largest number of POP2000, and print the result including PID, name and POP2000.

import math
import random
import os

#generate random point
XRand = random.randint(-104,-79)
YRand = random.randint(31,45)

#read file
fCities = open(os.getcwd()+'\\cities.csv', 'r')
lRecs = [] #create a new empty list to add records with an added field for distance from point
fCities.readline() #read the file line by line

while True:
    lCells = fCities.readline().split(',') #generate a list from the cells in the current line being read
    if lCells[0] == '': break #stop when the line contains an empty value in the first field
    DeltaX = float(lCells[3]) - XRand #calculate the X distance
    DeltaY = float(lCells[4]) - YRand #calculate the Y distance
    DistToRand = math.sqrt(math.pow(DeltaX, 2) + math.pow(DeltaY, 2)) #calculate the distance from current coordinate pair to random point
    lCells.append(DistToRand) #add the distance as a new value in the line being read
    lRecs.append(lCells) #add the appended line to the new list for appended records (leaving the original file alone

#Identify the 10 nearest cities and which one of those has the highest population
Nearest10 = sorted(lRecs, key = lambda rec: rec[5])[0:10] # sorted function builds/returns a new list by iterating over existing lists, etc.
#lambda is on "on-the-fly" function syntax so that we can use only the column - the 5th field index in each row to sort, and then return the top 10 results
HighestPop = sorted(Nearest10, key = lambda rec: rec[2], reverse = True)[0]
#out of the 10 cities identified, reverse sort (highest to lowest) on population and return the top result.

#Print all the results
print('Random coordinates: '+str(XRand)+', '+str(YRand))
print('Number of points read in from the file: '+str(len(lRecs)))
print('The nearest ten cities are:')
for r in Nearest10: #loop through records and print results
    print('  PID: '+str(r[0]))
    print('    Distance: '+str(r[5]))
    print('    Name: '+str(r[1]))
    print('    POP2000: '+str(r[2]))
print('The most populous of these 10 cities, '+str(HighestPop[1]) +', had a population of '+str(HighestPop[2])+' in the year 2000')


#Close the CSV data file
fCities.close()
