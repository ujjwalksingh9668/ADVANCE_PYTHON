# python code to print the English alphabet "X"...

#Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if row == col:
            print("*",end=" ")
        elif row + col == n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
