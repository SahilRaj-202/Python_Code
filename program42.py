#-write a program to check the number is amstrong or not-#
num1=int(input("enter a Number : "))
sum=0
x=num1
while num1>0:
    d=num1%10
    num1=num1//10
    sum=sum+(d*d*d)

if sum==x:
    print("the number ",x," is armstrong number ")
else:
    print("the number ",x," is not armstrong number ")
