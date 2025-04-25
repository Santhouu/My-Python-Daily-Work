# Program to check if a string is a palindrome

# A palindrome is a word that reads the same forward and backward

word = "madam"

# Reverse the word using slicing
reversed_word = word[::-1]

# Check if the original and reversed words are the same
if word == reversed_word:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
