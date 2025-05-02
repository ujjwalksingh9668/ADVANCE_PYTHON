"""
Q- Given an integer x, return true if x is a palindrome, and false otherwise.

   Example 1:
       Input: x = 121
       Output: true
       Explanation: 121 reads as 121 from left to right and from right to left.
"""
# https://leetcode.com/problems/palindrome-number/description/

# Solution:-
def Palindrome(number):
    if number < 0:
        return False
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original_number ==reversed_number



# drivers code:-
number = int(input("Enter a number: "))
if Palindrome(number):
    print("True")
else:
    print("False")
