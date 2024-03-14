"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
"""

def count_vowels(sentense):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    seen_char = set()
    for char in sentense:
        if char in vowels and char not in seen_char:
            vowel_count += 1
            seen_char.add(char)
    return vowel_count

print(count_vowels("Ronald is a developer"))        
