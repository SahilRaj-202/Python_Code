#-write a program to find the maximun of two number
def larger_number(num1,num2):
    if(num1>num2):
        {
        print("num1 is larger then num2")
        }
    elif(num2>num1):
        {
        print("num2 is larger then num1")
        }
    else:
        {
        print("num1 is equal to num2")
        }

larger_number(1,11)
larger_number(11,1)
larger_number(11,11)