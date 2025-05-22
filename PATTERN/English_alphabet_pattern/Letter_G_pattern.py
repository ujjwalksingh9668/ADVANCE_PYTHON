n = int(input())
for row in range(n):
    for col in range(n):
        if col == 0:
            print("*",end=" ")
        elif (row == 0 or row == n - 1):
            print("*",end=" ")
        elif (row == n//2 and col >= n//2):
            print("*",end=" ")
        elif (col == n - 1 and (row >= n // 2 or row == 0)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

