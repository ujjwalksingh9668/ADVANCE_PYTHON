"""
Given two strings denoting non-negative numbers sl and s2. Calculate the sum of sl
and s2.

Examples:
Input: sl="25", s2=23
output: "48"
Explanation: The sum of 25 and 23 is 48.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day5/problem/sum-of-numbers-or-number1219
"""

#Solution:-
def findSun(s1,s2):
    i,j = len(s1) - 1,len(s2) - 1
    carry = 0
    result = []
    while i >= 0 or j >= -0 or carry:
        if i >= 0:
            digit1 = int(s1[i])
        else:
            return 0
        if j >= 0:
            digit2 = int(s2[j])
        else:
            return 0
        total = digit1 +digit2 +carry
        carry = total // 10
        result.append(str(total % 10))
        i -= 1
        j -= 1
    sum_str = "".join(result[::-1]).lstrip("0")
    return sum_str if sum_str else 0
#Drivers code:-
s1 = input("enter the first string: ")
s2 = input("enter the second string: ")
print(findSun(s1,s2))
