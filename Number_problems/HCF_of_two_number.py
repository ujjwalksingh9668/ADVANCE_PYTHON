# HCF of two number
      
#Solution:-
def Compute_hcf(x,y):
    smaller = 0
    if x<y:
        smaller = x
    else:
        smaller = y
    HCF = 0
    for i in range(1,smaller+1):
        if (x % i==0) and (y % i == 0):
            HCF = i
    return HCF


number1 = int(input("enter the first number: "))
number2 = int(input("entert the second number: "))

print("the hcf of of 2 number is",Compute_hcf(number1,number2))
