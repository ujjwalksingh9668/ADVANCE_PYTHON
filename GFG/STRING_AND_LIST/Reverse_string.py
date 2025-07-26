"""
Given a string s, you need to reverse it.

Examples:
Input s = "Hellot'
Output: "olleH"
Explanation: Reverse Of Hello is olleH

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/reverse-string--141628
"""

#Solution:-
def reverseString(s):
    new_str = s[::-1]
    return new_str
#Drivers code:-
s = input("enter thr string that you want to reverse: ")
print(reverseString(s))
