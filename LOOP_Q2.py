# Q2. Python program to get the Fibonacci series between 0 to 50
a, b = 0, 1
while a <= 50:
    print(a, end=' ')
    a, b = b, a + b
