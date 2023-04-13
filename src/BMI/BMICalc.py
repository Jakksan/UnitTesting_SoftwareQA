import numpy
import pytest

def findBMI(weight, feet, inches):
    BMI = ( 703*weight ) / (( (feet*12) + inches)**2)
    return(BMI)

def classifyBMI(BMI=-1):
    BMI_used = BMI # default to internally stored BMI
    classification = ""

    if(BMI > 0):
        BMI_used = BMI # use provided BMI if it's valid
        BMI = BMI # set internal BMI to new BMI
    else:
        return(classification)

    if (BMI_used < 18.5):
        classification = "Underweight"
    elif (BMI_used >= 18.5 and BMI_used < 25):
        classification = "Normal Weight"
    elif (BMI_used >=25 and BMI_used < 30):
        classification = "Overweight"
    elif (BMI_used >= 30):
        classification = "Obese"
    else:
        classification = "Should not be possible"
    
    return(classification)
    

# class BMI_classify:
#     def __init__(self, BMI=-1):
#         self.BMI = BMI
#         self.classification = ""

        



    

# defines arguments to pass into test_CalcBMI

### Command Line interface ###
# def GetMeasurements():
#     input_valid = False
#     print("In the following three prompts enter height in feet, then inches, then enter weight")
#     feet, inches, weight = "", "", ""
#     while (input_valid == False):
#         feet = input("Enter feet: ")
#         if ( (not feet.isnumeric()) ):
#             print("Invalid. Try again.\n")
#             continue

#         inches = input("Enter inches: ")
#         if ( (not inches.isnumeric())):
#             print("Invalid. Try again.\n")
#             continue

#         weight = input("Enter weight in pounds: ")
#         if ( not weight.isnumeric() ):
#             print("Invalid. Try again.\n")
#             continue

#         if (float(feet)*12 + float(inches) > 0 and float(weight) > 0):
#             break
#         else:
#             print("Please input valid measurements.")
    
#     feet = float(feet)
#     inches = float(inches)
#     weight = float(weight)
#     measurements = (feet, inches, weight)
#     return(measurements)

# def GetBMI():
#     measurements = GetMeasurements()
#     BMI_calculator = BMI_calc(measurements[0], measurements[1], measurements[2])
#     BMI = BMI_calculator.findBMI()
#     BMI_classifier = BMI_classify(BMI)
#     classification = BMI_classifier.classifyBMI()
#     print(round(BMI,3),":",classification)

# runTests()
# GetBMI()