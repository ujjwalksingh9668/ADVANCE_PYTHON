# python code to print the English alphabet "M"...

# Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0 or col == n - 1:
            print("*",end=" ")
        elif row == col and row <= n // 2:
            print("*",end=" ")
        elif row + col == n - 1 and row <= n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
