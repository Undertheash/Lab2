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
    min_val = input[0]
    max_val = input[0]
    for item in input: 
        if item < min_val:
            min_val = item
        if item > max_val: 
            max_val = item 
    return [min_val,max_val]

def sort_temperature(temperature_list):
    return sorted(temperature_list)

def calc_median_temperature(input):
    print("calc_median_temperature")
    input=sort_temperature(input)
    if len(input)%2:
        return input[math.floor(len(input)/2)]
    else:
        upper=math.floor(len(input)/2)
        return (input[upper]+input[upper-1])/2   





