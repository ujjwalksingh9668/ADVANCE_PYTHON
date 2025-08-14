from abc import ABC, abstractmethod
"""
Implement the following classes to understand abstraction in Python :
Note: Driver code makes all the function calls and print statements
Class Name: Shape (Abstract Class)
Attributes: color (String)
Constructor: Shape(c) -> assign value of c to color attribute
Methods: get_color() returns value of color
get_area() abstract method with float return type
Class Name: Square (extends Shape)
Attributes: side (float)
Constructor: Square(c, side) calls super(c) to initialize the color and
assigns the value to side.
Methods: returns the area Of the square (side side).

Example:
Input: color = "red", side = 50
Output:
red 25.0

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day6/problem/abstraction-in-python
"""

#Solution:-
class Shape(ABC):
    def __init__(self,c:str):
        self.color = c
    def get_color(self) -> str:
        return self.color
    def get_area(self) -> float:
        pass

class Square(Shape):
    def __init__(self,c:str,side:float):
        super().__init__(c)
        self.side = side
    def get_area(self) -> float:
        return self.side * self.side

#Drives code
color = input("enter the color: ")
side = float(input("enter the side: "))
square = Square(color,side)
print(square.get_color())
print(square.get_area())
