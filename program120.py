#write a program to user enter a number in list and find the maxand min number in lsit

lst=[]
for i in range(0,4):
    x=input("Enter element to add to the list:")
    x=int(x)
    lst.append(x)

print("Elements of list are as follow")
print(lst)

def Max(lst):
    mymax=lst[0]
    for num in lst:
        if mymax<num:
            mymax=num
    return mymax

def Min(lst):
    mymin=lst[0]
    for num in lst:
        if mymin >num:
            mymin=num
    return mymin

x=Max(lst)
print("Maximum element from list ",x)
y=Min(lst)
print("Minimum element from list ",y)