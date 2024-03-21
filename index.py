def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for weight and height.")
        return

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
        return

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
1