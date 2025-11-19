def list_Of_Multiples(k):
    my_list=[]
    for i in range(1,6):
        res=k*i
        my_list.append(res)
    return my_list
    
print("The first five multiples are",list_Of_Multiples(2))