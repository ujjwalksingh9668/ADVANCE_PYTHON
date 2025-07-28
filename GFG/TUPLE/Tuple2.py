"""
You are given a tuple numbers that contains a A.P sequence integer. You need to
calculate the next three sequences of numbers and return the whole sequence in a
tuple.

Examples:
Input: tup = ( 1, 5, 9, 13, 17)
Output: 1 5 9 13 17 21 25 29
Explanation: It's an increasing sequence by 4. So, the next three numbers
are 17+4= 21, 21+4=25, 25+4=29.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day5/problem/tuple-2
"""

#Solution:-
def sequence(tup):
    common_diff =tup[1] - tup[0]
    result = list(tup)
    for i in range(3):
        next_value = result[-1] + common_diff
        result.append(next_value)
    return tuple(result)
#Drivers code:-
user_input = input("enter the elements separated by space: ")
value = list(map(int , user_input.split()))
print(sequence(value))
