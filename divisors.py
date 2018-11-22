# asks for a number and prints a list of divisors of that number


def main():
    a = int(input("Enter a number to divide: "))
    try:
        if a is int:
            pass
    except ValueError:
        print("Input Error!")
        main()
    return a


num = main()

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)

