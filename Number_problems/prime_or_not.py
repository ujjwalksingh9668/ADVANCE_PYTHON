# Q- checking a number is prime or not

# solution
a = int(input("enter the number: "))
for i in range (2,a):
    if a == 1:
        print("it is not a prime number")
    if a%i==0:
        print("it is not a prime number")
else:
    print("it is a prime number")
