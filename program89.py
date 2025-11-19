#----------------LIST SLICING WITH STEP SIZE--------------------
list2=[1,"a",2,"b",3,"c",4,"d",5,"e",6,"f"]

for i in range(0,len(list2)):
     print("index[",i,']=', list2[i])

print("list slicing with step size is")
print(list2[0:len(list2):4])
print("\nlist slicing with step size is")
print(list2[:4])  #by defualt start 0

