#--write a program to print even numbers form 0 to 10 and find their sum--#
sum=0;
for i in range (0,11,1):
    if(i%2==0):
        print(i)
        sum=sum+i
print("The Sum of Even Number is :",sum)