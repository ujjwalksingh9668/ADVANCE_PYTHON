# Write a code in python to print the Floyds triangle...

# Solution...
n = int(input())
num = 1
for row in range(n + 1):
    for col in range(row + 1):
       print(num,end=" ")
       num += 1
    print()
