"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
"""

def reverse_integer(n):
    if n > 0:
        reverse = str(n)[::-1]
        return int(reverse)
    else:
        reverse = "-" + str(abs(n))[::-1]
        return int(reverse)
    
print(reverse_integer(70))    
