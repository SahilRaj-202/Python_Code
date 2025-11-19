#-write a program to display the reverse  of the number entered--#
num=int(input("Enter a number : "))
rev=0
x=num
rem=0
while num>0:
    rem=num%10
    num=num//10
    rev=rev*10+rem

print("The reverse of a entered number ",x," is",rev)
