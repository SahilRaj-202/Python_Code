#--write a program the prompt a user to enter four numbers and find the greater nuber among the four number entered--#
num1=int(input("Enter a 1st Number : "))
num2=int(input("Enter a 2nd Number : "))
num3=int(input("Enter a 3rd Number : "))
num4=int(input("Enter a 4th Number : "))
sum=num1+num2+num3+num4
for i in range(sum):
    if(i==num1 or i==num2 or i==num3 or i==num4):
        large=i
print("The Large Number is ",large)
print("The Sum of Four Number is ",sum)