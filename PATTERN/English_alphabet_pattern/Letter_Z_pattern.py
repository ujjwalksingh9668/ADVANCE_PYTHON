# python code to print the English alphabet "Z"...

#Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if row == 0:
            print("*",end=" ")
        elif row + col == n - 1:
            print("*",end=" ")
        elif row == n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
