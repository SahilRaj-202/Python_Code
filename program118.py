def lst_Reverse(lst):
    r=lst[::-1]
    for i in range(0,len(lst)):
        print(r[i],end=" ")
lst=[1,2,3,4,5,6]
lst_Reverse(lst);