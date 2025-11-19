#-Write a Python Program to sum of natural number
def sum_natural_number(num):
    sum=0
    for i in range(1,num+1): 
     sum=sum+i
    print("The sum of natural number is",sum)

sum_natural_number(10)
