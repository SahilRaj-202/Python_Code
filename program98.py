#consider the list with mixed type of element such as l1[1,2,3,4,5,'a','c','d','e','r'].print only integer number
print("List with mixed elements")
l1=[1,2,3,4,5,'a','c','d','e','r']
print("List1",end='')
print(l1)
c=[x for x in l1 if type(x)==int]
print("The integer list is")
print("list1",end="")
print(c)