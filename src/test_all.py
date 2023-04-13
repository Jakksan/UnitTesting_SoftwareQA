import BMI
import pytest
import numpy

@pytest.mark.parametrize("feet, inches, pounds, finalBMI", [(5, 10, 250, 35.9), (5, 3, 125, 22.1)])
def test_findBMI(feet, inches, pounds, finalBMI, round_to_decimal=1):
    # This will be a checklist test, since it applies better than a boundary test for this situation.
    # Valid input is assumed, as it will be cleaned when it's read in
    print("Test that our function for finding BMI works...")
    
    # Inputs: 5'10" & 130lbs give us the rounded output: 18.65
    passed = False
    BMI_calculated = BMI.findBMI(pounds, feet, inches)
    
    assert BMI_calculated > 0 # BMI cannot be zero or negative
    assert round(BMI_calculated, round_to_decimal) == round(finalBMI, round_to_decimal)


##### Figure out what our test values should be ######
BMI_boundary_points = [18.5, 25, 30]
test_points = [20, 27] # start with our interior points
# NOTE: The following only works because each of our boundary 
# points is included in it's sub-domain.
for point in BMI_boundary_points:
    # print("ON:  " + str(point)) # boundary point
    smallest_increment = numpy.nextafter(point,point-1) # smallest possible increment of boundary point
    # print("OFF: " + str(smallest_increment))
    test_points.append(point)
    test_points.append(smallest_increment)
test_points.sort()

classification_oracle = ["Underweight", "Normal Weight", "Normal Weight", "Normal Weight", "Overweight", "Overweight", "Overweight", "Obese"] # expected vals of BMI_classifications
print(test_points)
print(classification_oracle)
val_oracle_tuples = []
for i in range(0, len(classification_oracle)):
    val_oracle_tuple = (test_points[i], classification_oracle[i])
    val_oracle_tuples.append(val_oracle_tuple)

@pytest.mark.parametrize("body_mass_index, oracle_classification", val_oracle_tuples)
def test_classifyBMI(body_mass_index, oracle_classification):
        # Sub-Domains:     (-inf, 18.5), [18.5, 25), [25, 30), [30, inf)
        # Classifications:    Under,        Normal,     Over,    Obese
        calculated_classification = BMI.classifyBMI(body_mass_index)
        assert calculated_classification == oracle_classification

            
# def test_BMI_calc(feet, inches, pounds, finalBMI):
#     test = BMI.BMI_calc(feet, inches, pounds)
#     test.findBMI()
#     test.findBMI_test()
#     print(test.return_BMI())
#     assert round(test.return_BMI(), 1) == round(finalBMI, 1)

# def test_BMI_classify():
#     test2 = BMI.BMI_classify(19)
#     assert test2.test_classifyBMI() == "passed"