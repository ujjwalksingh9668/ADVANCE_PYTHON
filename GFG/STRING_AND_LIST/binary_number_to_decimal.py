"""
Given a string b representing a Binary Number, The problem is to find its decimal
equivalent.


Examples:
Input : b = 111
Output : 7
Explanation :
The decimal equivalent of the binary number 111 is 2
1

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/binary-number-to-decimal-number3525
"""

#Solution:-
def binaryToDecimal(b):
    decimal = int(b , 2)
    return decimal
binary_string = input("enter the binary number: ")
decimal_value = binaryToDecimal(binary_string)
print("decimal equivalance: ",decimal_value)
