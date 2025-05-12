# python code to print the pattern of english alphabet "B"....

#Solution:-
n = int(input("Enter the size of the letter: "))

for row in range(n):
    for col in range(n):
        if (
            col == 0 or
            (row == 0 and col < n-1) or
            (row == n // 2 and col < n - 1) or
            (row == n - 1 and col < n-1) or
            (col == n -1 and row != 0 and row != n // 2 and row != n-1)
        ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
