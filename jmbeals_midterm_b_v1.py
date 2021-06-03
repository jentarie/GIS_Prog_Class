#Jen Beals
# write some description here!!!

import os
import csv

#get and save file path to a variable with trailing slash
Path = os.getcwd()+'\\'
#open the cities and states files in read format
csv_poparea = open(Path+'poparea.csv', 'r')
#open (or create and open) a results file in write mode
csv_results = open(Path+'poparea_results.csv', 'w')

#Read and process data
#initialize counter
i = 0
#loop through poparea.csv line by line, temporarily set each line as a variable without the \n
for line in csv_poparea:
    line = line.rstrip('\n')
    # write the first line of the results file with the header values from the line of poparea.csv,
    # appended with extra column header for density
    if (i == 0): csv_results.write(line+',PopDens')
    #get the population and area and calculate the density of each line in the file
    else:
        popLine = int(line.split(',')[3]) # pop. converted to int
        # data in 3rd,4th columns, index shifted because data contains a comma in a previous column
        areaKm = float(line.split(',')[4]) #store area as a floating number value
        popDens = popLine/areaKm #calculate population density for line
        #write the line from poparea.csv to a new line with the popDens appended as a new csv column
        csv_results.write('\n'+line+','+str(popDens))
    i += 1 #move to next line

#reader=csv.reader(csv_results)
#Close CSV files
csv_poparea.close()
csv_results.close()


#Identify the top 5 most and least dense cities
#read results file
results = open(os.getcwd()+'\\poparea_results.csv', 'r')
results.readline() #read the file line by line
DensTop10 = sorted(results, key = lambda rec: rec[7])[0:10] # sorted function builds/returns a new list by iterating over existing lists, etc.

results = open(os.getcwd()+'\\poparea_results.csv', 'r')
results.readline() #read the file line by line
DensBottom10 = sorted(results, key = lambda rec: rec[6], reverse=True)[0:10]

#print results - clean up print statement later!!!!
print(DensTop10)
print(DensBottom10)

#sort results by pop density, add index field, write to csv
results = open(os.getcwd()+'\\poparea_results.csv', 'r')
results.readline() #read the file line by line
results_sorted = sorted(results, key = lambda rec: rec[6], reverse=True)[:]
#print(results_sorted)
header_fields = ['DensityIndex', 'Rank', 'Name', 'POP2010', 'AREAkm', 'AREAmi', 'Density']
# name of csv file
fResults = open('poparea_sorted.csv','w')

#results=map(lambda x:x+'\n', results)
#fResults.writelines(results_sorted)
#fResults.close()

i = 0
#loop through poparea.csv line by line, temporarily set each line as a variable without the \n
for line in results_sorted:
    line = line.rstrip('\n')
    # write the first line of the results file with the header values from the line of poparea.csv,
    # appended with extra column header for density
    if (i == 0): fResults.write(str(header_fields))
    #get the population and area and calculate the density of each line in the file
    else:
       #write the line from poparea.csv to a new line with the popDens appended as a new csv column
        fResults.write('\n'+str(i)+','+line)
    i += 1 #move to next line
#
fResults.close()

#filename.close()
csv_poparea.close()