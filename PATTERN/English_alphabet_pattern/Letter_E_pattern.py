# python code to print the English alphabet "C"...

# Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0:
            print("*",end=" ")
        elif (row == 0 or (row == n // 2 and col != n - 1) or row == n - 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
