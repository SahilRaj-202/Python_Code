#write a program to create a list with element 1,2,3,4 and 5 display even element of the list using list comprehension
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
print("Content of List1")
print(list1)
list1=[x for x in list1 if x%2==0]
print("Even element from the list")
print(list1)
list2=[x for x in list2 if x%2!=0]
print("Odd element from the  list ")
print(list2)