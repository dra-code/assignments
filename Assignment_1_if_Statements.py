# Assignment - 1 (if-Statements)
# Objectives:
# To improve your conditional algorithm and string operations skills.
# Write your Python codes on any IDE, push it up to your GitHub repository and submit your GitHub Page link address in addition to your code as a plain text.

# Task : Let's say you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
# Write a program that 

# Takes the first name from the user and compares it to yours,
# Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
# If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

first_name = input('Enter your first name to recover your password: ')
password = 'auz54FwEr23'
if first_name == 'Turgut':
    print(f'Hello, {first_name}! The Password is : {password}')
else:
    print(f'Hello, {first_name}! See you later.')