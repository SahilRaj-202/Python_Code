# write a fiunction to check the list is palindrome or not
def is_Lst_Palindrome(lst):
    r=lst[::-1]
    for i in range(0 ,(len(lst)+1)//2):
        if r[i]!=lst[i]:
            return False
    return True
lst=[1,2,3,2,1]
x=is_Lst_Palindrome(lst)
print(lst,"is palindrome",x)