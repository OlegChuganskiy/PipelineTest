from bmi_calculator import calculate_bmi

def test_calculate_bmi_normal_case():
    assert calculate_bmi(70, 1.75) == 22.86  # Normal BMI (approximate value)

def test_calculate_bmi_underweight():
    assert calculate_bmi(50, 1.75) < 18.5

def test_calculate_bmi_obese():
    assert calculate_bmi(100, 1.75) > 30