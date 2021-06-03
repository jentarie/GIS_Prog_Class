#GEOS 5073 midterm script c
#Jen Beals
#31 March 2020
#adapted from the solution provided by J. Tullis

#this script inputs a csv file of hydrants and outputs a results file with the nearest three hydrants to each hydrant.
# Assumes hydrant data is in the same folder as script file.

import os, math

# Read data from csv files, create results file
Path = os.getcwd()+'\\'
csv_hydrants = open(Path+'hydrants.csv', 'r')
csv_results = open(Path + 'jmbeals_midterm_c_results.csv', 'w')
csv_results.write('FID,X,Y,N1,D1,N2,D2,N3,D3')

#read data into list variable and process
results_list = [] #create a new empty list to add records with an added field for distance from point
hydrants_list = csv_hydrants.readlines() #read the file line by line and save to a variable as a list
hydrants_list.pop(0) #remove the header row from the data list

#calculate distance from each hydrant to each other hydrant, sort the hydrants by distance, and append the top three hydrants to each record row
#write the results to a csv file and to a results list to use in python
i=0
for hydrant in hydrants_list:
    fields = hydrant.rstrip('\n').split(',') #create a variable for the fields in each row in the list
    distance_list = []
    j = 0
    for hydrant in hydrants_list:
        if (i != j):
            temp_list = hydrant.rstrip('\n').split(',')
            x1, x2 = float(fields[1]), float(temp_list[1]) #store the x coordinates fo the hydrant we are checking and the one we are comparing against
            y1, y2 = float(fields[2]), float(temp_list[2]) # same as above for y coordinates
            temp_list.append(math.sqrt((x1-x2)**2 + (y1-y2)**2)) #calculate the Euclidean distance and append to the temp list which contains the hydrant info
            distance_list.append(temp_list) #add the row with the Euclidean distance appended to the distance list of all compared hydrant for the reference hydrant
        j+=1
    distance_list = sorted(distance_list, key = lambda x: x[3]) #sort the distance list file by the 4th column containing the Euclidean distance
    for temp_list in distance_list[0:3]: #for the top three records in the sorted list, append the fields with the hydrant ID and distance to the records
        fields.append(temp_list[0])
        fields.append(temp_list[3])
    csv_results.write('\n'+','.join(str(field) for field in fields)) #append fields to csv file
    results_list.append(fields) #append fields to results list
    i+=1

#print the 10 most indispensible hydrants - those that are farthest from another hydrant
#sort the list by the field containing the first closest hydrant
#print thy hydrant fieild ID, number, and distance to closest hydrant
results_list = sorted(results_list, key=lambda x: x[4], reverse=True)
print('FID, N1, D1')
for hyd in range(0,10):
    print(results_list[hyd][0]+ ', '+results_list[hyd][3]+', '+str(results_list[hyd][4]))

#close csv files
csv_hydrants.close()
csv_results.close()
