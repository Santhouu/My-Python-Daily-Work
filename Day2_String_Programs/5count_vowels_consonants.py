# Program to count vowels and consonants in a string

string = "Python Full Stack Developer"
vowels = "aeiouAEIOU"

# Initialize counters
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():  # Check if character is an alphabet
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
