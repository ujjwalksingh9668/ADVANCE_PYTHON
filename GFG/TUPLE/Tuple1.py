"""
You are given a tuple numbers that contains integers. You need to return a tuple
containing doubles Of given numbers...

Examples:
Input: tup = (4, 5, 1, 2, 3, 5)
Output: 8 10 2 4 6 10
Explanation: multiplied numbers by 2.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day5/problem/tuple-1
"""

#Solution:-
def doubleTuple(numbers):
    return tuple(x * 2 for x in numbers)
#Drivers code:-
user_input = input("enter the number seperated by space: ")
number = tuple(map(int, user_input.split()))
print(doubleTuple(number))
