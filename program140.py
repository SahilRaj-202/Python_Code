# write a program  to pass a list to a function .calculate the total number is pos or neg number from the list then display the count in term dictionary

def count_pos_neg(num_list):   
    D={}
    D['Positive']=0
    D['Negative']=0
    for num in num_list:
        if num>=0:
            D['Positive']+=1
        else:
            D['Negative']+=1
    print(D)

list_num=[10,-5,6,-2,3,-8,0,7,-1]
count_pos_neg(list_num)
    