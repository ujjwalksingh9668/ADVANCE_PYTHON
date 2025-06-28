# python code to print the English alphabet "T"...

#Solution:-
n = int(input())
for row in range(n):
    for col in range(n):
        if row == 0:
            print("*",end=" ")
        elif col == n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
