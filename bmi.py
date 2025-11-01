def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    # CALCULATE BMI
    bmi = weight / (height ** 2)
    # PRINT BMI
    print("Your BMI is : ", float(bmi))
    # BMI classification
    if bmi < 18.5:
        print("You are Under weight")
    elif bmi <= 25.0:
        print("You are Normal weight")
    else: 
        print("You are Over weight")
calculate_bmi(weight=80, height=1.73)