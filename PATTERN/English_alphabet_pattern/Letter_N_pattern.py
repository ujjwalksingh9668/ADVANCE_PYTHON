# python code to print the English alphabet "N"...

#Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0 or col == n - 1:
            print("*",end=" ")
        elif row == col and row <= n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
