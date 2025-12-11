# main.py
from bmi_module import calculate_bmi, bmi_category

def get_float(prompt):
    while True:
        try:
            raw = input(prompt).strip()
            value = float(raw)
            if value <= 0:
                print("Enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a number like 60 or 1.65.")

def main():
    print("=== BMI Calculator ===")
    print("Enter weight in kilograms and height in meters.")
    weight = get_float("Weight (kg): ")
    height = get_float("Height (m): ")
    try:
        bmi = calculate_bmi(weight, height)
    except ValueError as e:
        print("Error:", e)
        return
    category = bmi_category(bmi)
    print(f"\nYour BMI: {bmi}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
