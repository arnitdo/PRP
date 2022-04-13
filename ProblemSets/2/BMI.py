userHeight = int(input("Enter your height (cm) : "))
userWeight = int(input("Enter your weight (kg) : "))

heightMetres = userHeight / 100
userBMI = (userWeight / (heightMetres * heightMetres))

print("Your BMI is :", userBMI)

if userBMI < 18.5:
    print("You are underweight")
elif userBMI < 25:
    print("You are healthy")
elif userBMI < 30:
    print("You are overweight")
else:
    print("You are obese")
