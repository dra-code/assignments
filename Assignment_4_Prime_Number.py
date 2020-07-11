# Task : 
# Write a program that takes a number from the user and prints the result to check if it is a prime number.

num = int(input('Enter a number: '))

n = int(num / 2)
prime = True
for i in range(2, n):
    if num % i == 0:
        prime = False

if num != 2 and num != 4 and prime == True:
    print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')