"""
Design a class as described below:
• Class Name: Addition
• Method.
function name: add
Parameters: a (int), b (int)
Return Type: int
Static: Yes (Use the @staticmethod decorator)
Task: Returns the sum Of the values given as parameters.

Examples:
Input: a = 4, b = 3
Output 7
Function Name: add
Parameters: a (int), b (int)
Return Type: int
Static: Yes (Use the @staticmethod decorator)
Task: Returns the sum of the values given as parameters.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day6/problem/static-method-in-python
"""

#Solution:-
def add(a:int,b:int) -> int:
    return a + b
#Drivers code:-
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
print(add(a,b))
