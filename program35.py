#write a program that program that prompts auser to enter two different numbers.perform  basic aritmetic operations based on the choice--#
num1=float(input("Enter a 1st number :"))
num2=float(input("Enter a 2nd number :"))
print(" Addition ")
print(" Subtraction ")
print(" Multiplication ")
print(" Division ")

choice=int(input("Please Enter the Choice :"))

if choice==1:
    print("Addition of ",num1 ," and ",num2 ," is ",num1+num2)
elif choice==2:
    print("Subtraction of ",num1 ," and ",num2 ," is ",num1-num2)
elif choice==3:
    print("Multiplication of ",num1 ," and ",num2 ," is ",num1*num2)
elif choice==2:
    print("Division of ",num1 ," and ",num2 ," is ",num1/num2)
else:
    print("Sorry!!! invalid Choice ")