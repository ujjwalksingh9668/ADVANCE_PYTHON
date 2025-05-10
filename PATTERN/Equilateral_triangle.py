# using python printing equilateral triangle...

# Solution:-
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

#reverse of the equilateral triangle...
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
