# Factor of two numbers....

#Solution:-
number = int(input("enter the number: "))

print("the factor of",format(number),"are: ")
for i in range(1,number+1):
    if (number % i == 0):
        print(i)
