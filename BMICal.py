n = int(input("Enter your Height (in cm):"))
w = int(input("Enter your Weight (in kg)"))

met = n/100

BMI = w / (met**2)
print("Your BMI is",BMI)