valid_input = False

while not valid_input:
    weight_input = input("Enter your weight in pounds: ")
    height_input = input("Enter your height in inches: ")

    if weight_input.isdigit() and height_input.isdigit():
        WEIGHT = int(weight_input) * 0.453592
        HEIGHT = int(height_input) * 0.0254
        valid_input = True
    else:
        print("Invalid input. Please enter numerical values.")

bmi = WEIGHT / (HEIGHT * HEIGHT)

print(f"Your BMI is: {bmi:,.2f}")

if bmi < 18.5:
    print("You are in the underweight category.")

elif 18.5 <= bmi < 24.9:
    print("You are in the normal weight category.")

elif 25 <= bmi < 29.9:
    print("You are in the overweight category.")

elif bmi >= 30:
    print("You are in the obese weight category.")
