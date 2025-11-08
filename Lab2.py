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

def calc_average(numbers):
    return sum(numbers) / len(numbers)

def find_min_max(numbers):
    return [min(numbers), max(numbers)]

def sort_temperature(temperature_list):
    return sorted(temperature_list)

def calc_median_temperature(temperature_list):
    sorted_list = sorted(temperature_list)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 1:
        # odd number of elements → middle one
        return sorted_list[mid]
    else:
        # even number of elements → average of the two middle
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2

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

