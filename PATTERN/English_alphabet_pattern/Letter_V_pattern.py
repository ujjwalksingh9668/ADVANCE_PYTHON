# python code to print the English alphabet "V"...

#Solution:-
n= int(input())
for row in range(n):
    for col in range(n * 2 - 1):
        if col == row or col == (n * 2 - 2 - row):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



