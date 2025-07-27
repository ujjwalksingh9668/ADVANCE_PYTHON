"""
Given a string s, and a pattern p. You need to find if p exists in s or not and return the
starting index of p in s. If p does not exist in s then -1 will be returned.
Here p and s both are case-sensitive.

Examples:
Input: s = "Hello", p
= "110"
Output: 2
Explanation:
110 starts from the second index in Hello.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/find-pattern--141628
"""

#Solution:-
def findPattern(s,p):
    return s.find(p)
#Drivers code:-
s = input("enter the main string: ")
p = input("enter the pattern (p): ")
index = findPattern(s,p)
print(index)
