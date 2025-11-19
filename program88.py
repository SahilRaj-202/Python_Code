#---------------LIST SLICING [START:END]------------------------
l1=[1,2,3,4,5,6]
for i in range(0,6):
    print("index[",i,']=',l1[i])
print("slicing list is")
print(l1[2:5])

#----------------LIST SLICING WITH STEP SIZE--------------------
l2=[1,"a",2,"b",3,"c",4,"d",5,"e",6,"f"]
for i in range(0,13):
    print("index[",i,']=',l2[i])
print("list slicing with step size is")
print(l1[0:6:2])
