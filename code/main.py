__author__ = 'KKumaresan'
########################################################################################################################
# Problem1: Given a list of people with their birth and end years (all between 1900 and 2000),
# find the year with the most number of people alive.
# Date:06/09/2016
########################################################################################################################
from input import input
from globals import globals
from datetime import datetime
########################################################################################################################
def main():
    # uncommenting below line generates random input automatically
    # input.generateInput()
    # Gets input form dataset text file
    inputList = input.getInput()
    maxAliveInfo = maximumPopulationYear(inputList)
    maxYears = maxAliveInfo[0]
    for year in maxYears:
        print ('Result: {0} had max numer of {1} people alive').format(globals.StartYear+year,maxAliveInfo[1])

########################################################################################################################
# Finds the year with maximum people alive in O(n) time complexity
# Algorithm:
# 1. create a population list with size EndYear-StartYear and fill with 0's
# 2. iterate through each input
# 3. increment the alive count for that birth year in population list
# 4. decrement the alive count for the death year in population list
# 5. Finally sum all the items in the population list, keeping track of maximum indexs
# 6. Adding this to the Start year will give the answer
########################################################################################################################
def maximumPopulationYear(people):
    startTime = datetime.now()
    maxSum, sum = 0, 0
    maxIndexs=[]
    if (len(people) > 0):
        populationList = [0 for i in range(globals.StartYear, globals.EndYear+1)]
        for person in people:
            populationList[person.birthYear - globals.StartYear] += 1
            populationList[person.deathyear - globals.StartYear] -= 1
        for index, item in enumerate(populationList):
            sum = sum + item
            if (sum == maxSum):
                maxIndexs.append(index)
            if (sum>maxSum):
                maxSum=sum
                del(maxIndexs[:])
                maxIndexs.append(index)
    else:
        print 'Input is empty, Enter a valid input'
    endTime = datetime.now()
    # uncomment below to print compute time
    # print 'compute time: {0}'.format((endTime-startTime).microseconds)
    return (maxIndexs, maxSum)
########################################################################################################################

if __name__=="__main__":main()