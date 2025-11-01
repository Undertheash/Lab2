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

def calc_average():
    print("calc_average")

def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")
