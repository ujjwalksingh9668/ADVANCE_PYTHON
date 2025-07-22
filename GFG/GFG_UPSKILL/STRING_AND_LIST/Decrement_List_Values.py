"""
You are given a list that contains integers. You need to decrement each element Of the
list by 1 and return the list.

Input: arr = [54, 43, 2, 1, 5]
Output: 53 42 1 0 5
Explanation: Just decrement the numbers by 1.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/decrement-list-values
"""

#Solution:-
def decrementList(arr):
#code here
    return [x- 1 for x in arr]
#Drivers code:-
number = [54, 43, 2, 1, 5]
result = decrementList(number)
print(result)
