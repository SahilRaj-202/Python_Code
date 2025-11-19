#write program to check the list element can duplicate or not.

def check_Duplicate(lst):
    dup_lst=[]
    for i in lst:
        if i not in dup_lst:
            dup_lst.append(i)
        else:
            return True
    return False

lst=[1,2,3,4,5]
print(check_Duplicate(lst))