# write a program to sort using list inbuilt function but tuble also used.
list1=[23,46,45,2,22]
t1=tuple(list(list1))
print('Original values :',list1)
list1.sort()
t1=tuple(list(list1))
print("Sortes tuple :",t1)