# t1=()
# print(type(t1))

# t2=(1,2,3)
# print(type(t2))

# t3=('a','aa','aaa')
# print(type(t3))

# t4='a','aa','aaa'
# print(type(t4))

# t5=(4,)
# print(type(t5))

# t6=(4)
# print(type(t6)) #not a tuple 

#write a program to create a function create_tup() which accepts a variable number of argument and print into of them.

def create_tup(*args):
    print(args)

create_tup(1,1,1)