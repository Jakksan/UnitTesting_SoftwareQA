import BMI
import pytest

@pytest.mark.parametrize("feet, inches, pounds, finalBMI", [(5, 10, 250, 35.9), (5, 3, 125, 22.1)])

def test_BMI_calc(feet, inches, pounds, finalBMI):
    test = BMI.BMI_calc(feet, inches, pounds)
    test.findBMI()
    test.findBMI_test()
    print(test.return_BMI())
    assert round(test.return_BMI(), 1) == round(finalBMI, 1)

def test_BMI_classify():
    test2 = BMI.BMI_classify(19)
    assert test2.test_classifyBMI() == "passed"