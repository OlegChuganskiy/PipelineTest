from main import calculate_bmi

def test_calculate_bmi_normal_case():
    assert calculate_bmi(100, 2) == 25

def test_calculate_bmi_underweight():
    assert calculate_bmi(50, 1.75) < 18.5

def test_calculate_bmi_obese():
    assert calculate_bmi(100, 1.75) > 30