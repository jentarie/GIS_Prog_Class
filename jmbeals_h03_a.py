#	(20 points) Develop and call a function that will:
#		1. Generate a random number n with a value between 1 and 1,000.
#		2. In the range of (n, n+200), iterate each number and count how many of them are divisible by 7 and #
#		how many of them are divisible by 13.
#Print out the result.

import random
def divis():
    n = random.randint(1,1001) #assign a random value between 1 and 1000
    #initialize counter variables
    div7 = 0
    div13 = 0
    #loop through range and increment counters for numbers that are divisible by 7 or 13
    for i in range(n,n+200):
        if i%7 == 0:
            div7 += 1
        if i%13 == 0:
            div13 += 1
    #print results
    print("There are {0} numbers divisible by 7 and {1} numbers divisible by 13 in the range {2} to {3}.".format(str(div7),str(div13),str(n),str(n+200)))
#call function
divis()
