#	(20 points) Develop and call a function that will:
#		1. Generate 150 random numbers with a value between 1 and 1,000.
#		2. Calculate the total, mean, maximum, minimum, and standard deviation of these numbers.
#		3. Print out the result.

import random
import math

def stats():
    numbers = [] #create empty list to hold random numbers
    #add 150 random numbers between 1 and 1000 to the list
    for x in range(150):
        numbers.append(random.randint(1,1001))
    #calculate total, mean, max, and min values for numbers in list
    total = sum(numbers)
    mean = total/len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    #Initialize a variable to hold the sum of the squared differences for st. dev. (i.e. (x_i - x_bar)**2)
    sqdif = 0
    for val in numbers:
        sqdif += (val - mean)**2
    #calculate st. dev. = sqrt(avg squared difference)
    stdev = math.sqrt(sqdif/150)
    #print results
    print('Total: ' + str(total))
    print('Mean: ' + str(mean))
    print('Minimum: ' + str(minimum))
    print('Maximum: ' + str(maximum))
    print('Standard deviation: ' + str(stdev))
#call function
stats()
