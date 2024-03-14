"""
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.
"""

num1 = 0
num2 = 1

while num1 <= 100:
    print(num1)
    num1, num2 = num2, num1 + num2

    