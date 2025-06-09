# python code to print the English alphabet "P"...

# Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0:
            print("*",end=" ")
        elif row == 0 or row == n // 2:
            print("*",end=" ")
        elif col == n - 1 and row != 0 and row != n // 2 and row <= n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
