#write aprogram to calculate the hypotenuse of the right-angled triangle given as follow
import math
Height=int(input('Enter the height of a right-angled triangle:'))
Base=int(input('Enter the base of a right-angled triangle'))
print('Triangle details are as follow: ')
print('Base :',Base)
print('Height :',Height)
Hypotenuse=math.sqrt(Base*Base+Height*Height)
print('The Hypotenuse :',Hypotenuse)