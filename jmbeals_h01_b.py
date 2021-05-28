#GEOS 3103/5073 Homework 1 Script b
#Jen Beals
#30 Jan 2020

#This function returns the largest of the numbers in a given list and prints out the result.

#Define the numbers to be searched
myList = [1,2,3,4]

#define the function using a list of numbers variable as the input parameter
def largestNum(numList):
    print('The largest number in the list is ' + str(max(numList))) #print the largest value in the list using the max method [for lists, built in 'function' in python].

#call the function using the defined list of numbers as input
largestNum(myList)
