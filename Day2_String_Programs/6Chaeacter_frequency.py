# Program to count the frequency of each character in a string

text = "programming"

# Create an empty dictionary to store character counts
frequency = {}

# Count each character
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
