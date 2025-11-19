#--write a program to print the sum of the numbers from 1 to 20  are include that are divisible by 5 using while loop--#
count=0
sum=0
while count <=20:
    if count%5==0:
        sum=sum+count
    count=count+1
print("the sum of the numbers from 1 to 20   divisible by 5 ",sum)