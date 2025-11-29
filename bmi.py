def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight)) # str() converts non-string data types (like float or int) into strings.
    # CALCULATE BMI
    bmi = weight / (height ** 2)
    # PRINT BMI
    print("Your BMI is : ", float(bmi))
    # BMI classification
    if bmi < 18.5:
        print("You are Under weight")
        return -1
    elif bmi <= 25.0:
        print("You are Normal weight")
        return 0
    else: 
        print("You are Over weight")
        return 1
calculate_bmi(weight=40, height=1.73)