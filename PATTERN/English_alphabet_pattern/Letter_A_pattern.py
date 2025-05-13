# python code to print pattern of capital english alphabet "A"...
    
# Solution:-
n = int(input("Enter the height of the letter A: "))

for row in range(n):
    for col in range(n):
        # Condition to print '*':
        if (
            (col == 0 or col == n - 1) and row != 0 or
            (row == n // 2 and (col > 0 and col < n - 1)) or
            (row == 0 and (col > 0 and col < n - 1))
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
