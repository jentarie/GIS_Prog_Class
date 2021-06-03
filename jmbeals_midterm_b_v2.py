#Jen Beals
# write some description here!!!
# assumes source file is in same working directory as script

import os


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
for line in csv_poparea.readlines():
    line = line.rstrip('\n')
    # write the first line of the results file with the header values from the line of poparea.csv,
    # appended with extra column header for density
    if (i == 0): csv_results.write(line+',PopDens')
    #get the population and area and calculate the density of each line in the file
    else:
        popLine = int(line.split(',')[3]) # pop. converted to int
        # data in 3rd,4th columns, index shifted because data contains a comma in a previous column
        areaKm = float(line.split(',')[4]) #store area as a floating number value
        popDens = float(popLine)/float(areaKm) #calculate population density for line
        #write the line from poparea.csv to a new line with the popDens appended as a new csv column
        csv_results.write('\n'+line+','+str(popDens))
    i += 1 #move to next line

#reader=csv.reader(csv_results)
#Close CSV files
csv_poparea.close()
csv_results.close()


#Identify the top 5 most and least dense cities

#read results into file and sort them - Method 1
fResults = open(os.getcwd()+'\\poparea_results.csv', 'r')
results = fResults.readlines()
results.pop(0) #remove header row
lResults = [] #create list for results to work with in code


# #read results into list
for line in results:
    lResults.append(line.rstrip('\n'))
# print(lResults)


results_sorted = sorted(lResults, key = lambda rec: (rec[5]), reverse = False)
# Traceback (most recent call last):
#   File "C:/Users/jbeal/GIS_Prog/midterm_data/jmbeals_midterm_b_COMMENTS.py", line 55, in <module>
#     results_sorted = sorted(lResults, key = lambda rec: float(rec[5]), reverse = False)
#   File "C:/Users/jbeal/GIS_Prog/midterm_data/jmbeals_midterm_b_COMMENTS.py", line 55, in <lambda>
#     results_sorted = sorted(lResults, key = lambda rec: float(rec[5]), reverse = False)
# ValueError: could not convert string to float: 'w'

# print(results_sorted)

#created new lists with only the top five and bottom five rows of results
DensBottom10 = results_sorted[-5:]
DensTop10 = results_sorted[:5]

# print results - clean up print statement later!!!!
print(DensTop10)
print(DensBottom10)


header_fields = ['DensityIndex', 'Rank', 'Name', 'POP2010', 'AREAkm', 'AREAmi', 'Density']
# name of csv file
fResults = open('poparea_sorted.csv','w')

# results_sorted=map(lambda x:x+'\n', results)
# fResults.write(str(header_fields))
# fResults.writelines(results_sorted)
# fResults.close()

i = 0
# #loop through poparea.csv line by line, temporarily set each line as a variable without the \n
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
