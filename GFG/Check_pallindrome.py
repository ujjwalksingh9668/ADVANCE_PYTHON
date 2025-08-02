"""
Given a string s, you need to check if it is palindrome or not. A palidrome is a string
that reads the same from front and back....

Examples:
Input: s = "Hello"
Output: false
Explanation: Hello is not equal to olleH so it's not a palindrome.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/check-palindrome--141628
"""

#Solution:-
def isPallindrome(s):
    s = s.replace(" ","").lower()
    if s == s[::-1]:
        return True
    else:
        return False
#Drivers code:-
s = input("enter the string:")
if isPallindrome(s):
    print("True")
else:
    print("False")
