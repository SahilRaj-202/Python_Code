#-write a program to calculate Simple Interest(SI)--#
P=eval(input('Enter Principle Amount in Rs ='))
ROI=eval(input('Enter Rate of Interest  ='))
Years=eval(input('Enter the Number of Years ='))
print('-------------------------------------------------------')
print('The Principle Amount is ',P)
print('The Rate of Interest is ',ROI)
print('The Number of Year Is ',Years)
SI=(P*ROI*Years)/100
print('Simple Interest =',SI)