"""
Your task is to create a Person class in Python that demonstrates encapsulation. This
class should have two "private" attributes:
• name (String) with a default value of "Geeks".
• age (int) with a default value of 10.
The class should provide public methods to access and modify these private
attributes:
• Getter and
• Setter Methods: and


Example:
Input: Funtion calls: [Person().
get—age()]
Output: Geeks John 21
Explanation:
person = Person() // Person Object Created
person.get_name() // Default value "Geeks" returned
person.set_name("John") // name value set to "John"
person.set_age(21) // age value set to 21
person.get_name() // "John" returned
// 21 returned

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day6/problem/encapsulation-in-python
"""

#Solution:-
class Person:
    def __init__(self):
        self.__name = "Geeks"  # Private attribute
        self.__age = 10        # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age


# Drives code:-
p = Person()
print(p.get_name())  # Output: Geeks

p.set_name("John")
p.set_age(21)

print(p.get_name(), p.get_age())  # Output: John 21
