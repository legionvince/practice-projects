from math import *


def addition():
    """
    Adds 2 numbers together.
    :return:
    """
    a = (input("Enter the first number: "))
    b = (input("Enter the second number: "))
    equation = a + ' + ' + b + ' ='
    print(equation)
    ans = float(a) + float(b)
    print(ans)


def subtraction():
    """
    subtracts 2 numbers.
    :return:
    """
    a = (input("Enter the first number: "))
    b = (input("Enter the second number: "))
    equation = a + ' - ' + b + ' ='
    print(equation)
    ans = float(a) - float(b)
    print(ans)


def multiplication():
    """
    multiplies 2 numbers together.
    :return:
    """
    a = (input("Enter the first number: "))
    b = (input("Enter the second number: "))
    equation = a + ' x ' + b + ' ='
    print(equation)
    ans = float(a) * float(b)
    print(ans)


def division():
    """
    divides 2 numbers.
    :return:
    """
    a = (input("Enter the first number: "))
    b = (input("Enter the second number: "))
    equation = a + ' / ' + b + ' ='
    print(equation)
    ans = float(a) / float(b)
    print(ans)


def power_expo():
    """
     does: a^b
    :return:
    """
    a = (input("Enter the base: "))
    b = (input("Enter the exponent: "))
    equation = a + ' ^ ' + b + ' ='
    print(equation)
    ans = float(a) ** float(b)
    print(ans)


def log():
    """
     log base a of b (roots)
    :return:
    """
    a = (input("Enter the base: "))
    b = (input("Enter the number you would like to take the lod of: "))
    equation = "Log base " + a + "of " + b + "="
    print(equation)
    ans = log(float(b),float(a))
    print(ans)

def square_root():
    """
     square root
    :return:
    """
    a = (input("Enter the number: "))
    # b = eval(input("Enter the exponent: "))
    equation = a +"^(1/2) ="
    print(equation)
    ans = float(a)**(1/2)
    print(ans)


def cube_root():
    """
     cube root
    :return:
    """
    a = (input("Enter the number: "))
    # b = eval(input("Enter the exponent: "))
    equation = a + "^(1/3) ="
    print(equation)
    ans = float(a) ** (1 / 3)
    print(ans)


def sin_a():
    """
     returns the sin of a
    :return:
    """
    a = (input("Enter the number: "))
    # b = eval(input("Enter the exponent: "))
    equation = "sin("+a+") ="
    print(equation)
    ans = sin(float(a))
    print(ans)


def cos_a():
    """
     returns the cos of a
    :return:
    """
    a = (input("Enter the number: "))
    # b = eval(input("Enter the exponent: "))
    equation = "cos("+a+") ="
    print(equation)
    ans = cos(float(a))
    print(ans)


def tan_a():
    """
     returns the tan of a
    :return:
    """
    a = (input("Enter the number: "))
    # b = eval(input("Enter the exponent: "))
    equation = "tan("+a+") ="
    print(equation)
    ans = tan(float(a))
    print(ans)

