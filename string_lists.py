# Ask the user for a string and print
# out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Enter a word: "))

reverse_word = word[::-1]

print("You entered: " + word)
print("The reverse of your entry is: " + reverse_word)

if word == reverse_word:
    print(word + " is a palindrome!")
else:
    print(word + " is not a palindrome!")