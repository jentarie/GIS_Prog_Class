#GEOS 3103/5073 Homework 1 Script a
#Jen Beals
#30 Jan 2020

#This function inputs a list of numbers and outputs the sum and product of all numbers in the list.

#input: define a list of numbers
myList = [1,2,3,4,5]

#define the function with input parameter of a list of numbers
def sumMult(numList):
    #sum the variables
    sum = 0
    for num in numList:
        sum += num
    #multiply the variables
    mult = 1
    #loop through numbers in the list and multiply - and update - the mult variable
    for num in numList:
        mult *= num
    #output (print) the results
    print('The sum of the numbers in the list is ' + str(sum))
    print('The multiplication of the numbers in the list is ' + str(mult))

#call the function using the list assigned to the myList variable
sumMult(myList)
