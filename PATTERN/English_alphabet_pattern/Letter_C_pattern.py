# python code to print the English alphabet "C"...

# solution:-
n = int(input("Enter the size of the C: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
