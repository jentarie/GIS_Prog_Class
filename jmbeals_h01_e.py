#GEOS 3103/5073 Homework 1 Script e
#Jen Beals
#30 Jan 2020

#This function calculates the average of a user-defined list of numbers through the input() method.

#First enter the number of elements to be averaged, then input each numerical element as prompted.
def averageInput():
    #create an empty list to contain the numbers input by the user
    numList = []
    #define the number of elements to be averaged
    n = int(input("Enter number of elements to be averaged: ")) #define number of elements in list
    #query user to enter and store the numbers in the numList by looping through input() query n times
    for i in range(0,n):
        num = float(input('Enter value of element ' + str(i+1) + ' to be averaged: '))
        numList.append(num)
    #print the average value of numbers in the list
    print(sum(numList)/n)
#call the function
averageInput()
