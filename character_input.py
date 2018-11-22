# program that asks the user to
# enter their name and their age.
# Prints out a message addressed to them that tells
# them the year that they will turn 100 years old


def main():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    age_int = int(age)
    year = input("Enter the current year: ")
    year_int = int(year)
    diff = 100 - age_int
    reach_peak = year_int + diff
    reach_age = str(reach_peak)

    print("Your name is " + name)
    print("Your age is " + age)
    print("You will be 100 years old in the year " + reach_age)


main()
