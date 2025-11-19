#-write a program to calculate the area of circle and useibng format() function
radius=int(input('Enter a radius of a circle : '))
PI=3.1428;
Area=PI*radius*radius
print("Radius : ",radius)
print("The Area Of Circle :",format(Area,'.6f'))