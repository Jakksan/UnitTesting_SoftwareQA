import numpy

class BMI_calc:
    def __init__(self, feet=0, inches=0, weight=0):
        self.feet = feet
        self.inches = inches
        self.weight = weight
        self.BMI = -1

    def findBMI(self):
        self.BMI = ( 703*self.weight ) / (( (self.feet*12) + self.inches)**2)
        return(self.BMI)

    def findBMI_test(self):
        # This will be a checklist test, since it applies better than a boundary test for this situation.
        # Valid input is assumed, as it will be cleaned when it's read in
        print("Test that our function for finding BMI works...")
        # BMI cannot be zero or negative
        # Inputs: 5'10" & 130lbs give us the rounded output: 18.65

        if (self.BMI > 0):
            print("findBMI: Test 1 Passed. BMI Greater than 0")
        else:
            print("findBMI: Test 1 Failed. BMI less than or equal to zero.")
        
        tmp_BMI = self.BMI # Save vals so we can change back after the test
        tmp_feet = self.feet 
        tmp_inches = self.inches 
        tmp_weight = self.weight
        self.feet = 5
        self.inches = 10
        self.weight = 130
        self.findBMI()
        if (round(self.BMI, 2) == 18.65):
            print("findBMI: Test 2 Passed. Function works as expected given preset inputs")
        else:
            print("findBMI: Test 2 Failed. Function did not perform as expected given preset inputs")
        self.BMI = tmp_BMI
        self.feet = tmp_feet
        self.inches = tmp_inches
        self.weight = tmp_weight

    def return_BMI(self):
        return self.BMI
        
class BMI_classify:
    def __init__(self, BMI=-1):
        self.BMI = BMI
        self.classification = ""

        

    def classifyBMI(self, BMI=-1):
        BMI_used = self.BMI # default to internally stored BMI
        if(BMI > 0):
            BMI_used = BMI # use provided BMI if it's valid
            self.BMI = BMI # set internal BMI to new BMI

        if (BMI_used < 18.5):
            self.classification = "Underweight"
        elif (BMI_used >= 18.5 and BMI_used < 25):
            self.classification = "Normal Weight"
        elif (BMI_used >=25 and BMI_used < 30):
            self.classification = "Overweight"
        elif (BMI_used >= 30):
            self.classification = "Obese"
        
        return(self.classification)

    def classifyBMI_test(self):
        # Sub-Domains:     (-inf, 18.5), [18.5, 25), [25, 30), [30, inf)
        # Classifications:    Under,        Normal,     Over,    Obese
        BMI_boundary_points = [18.5, 25, 30]
        BMI_test_points = [20, 27] # start with our interior points
        # NOTE: The following only works because each of our boundary 
        # points is included in it's sub-domain.
        for point in BMI_boundary_points:
            # print("ON:  " + str(point)) # boundary point
            smallest_increment = numpy.nextafter(point,point-1) # smallest possible increment of boundary point
            # print("OFF: " + str(smallest_increment))
            BMI_test_points.append(point)
            BMI_test_points.append(smallest_increment)
        BMI_test_points.sort()
        classification_oracle = ["Underweight", "Normal Weight", "Normal Weight", "Normal Weight", "Overweight", "Overweight", "Overweight", "Obese"] # expected vals of BMI_classifications
        
        print("\nClassify BMI test:")
        # feed each test point to classifyBMI function
        test_classifications = []
        for test_point in BMI_test_points:
            print(test_point)
            test_classifications.append(self.classifyBMI(test_point))

        point_count = len(BMI_test_points)
        # check against oracle for each point
        for i in range(0,point_count):
            test_passed = "failed"
            if(test_classifications[i] == classification_oracle[i]):
                test_passed = "passed"

            print(str(i)+": "+ test_passed + " -- " + str(BMI_test_points[i]))

def runTests():
    test = BMI_calc(1, 2, 3)
    test.findBMI()
    test.findBMI_test()
    print(test.return_BMI())

    test2 = BMI_classify(19)
    test2.classifyBMI_test()

### Command Line interface ###
def GetMeasurements():
    input_valid = False
    print("In the following three prompts enter height in feet, then inches, then enter weight")
    feet, inches, weight = "", "", ""
    while (input_valid == False):
        feet = input("Enter feet: ")
        if ( (not feet.isnumeric()) ):
            print("Invalid. Try again.\n")
            continue

        inches = input("Enter inches: ")
        if ( (not inches.isnumeric())):
            print("Invalid. Try again.\n")
            continue

        weight = input("Enter weight in pounds: ")
        if ( not weight.isnumeric() ):
            print("Invalid. Try again.\n")
            continue

        if (float(feet)*12 + float(inches) > 0 and float(weight) > 0):
            break
        else:
            print("Please input valid measurements.")
    
    feet = float(feet)
    inches = float(inches)
    weight = float(weight)
    measurements = (feet, inches, weight)
    return(measurements)

def GetBMI():
    measurements = GetMeasurements()
    BMI_calculator = BMI_calc(measurements[0], measurements[1], measurements[2])
    BMI = BMI_calculator.findBMI()
    BMI_classifier = BMI_classify(BMI)
    classification = BMI_classifier.classifyBMI()
    print(round(BMI,3),":",classification)


# runTests()
GetBMI()