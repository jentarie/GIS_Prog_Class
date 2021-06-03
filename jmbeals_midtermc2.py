
import os
import math
import csv


Path = os.getcwd()+'\\'
#open the hydrants file in read format
csv_hydrants = open(Path+'hydrants_trunc.csv', 'r+')

#input_file = open("nameOfFile.csv","r+")
reader_file = csv.reader(csv_hydrants)
length = len(list(reader_file))

#lRecs = [] #create a new empty list to add records with an added field for distance from point
csv_hydrants.readline() #read the file line by line


while True:
    lCells = csv_hydrants.readline().split(',') #generate a list from the cells in the current line being read
    if lCells[0] == '': break #stop when the line contains an empty value in the first field
    Xcoord = float(lCells[1])
    Ycoord = float(lCells[2])
    while True:
        compCells=csv_hydrants.readline().split(',')
        if lCells[0] == '': break  # stop when the line contains an empty value in the first field
        cXcoord = float(lCells[1])
        cYcoord = float(lCells[2])
        DeltaX = float(lCells[1]) - Xcoord  # calculate the X distance
        DeltaY = float(lCells[2]) - Ycoord  # calculate the Y distance
        distances = dict()
        DistToHydrant = math.sqrt(math.pow(DeltaX, 2) + math.pow(DeltaY, 2))
        distances[compCells[0]]=DistToHydrant
        print(distances)
