# write a function histogram that takees string as parameter and generates a fequency of characters contained in in

# -------------------method 1--------------------------
# def Histogram(s):
#     D=dict()            #empty dictionary created
#     for C in s:
#         if C not in D:
#          D[C]=1
        
#         else:
#            D[C]=D[C]+1
#     return D

# H=Histogram("SAHIL")
# print(H)


# -----------------method 2-------------------
def Histogram():
    s = 'SSAAHHIILL'
    D = dict()            # empty dictionary created
    
    for C in s:
        if C not in D:
            D[C] = 1
        else:
            D[C] = D[C] + 1

        print(f"{C} → {D[C]}")


