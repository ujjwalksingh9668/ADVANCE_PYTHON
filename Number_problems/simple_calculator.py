#Simple calculator....

#Solution:-
print("1  - Add")
print("2  - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("choose the operation from the above opton: "))

if option in {1,2,3,4}:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))

    if option == 1:
        result= (num1 + num2)
    elif option == 2:
        result= (num1 - num2)
    elif option == 3:
        result= (num1 * num2)
    elif option == 4:
        result= (num1 // num2)
    else:
        print("entered invalid operation")

print("the result of the entered numbers are",result)
