#--write a program to find the factorial of a number
def fact(num1):
    fact=1;
    for i in range(1,num1+1):
        fact=fact*i
    print("The factorial of number ",num1," is=",fact)

fact(5)
