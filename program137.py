# write a program to count the frequency of  characters using the get() method

def Histogram(s):
    D=dict()
    for C in s:
        if C not in D:
            D[C]=1

        else:
            D[C]=D.get(C,0)+1
    return D

H=Histogram("Jay SHRI Ram")
print(H)