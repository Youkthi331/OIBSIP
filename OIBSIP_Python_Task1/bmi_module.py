# bmi_module.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI rounded to 2 decimals."""
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    """Return category string for given BMI."""
    if bmi < 18.5:
        return "Underweight"
    if 18.5 <= bmi < 25:
        return "Normal weight"
    if 25 <= bmi < 30:
        return "Overweight"
    return "Obesity"
