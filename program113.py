# -- write a program to pass a list to function---
def reverse_Lst(lst):
     print("List before Revrsing",lst)
     lst.reverse()
     return lst
lst=[5,4,3,2,1]
print("List after Reversing",reverse_Lst(lst))