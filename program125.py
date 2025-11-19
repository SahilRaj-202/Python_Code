l1=['black','white','red']
l2=[23,4,55]
#print(tuple(zip(l1,l2)))   #output:-(('black', 23), ('white', 4), ('red', 55))
for color,code in zip(l1,l2):
    print(color,code)     