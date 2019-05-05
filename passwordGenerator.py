#   Jake Espinosa

#   Homework 7-2

#   hw7-2.py

#   Description

# housekeeping

import random
import time
upperList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numberList = ['0','1','2','3','4','5','6','7','8','9']
specialList = ['!','@','#','$','%','^','&','*','?','<','>']
totalLength = 0
chosenUpper  = 0
chosenLower = 0
chosenNumber = 0
chosenSpecial = 0
chosenLength = 0
charsList = []
concatenator = 0
password = ''

# Name: getAnInt

# Input: none

# Output: an single integer

# Description:
# This function requires the user to input an integer and checks it to make sure
# it is an integer then returns it.

def getAnInt():
    while True:
        try:
            
            isItAnInt = input()
            if (int(isItAnInt)):
                isItAnInt = int(isItAnInt)
                break

        except ValueError:
            print('Please enter an integer (whole number)!')
    return isItAnInt

try:
    
# prompt user for chosen variables

    print('Welcome to my password generator script!')
    
    while True:
        print('Enter the desired length of your password (8 or more is recommended):')
        chosenLength = getAnInt()
        totalLength = 0
        print('Enter the desired number of uppercase characters:')
        chosenUpper = getAnInt()
        totalLength = totalLength + chosenUpper
        print('Enter the desired number of lowercase characters:')
        chosenLower = getAnInt()
        totalLength = totalLength + chosenLower
        print('Enter the desired number of numbers:')
        chosenNumber = getAnInt()
        totalLength = totalLength + chosenNumber
        print('Enter the desired number of special characters:')
        chosenSpecial = getAnInt()
        totalLength = totalLength + chosenSpecial
        if chosenLength < totalLength:
            print('Oops! The length of your password exceeds the desired length!')
        if chosenLength >= totalLength:
            break

    if chosenLength > totalLength:
        difference = chosenLength - totalLength
        chosenLower = chosenLower + difference
        
# logic

    for i in range(chosenUpper):
        upperSelector = random.randint(0,25)
        upperToAdd = upperList[upperSelector]
        charsList.append(upperToAdd)

    for i in range(chosenLower):
        lowerSelector = random.randint(0,25)
        lowerToAdd = lowerList[lowerSelector]
        charsList.append(lowerToAdd)

    for i in range(chosenNumber):
        numberSelector = random.randint(0,9)
        numberToAdd = numberList[numberSelector]
        charsList.append(numberToAdd)

    for i in range(chosenSpecial):
        specialSelector = random.randint(0,10)
        specialToAdd = specialList[specialSelector]
        charsList.append(specialToAdd)

# shuffle charsList and display the password

    random.shuffle(charsList)

    for i in range(len(charsList)):
        password = password + charsList[concatenator]
        concatenator = concatenator + 1
        
    
    print('Here is your password!')
    print(password)
    time.sleep(5)

    print('Thank you for using my password generator script!')
    
# way to handle Ctrl+C
    
except KeyboardInterrupt:
    print('Ctrl+C was entered, program terminating...')
