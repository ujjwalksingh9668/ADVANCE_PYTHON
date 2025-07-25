"""
Given a positive integer n, find the number of perfect squares that are less than n in the
sample space of perfect squares.
"""
#https://www.geeksforgeeks.org/problems/count-squares3649/1?page=1&category=Mathematical&sortBy=submissions

#Solution:-
import math
n = int(input())
a = int(math.sqrt(n-1))
print(a)


