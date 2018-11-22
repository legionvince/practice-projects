# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user


def main():
    user_input = input("Enter a number: ")

    try:
        a = (int(user_input) % 2)

        if a == 0:
            print(user_input + " is an even number!")
        else:
            print(user_input + " is an odd number")
    except ValueError:
        print("Sorry, input is unsupported. Please try again.")
        main()


main()


