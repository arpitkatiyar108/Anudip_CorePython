#1. Python program to check if a given number is an Armstrong number
num = int(input())
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
