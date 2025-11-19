#write a program to read three number and check which number is greater than in three number .
num1=int(input('Enter a 1st Number :'))
num2=int(input('Enter a 2nd Number :'))
num3=int(input('Enter a 3rd Number'))
if num1 > num2:
    if num2 > num3:
        print(num1 ,' is greater than ',num2,' and ',num3)

else:
    print(num1,' is less than ',num2,' and ',num3)