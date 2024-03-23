# Ask the user to enter a sentence
str = input("Enter a sentence: ")

# Calculate and display the length of str
length_of_str = len(str)
print("Length of str:", length_of_str)

# Find the last letter in the str sentence
last_letter = str[-1]

# Replace every occurrence of the last letter with '@'
str_replaced = str.replace(last_letter, '@')
print("After replacing every occurrence of the last letter with '@':", str_replaced)

# Print the last 3 characters in str backwards
last_3_chars_backwards = str[-1:-4:-1]
print("Last 3 characters in str backwards:", last_3_chars_backwards)

# Create a five-letter word using the first three and last two characters in str
five_letter_word = str[:3] + str[-2:]
print("Five-letter word made up of the first three and last two characters:", five_letter_word)