def split_List(lst,n):
    list1=lst[:n]
    list2=lst[n:]
    print("First list with",n,"element")
    print(list1)

    print("Second list with",len(lst)-n,'element')
    print(list2)

lst=[10,20,30,40,50]
print("List Lst Before spliting")
print(lst)

split_List(lst,4)