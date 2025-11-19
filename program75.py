# Python Program to find the L.C.M. of two input number
def compute_Lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y

    while(True):
        if ((greater%x==0) and (greater%y==0)):
            Lcm=greater
            break
        greater=greater+1
    return Lcm

num1=int(input("Enter a 1str number "))
num2=int(input("Enter a 2nd number "))
print("The Lcm is ",compute_Lcm(num1,num2))