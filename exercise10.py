
weight = float(input("Enter your weight in Kg:"))
height = float(input("Enter your height in meter:"))

bmi = round(weight / height **2)
print((bmi))

if bmi >= 40.0:
    print(f"Your BMI is {bmi} and you have Obesity (Obese- Class III)")
else:
    if bmi < 16.0:
        print(f"Your BMI is {bmi} and you are underweight (Severe thinness).")
    elif bmi < 17.0:
        print(f"Your BMI is {bmi} and you are underweight (Moderate thinness).")
    elif bmi < 18.5:
        print(f"Your BMI is {bmi} and you are underweight (Mild thinness).")
    elif bmi < 25.0:
        print(f"Your BMI is {bmi} and you have normal weight.")
    elif bmi < 30.0:
        print(f"You BMI is {bmi} and you are overweight (Pre-obese)")
    elif bmi < 35.0:
        print(f"Your BMI is {bmi} and you have Obesity (Obese- Class I)")
    elif bmi < 40.0:
        print(f"Your BMI is {bmi} and you have Obesity (Obese- Class II)")
    else:
        print("Invalid input!")

