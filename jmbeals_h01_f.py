#GEOS 3103/5073 Homework 1 Script f
#Jen Beals
#30 Jan 2020

#this function returns the difference between the maximum and minimum values in a given list of numbers (float) as input by a user
def differenceMaxMin():
    numList = [] #create an empty list of numbers to be populated
    n = int(input("Enter number of elements in the list: ")) #define number of elements in list
    #query the user for numbers and append into numList by looping through input() query n times
    for i in range(0,n):
        num = float(input('Enter value of element number ' + str(i+1) + ': '))
        numList.append(num)
    print(max(numList) - min(numList)) #print the difference between max and min value in list
differenceMaxMin() #call the function
