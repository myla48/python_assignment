# Level 1 Task: Reverse a String
# This program takes a string input from the user and prints the reversed version.
def reverse_string(text):
    return text[::-1]

user_input = input("Enter a string: ")
print("Reversed:", reverse_string(user_input))