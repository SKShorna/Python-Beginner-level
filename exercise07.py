
# BMI- weight in KG and integer
# height in meters and float
# BMI = weight/ height^2
# the result should be in round form

weight = int(input("Enter the weight in Kg:"))
height = float(input("Enter the height in Meters:"))

BMI = int(weight / (height**2))
print("Your BMI is: ", (BMI))
