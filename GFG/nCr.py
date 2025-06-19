# Given two integer values n and r, the task is to find the value of Binomial Coefficient nCr
# https://www.geeksforgeeks.org/problems/ncr1019/1?page=1&category=Mathematical&sortBy=submissions
     
# Solution:-
def fact(n, r):
    if r > n:
        return 0
    result = 1
    r = min(r , n - r)
    for i in range(r):
        result *= n - i
        result //= i + 1
    return result
# Drivers dode:-
n = int(input())
r = int(input())
print(fact(n , r))
