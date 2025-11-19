#--write a program to print fibonacci series--#
first_number=int(input("Please Enter First Number :"))
second_number=int(input("Please Enter Second Number :"))
limit=int(input("Number of Fibonacci Number to be Print :"))
print(first_number, end=" ")
print(second_number,end=" ")
for i in range(limit):
    sum=first_number+second_number
    first_number=second_number
    second_number=sum
    print(sum,end=" ")