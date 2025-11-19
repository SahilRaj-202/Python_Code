# write a program to print and store squares of number into a dictionary

def sq_number(n):
    D=dict()
    for i in range(1,n+1):
        D[i]=i*i
    return D

Sq=sq_number(10)
print(Sq)