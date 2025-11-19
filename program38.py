#-write a program to find the sum of three digits number 123=3+2+1=6--#
num=int(input("Enter a number :"))
x=num
rem=0
sum=0
while num>0:
    rem = num % 10
    num = num //10
    sum = sum + rem
print("The sum of three digit ",x," is ",sum)
