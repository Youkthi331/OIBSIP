# tests.py
import pytest
from bmi_module import calculate_bmi, bmi_category

def test_calculate_bmi_basic():
    assert calculate_bmi(60, 1.6) == round(60 / (1.6**2), 2)

def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.7)
    with pytest.raises(ValueError):
        calculate_bmi(-10, 1.7)
    with pytest.raises(ValueError):
        calculate_bmi(50, 0)

def test_bmi_category():
    assert bmi_category(17) == "Underweight"
    assert bmi_category(22) == "Normal weight"
    assert bmi_category(27) == "Overweight"
    assert bmi_category(32) == "Obesity"
