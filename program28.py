#write a program which prompt a user to enter the radius o a crcle.if the radius is greater than zero statement then calculate area and circumference--#

Radius=float(input('enter the Radius of Circle :'))
PI=3.14
if(Radius>0):
    Area=PI*Radius*Radius
    print('The Area of Circle is :',Area)
    Circumference=2*PI*Radius
    print('Circumference of Circle is :',Circumference)

 