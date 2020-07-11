# Task : 
# Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

p = 0
l = 1
f = 0
fibo_list = []
while f <= 54:
    f = p + l
    fibo_list.append(f)
    p = l
    l = f

print(fibo_list)