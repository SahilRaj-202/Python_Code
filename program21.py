#-write a program to calculate the distance of two point--#
print('Point 1')
x1=eval(input('Enter x1 coordinate :'))
y1=eval(input('Enter y1 coordinate :'))
print('Point 2')
x2=eval(input('Enter x2 coordinate :'))
y2=eval(input('Enter y2 coordinate :'))
l1=(x2-x1)**2+(y2-y1)**2
distance=l1**0.5
print('The Distances betwwen the two pints is as follow :')
print('(',x2,x1,')','','(',y2,y1,')',' = ',distance)