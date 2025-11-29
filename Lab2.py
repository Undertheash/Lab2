import math
print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    # Step 1: Read user input
    user_input = input("Enter numbers: ")   
    # Step 2: Split input string into a list of strings
    input_list = user_input.split(",")
    # Step 3: Convert list of strings to list of floats
    float_list = [float(num) for num in input_list]
    # Step 4: Return the list of floats
    return float_list

def calc_average(input):
    print("calc_average")
    sum = 0
    for item in input:
        sum += item 
    return sum/len(input)

def find_min_max(input):
    print("find_min_max")
    min = input[0]
    max = input[0]
    for item in input: 
        if item < min:
            item = min
        if item > max: 
            max = item 
    return [min,max]

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature(input):
    print("calc_median_temperature")
    input=sort_temperature(input)
    if len(input)%2:
        return input[math.floor(len(input)/2)]
    else:
        upper=math.floor(len(input)/2)
        return (input[upper]+input[upper-1])/2   

def calc_average_temperature(temperature_list):
    # Calculate the average temperature
    average = sum(temperature_list) / len(temperature_list)
    return average


def calc_min_max_temperature(temperature_list):
    # Find minimum and maximum temperature
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)
    # Return both values in a list [min, max]
    return [min_temp, max_temp]

temperatures = [30.5, 32.0, 28.7, 31.2]
avg = calc_average_temperature(temperatures)
min_max = calc_min_max_temperature(temperatures)
print("Average temperature:", round(avg, 2))
print("Min and Max temperatures:", min_max)
display_main_menu()
numbers = get_user_input()
print("Numbers entered:", numbers)