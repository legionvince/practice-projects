from functions import *
from time import sleep


def run_calculator():
    """
    runs the calculator
    :return:
    """
    choices_list = ["Addition: 1",
                    "Subtraction: 2",
                    "Multiplication: 3",
                    "Division: 4",
                    "Exponent: 5",
                    "Logarithm: 6",
                    "Square Root: 7",
                    "Cube Root: 8",
                    "Sin: 9",
                    "Cos: 10",
                    "Tan: 11",]
    print("=========================================")
    for item in choices_list:
        print(item)
    print("=========================================")
    """
    command = {1:addition,
            2:subtraction,
            3:multiplication,
            4:division,
            5:power_expo,
            6:log,
            7:square_root,
            8:cube_root,
            9:sin_a,
            10:cos_a,
            11:tan}
    """
    user_input = eval(input("Enter the number of your selection: "))

    if user_input == 1:
        addition()
    elif user_input == 2:
        subtraction()
    elif user_input == 3:
        multiplication()
    elif user_input == 4:
        division()
    elif user_input == 5:
        power_expo()
    elif user_input == 6:
        log()
    elif user_input == 7:
        square_root()
    elif user_input == 8:
        cube_root()
    elif user_input == 9:
        sin_a()
    elif user_input == 10:
        cos_a()
    elif user_input == 11:
        tan_a()
    else:
        print("INVALID INPUT!")

    sleep(2)
    run_calculator()


run_calculator()

