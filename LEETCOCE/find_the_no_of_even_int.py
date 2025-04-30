"""
Q- Given an array nums of integers,
return how many of them contain an even number of digits.
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30
"""

# Solution:-
def find_number(nums):
    count = 0
    for num in nums:
        # Count digits in the number
        digit_count = len(str(abs(num)))
        # Check if the number of digits is even
        if digit_count % 2 == 0:
            count += 1
    return count

# Get input as a list of integers
input_str = input("Enter numbers separated by space: ")
nums = [int(x) for x in input_str.split(",")]
print(find_number(nums))
