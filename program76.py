 #Python program to find H.C.F of two numbers
def compute_Hcf(x,y):
    if x>y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            Hcf=i
    return Hcf

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", compute_Hcf(num1, num2))