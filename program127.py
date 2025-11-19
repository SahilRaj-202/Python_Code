#demonstrate the use of zip(*) function
l1=[('Apple',150000),('Dell',30000)]
laptop,prize=zip(*l1)
print(laptop)
print(prize)