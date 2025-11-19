# Python Program to find the L.C.M. of two input number
num1=int(input("Enter a 1st number :"))
num2=int(input("Enter a 2nd number :"))
if num1>num2:
    greater =num1
else:
    greater=num2

while(True):
    if(greater%num1==0)and(greater%num2==0):
        Lcm = greater
        break
    greater = greater+1
print("The L.C.M. is", Lcm)