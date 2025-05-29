# python code to print the English alphabet "C"...

# Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0:
            print("*",end=" ")
        elif row + col == n // 2 or row - col == n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
