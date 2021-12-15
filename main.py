import re
import root

# takes in lists a, b and c that each contain coefficients and returns the appropriate int or float value in the form of a tuple
def listToValue(a, b, c):
    aValue = ""
    bValue = ""
    cValue = ""
    for i in a:
        aValue = aValue + i
    if(aValue.find('.') != -1):
        aValue = float(aValue)
    else:
        aValue = int(aValue)
    for i in b:
        bValue = bValue + i
    if(bValue.find('.') != -1):
        bValue = float(bValue)
    else:
        bValue = int(bValue)
    for i in c:
        cValue = cValue + i
    if(cValue.find('.') != -1):
        cValue = float(cValue)
    else:
        cValue = int(cValue)
    return aValue, bValue, cValue

pattern = "^(-0)\.{1}\d*[1-9]+\d*$"
pattern2 = "^-[1-9]\d*(\.\d+)?$"
pattern3 = "^((-0)\.{1}\d*[1-9]+\d*|-[1-9]\d*(\.\d+)?)(x\^2){1}(\+|-){1}\d+\.?\d*x{1}(\+|-){1}\d+\.?\d*$" # pattern to match quadratic function where a < 0
exp = input("Enter the quadratic equation that models trajectory of football (a < 0) ") # quadratic equation that models trajectory
while(not re.search(pattern3, exp)): # while loop ensures validation of quadratic equation
    print("Invalid form")
    exp = input("Try again ")
# empty lists for a, b and c will contain string values of the respective coefficients
aList = []
bList = []
cList = []
# check variables will be used for iteration to push the string values of the coefficients
aCheck = 0
bCheck = 0
cCheck = 0
indexTracker = 0
while(aCheck != 1):
    if(exp[indexTracker+1] == 'x'):
        aList.append(exp[indexTracker])
        indexTracker = indexTracker + 4
        aCheck = 1
    else:
        aList.append(exp[indexTracker])
        indexTracker = indexTracker + 1
if(aCheck == 1):
    while(bCheck != 1):
        if(exp[indexTracker+1] == 'x'):
            bList.append(exp[indexTracker])
            indexTracker = indexTracker + 2
            bCheck = 1
        else:
            bList.append(exp[indexTracker])
            indexTracker = indexTracker + 1
if(bCheck == 1):
    while(cCheck != 1):
        if(indexTracker < len(exp)):
            cList.append(exp[indexTracker])
            indexTracker = indexTracker + 1
        else:
            cCheck = 1
coefficientTuple = listToValue(aList, bList, cList) # function call returns tuple containing coefficients
roots = root.quadratic(coefficientTuple[0], coefficientTuple[1], coefficientTuple[2]) # call to quadratic function returns roots
ground = abs(roots[0]-roots[1])
print("The ball will hit the ground after " + str(ground) + " seconds")
