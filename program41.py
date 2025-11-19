#--write a program to find the factorial of a number--#
num=int(input("Enter a number :"))
fact=1
ans=1
while fact<=num:
  ans=ans*fact
  fact=fact+1
print("Factorial of ",num," is ",ans)