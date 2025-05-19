"""
Given a non-negative integer n, your task is to find the nth Fibonacci number.
The Fibonacci sequence is a sequence where the next term is the sum of the previous two
terms. The first two terms of the Fibonacci sequence are O followed by 1. The Fibonacci
sequence: O, I, I, 2, 3, 5, 8. 13. 21
The Fibonacci sequence is defined as follows:
• F(n)
Examples :
        Input: n = 5
        Output: 5
        1) + F(n - 2) for n > 1
        Explanation: The 5th Fibonacci number is 5.
"""
# https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?page=1&category=Mathematical&sortBy=submissions

# Solution:-
def nthFibonacci(n):
    # code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
# Drivers code:-
n = int(input())
if n < 0:
    print("please enter a positive number")
else:
    print(nthFibonacci(n))



