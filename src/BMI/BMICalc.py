def findBMI(weight, feet, inches, round_to_decimal=-1):
    weight = weight
    feet = feet
    inches = inches
    try:
        weight = float(weight)
        feet = float(feet)
        inches = float(inches)
    except:
        return("Invalid Input.")

    BMI = ( 703*weight ) / (( (feet*12) + inches)**2)
    if(round_to_decimal > -1):
        BMI = round(BMI, round_to_decimal)
    return(BMI)

def classifyBMI(BMI=-1):
    BMI_used = BMI # default to internally stored BMI
    classification = ""
    try:
        BMI_used = float(BMI_used)
    except:
        return("Invalid Input.")
    
    if(BMI > 0):
        BMI_used = BMI # use provided BMI if it's valid
    else:
        return("Invalid Input.")

    if (BMI_used < 18.5):
        classification = "Underweight"
    elif (BMI_used >= 18.5 and BMI_used < 25):
        classification = "Normal Weight"
    elif (BMI_used >=25 and BMI_used < 30):
        classification = "Overweight"
    elif (BMI_used >= 30):
        classification = "Obese"
    
    return(classification)
    