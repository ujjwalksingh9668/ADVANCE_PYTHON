# palindrome number

#Solution:-
num = int(input("enter the number"))
lenght = len(str(num))
temp = num
sum = 0
while temp >0:
    digit = temp%10
    sum += digit**lenght
    temp=temp//10

if sum==num:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")


