"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
# https://leetcode.com/problems/two-sum/description/

# Solution:-
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in d:
                return [d[x], i]
            d[nums[i]] = i
        return []

# Driver code
nums = list(map(int, input("Enter the list of numbers (space-separated): ").split(",")))
target = int(input("Enter the target sum: "))

solution = Solution()
result = solution.twoSum(nums, target)

if result:
    print("Indices of elements that sum to target:", result)
else:
    print("No two elements sum to the target.")
