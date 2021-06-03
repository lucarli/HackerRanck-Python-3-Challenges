#Hackerrank Validating UID

#Author: Luciano Carli Moreira de Andrade

#ABCXYZ company has up to 100 employees.
#The company decides to create a unique identification number (UID) for each of its employees.
#The company has assigned you the task of validating all the randomly generated UIDs.

#A valid UID must follow the rules below:

#It must contain at least 2 uppercase English alphabet characters.
#It must contain at least 3 digits (0 - 9).
#It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
#No character should repeat.
#There must be exactly 10 characters in a valid UID.

#Input Format

#The first line contains an integer T, the number of test cases.
#The next T lines contains an employee's UID.

#Output Format

#For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

import re

regex = r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$"

T = int(input())

for _ in range(T):
    
    uid = input()
    
    print("Valid" if re.match(regex, uid) else "Invalid")
    