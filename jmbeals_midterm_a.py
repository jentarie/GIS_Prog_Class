#GEOS 3103/5073 Midterm Script A
#Jen Beals
#Adapted from Tullis (2019)
#Assumes midterm data is in same folder as this script
#2020 19 March

#Import module and open CSV files
import os
#get and save file path to a variable with trailing slash
sPrj = os.getcwd()+'\\'
#open the cities and states files in read format
fCities = open(sPrj+'cities.csv', 'r')
fStates = open(sPrj+'states.csv', 'r')
#open (or create and open) a results file in write mode
fResults = open(sPrj+'jmbeals_midterm_a_results.csv', 'w')

#Read and process data
#create an empty dictionary object to store state information
dStates = {}
#loop through the states.csv, read the file line by line, remove the newline character from the end of each line,
# set the first column as the key, and combine the second and third columns as the value
for sState in fStates:
    sState = sState.rstrip('\n')
    dStates[sState[0:2]] = sState[2:] #set the first two characters in the line as the key, the remainder of the line as the value

#for key,value in dStates.items():
#    print("Key : {} , Value : {}".format(key,value))

#initialize counter
i = 0
#loop through cities.csv line by line, temporarily set each line as a variable without the \n
for sCity in fCities:
    sCity = sCity.rstrip('\n')
    # write the first line of the results file with the header values from the line of cities.csv,
    # appended with two extra labelled columns for state name and abbreviation
    if (i == 0): fResults.write(sCity+',STATE_NAME,STATE')
    #set the state key variable to the value of the current line, spliting the values with a comma since it is a .csv file
    #get the state key from the first two numbers of the long code in the second column in cities.csv
    else:
        sStateKey = sCity.split(',')[1][0:2]
        #write the line from cities.csv to a new line with the state name and abbreviation added by looking up in dStates with key
        fResults.write('\n'+sCity+str(dStates.get(sStateKey)))
    i += 1 #move to next line

#Close CSV files
fCities.close()
fStates.close()
fResults.close()
