# python code to print the English alphabet "Y"...

#Solution:-
n= int(input())
for row in range(n):
    for col in range(n):
        if row == col and  row <= n // 2:
            print("*",end=" ")
        elif col == n - row - 1 and row <= n // 2:
            print("*",end=" ")
        elif row >= n // 2 and col == n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
