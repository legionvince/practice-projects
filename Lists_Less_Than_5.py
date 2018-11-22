# Take a list
# write a program that prints out all
# the elements of the list that are less than a given number


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_list = []

for i in a:
    if i < num:
        new_list.append(i)

print(new_list)
