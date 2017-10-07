#! python3

''' Automate the boring stuff chapter 7 - regex
1. Import re
2. create a regex object using re.compile()
3. Pass a string into regex object search method to return a Match object
4. Call the Match object's group method to return a string of the matched text

Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password is defined as one that is at least
eight characters long, contains both uppercase and lowercase characters, and
has at least one digit. You may need to test the string against multiple regex
patterns to validate its strength.

Ok, so do I need to design a regular expression
[A-Z] [a-z] [0-9]
ie at least 1 lowercase, at least 1 uppercase, at least one digit, and 8 or more characters
'''

import re
import sys

def checkPass(somePassword):
    capsRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    numRegex = re.compile(r'[0-9]+')
    capsMo = capsRegex.search(somePassword)
    lowerMo = lowerRegex.search(somePassword)
    numMo = numRegex.search(somePassword)
    print(capsMo, lowerMo, numMo)
    if (len(somePassword)>7):
        if(capsMo == None):
            print('Your password ', somePassword, ' is invalid because it has no capital letters')
        elif(lowerMo == None):
            print('No lower letters called')
            print('Your password ', somePassword, ' requires at least one lower case letter')
        elif(numMo == None):
            print('No numbers called')
            print('Error: Your password ', somePassword, ' requires at least one number')
        else:
            print('Your password is valid')
    else:
        print('Invalid password. Password must be 8 characters.')

password = sys.argv[1]
checkPass(password)
