########################################################################################################################
__author__ = 'KKumaresan'
########################################################################################################################
# Input format: zzzz:yyyy
# z and y should be numbers, all other formats will be rejected
# each input should be ina seperate line
# Example: 1904:1965
########################################################################################################################
import os
import random
from person import person
from globals import globals
########################################################################################################################
class input:
    # Generates dataset to test the code and updates the dataset.txt
    # Used random package to generate random data set within limits each time
    @staticmethod
    def generateInput():
        if os.path.exists(globals.fileName):
            with open(globals.fileName,'w+') as f:
                for i in range(globals.inputNumber):
                    birthYear = random.randrange(globals.StartYear,globals.EndYear)
                    deathYear = random.randrange(birthYear,globals.EndYear)
                    f.write(str(birthYear)+':'+str(deathYear)+'\n')


    @staticmethod
    def getInput():
        inputList=[]
        if os.path.exists(globals.fileName):
            with open(globals.fileName) as f:
                for line in f:
                    temp= input.getyears(line)
                    if temp is not None:
                        inputList.append(temp)
        else:
            print 'Input File cannot be found'
        return inputList

    @staticmethod
    def getyears(inputString):
        if len(inputString)== 0:
            return
        else:
            inputString = inputString.rstrip('\n')
            inputString = inputString.split(":")
            temp = input.validateYears(inputString)
            if temp is not None:
                return (person(temp[0], temp[1]))
            else:
                input.printInvalid(inputString)

    @staticmethod
    def validateYears(yearString):
        inputSize = 2
        yearSize = 4
        if (len(yearString) == inputSize):
            birth = yearString[0]
            death = yearString[1]
            if len(birth) == yearSize and birth.isdigit():
                birth = int(birth)
                if len(death) == yearSize and death.isdigit():
                    death=int(death)
                    if (birth <= death and birth >= globals.StartYear and death <= globals.EndYear):
                        return (int(yearString[0]), int(yearString[1]))

    @staticmethod
    def printInvalid(inputString):
        print ('{0} is invalid and will not not be considered').format(inputString)
########################################################################################################################