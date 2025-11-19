#-write a program to test whether a number is divisible by 5 and 10 or 5 by 10-#

num=int(input('Enter  The Number :'))
print('Entered Number :', num)
if (num%5==0 and num%10==0):
    print(num,' is Divisible by Both 5 and 10 ')
elif (num%5==0 or num%10==0):
   print(num,' is Divisible by  5 or 10 ')
else:
    print(num,' is not Divisible by 5 or 10')