"""
You are familiar with most Of the properties Of dictionaries in Python. Let's get this
into head by solving a problem.
The task is to do operations as described below:
• k key, v value: Insert given key k and value v in the dictionary, print
'Inserted' after inserting.
• d key: Delete the entry for a given key d and print 'Deleted' if the key to be
deleted is present, else print
• p key: Print marks Of given key p in statement as "Marks Of {student_name) is :
(marks)". If key is not present print '-1'.

https://www.geeksforgeeks.org/batch/da-skill-up/track/su-da-day5/problem/implement-dictionary-in-python--172954
"""

#Solution:-
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

my_dict[k] = int(v)
print("Inserted")

d = input()

if d in my_dict:
    del my_dict[d]
    print("Deleted")
else:
    print("-1")

p = input()

if p in my_dict:
    print(f"Marks of {p} is {my_dict[p]}")
else:
    print("-1")
