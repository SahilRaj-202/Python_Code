# write a program to print and store Even of number into a dictionary

# ----------------method1-------------
# def Even_number():
#     n=int(input('Enter Nth number'))
#     D=dict()
#     for i in range(1,n+1):
#           if i%2==0:
#             D[i]=i
#             print(D[i])

# Even_number()

# ----------------method2-------------
def Even_number(n):
    D=dict()
    for i in range(1,n+1):
          if i%2==0:
            D[i]=i
    return D

E=Even_number(10)
print(E)
