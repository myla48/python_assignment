# Level 2 Task: Count Vowels
# This program counts how many vowels are in a given string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count

user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))