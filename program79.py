#write a program to find the factorial of a number
def printFact():
    num=5
    fact=1
    for i in range(1,num+1):
        fact=fact*i;
    return fact;

print("The factorial is ",printFact())