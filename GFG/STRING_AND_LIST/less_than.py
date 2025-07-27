"""
You are given a number k and a list arr[] that contains integers. You need to return list
Of numbers that are less than k.
Examples:

Input: arr[] = [54, 43, 2, 1, 5], k = 6
Output: 2 1 5
Explanation: 2 1 5 are less than 6.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day4/problem/less-than
"""

#Solution:-
def lessThan(arr,k):
    ans = []
    for i in arr:
        if i < k:
            ans.append(i)
    return ans
#Drivers code:-
arr = list(map(int, input("Enter teh element in the array that are separated by space").split()))
k = int(input("enter the value of k:"))
result = lessThan(arr,k)
print(result)
