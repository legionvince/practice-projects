# generates 2 lists
# prints a new list which contains
# elements which are common in both lists

import random

a = range(1, random.randint(1, 20))
b = range(1, random.randint(15, 50))

new_list = []

for num in a:
    if num in b:
        new_list.append(num)

print("The numbers in list A are: " + str(a))
print("The numbers in list B are: " + str(b))

print("The numbers which appear in both lists are: ")
print(new_list)
