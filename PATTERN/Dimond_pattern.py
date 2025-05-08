# python program to print the diamond pattern...

# Solution:-
num = int(input("enter the number of rows: "))
#upper part:-
for i in range(1,num + 1):
    print(" " * (num - i), end="")
    for j in range(1,2*i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ",end="")
    print()
#lower part:-
for i in range(num - 1, 0 , -1):
    print(" " * (num - i), end="")
    for j in range(1,2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ",end="")

    print()
