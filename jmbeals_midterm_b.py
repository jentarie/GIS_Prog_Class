# Jen Beals
# GEOS 5073 midterm script b
# 31 March 2020
# assumes source file is in same working directory as script
# This script takes the area and population of cities from a csv file, calculates the population density,
# sorts the list by density in ascending order, and writes a new csv file with the density and density index included.

#Import module and open CSV files
import os
Path = os.getcwd()+'\\'
csv_poparea = open(Path+'poparea.csv', 'r')
csv_results = open(Path+'poparea_results.csv', 'w')

#Read and process data
lResults = []
i = 0
for line in csv_poparea:
    line = line.rstrip('\n')
    if (i==0): csv_results.write('DensityIndex,'+line+',Density')
    else:
        popLine = int(line.split(',')[3])
        areaKm = float(line.split(',')[4])
        popDens = str(popLine/areaKm)
        sPopArea = line+','+popDens
        lResults.append(sPopArea)
    i+=1
#print(lResults)

results_sorted = sorted(lResults, key = lambda rec: float(rec.split(',')[6]))
# print(results_sorted)

#write sorted results to csv file with Density Index added as the first field in each row from lowest to highest density
i=1
for line in results_sorted:
    csv_results.write('\n'+str(i)+','+line)
    i+=1

#close the csv files
csv_poparea.close()
csv_results.close()

# print the top 5 most and least dense cities
DensTop5 = results_sorted[-5:]
DensBottom5 = results_sorted[:5]
header_fields = str('DensityIndex, Rank, Name, POP2010, AREAkm, AREAmi, Density')

# print(DensTop5)
# print(DensBottom5)

print('The 5 most dense cities are:')
print(header_fields)
for line in DensTop5:
    print(line)

print('The 5 least dense cities are:')
print(header_fields)
for line in DensBottom5:
    print(line)