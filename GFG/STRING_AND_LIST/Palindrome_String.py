"""
You are given a string s. Your task is to determine if the string is a palindrome. A string
is considered a palindrome if it reads the same forwards and backwards.

Examples :
Input: s = "abba"
Output: true
Explanation: "abbat• reads the same forwards and backwards, so it is a
palindrome.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/palindrome-string0817
"""

#Solution:-
def isPalindrome(s: str) -> bool:
    s = s.replace(" ","").lower()
    return s == s[::-1]

#Drivers code:-
input_string = input("enter a string: ")
if isPalindrome(input_string):
    print("the string is palindrome")
else:
    print("the string is not palindrome")
