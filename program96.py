#write a program to create a list "A to generate square of the number(from 1 to 10)"list "B" to generate cube of the number(from 1 to 10)"
print("ListA",end="")
listA=[x**2 for x in range(1,11)]
print(listA)

print("ListB",end="")
listB=[x**3 for x in range(1,11)]
print(listB)
print("Only Even Number from list A",end="")
c=[c for c in listA if c%2==0]
print(c)

print("Only Odd Number from list A",end="")
d=[d for d in listB if d%2==0]
print(d) 