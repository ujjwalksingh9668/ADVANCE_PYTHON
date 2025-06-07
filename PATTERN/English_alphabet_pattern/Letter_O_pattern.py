# python code to print the English alphabet "O"...

# Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0 and row !=0 and row != n - 1:
            print("*",end=" ")
        elif row == 0 and col != 0 and col != n - 1:
            print("*",end=" ")
        elif row == n - 1 and col != 0 and col != n - 1:
            print("*",end=" ")
        elif col == n - 1 and row != 0 and row != n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
