# write a program  to pass a list to a function .calculate the total number is even or old number from the list then display the count in term dictionary
def even_old_count(l):
    D={};
    D['even']=0
    D['old']=0
    for C in l:
        if C%2==0:
            D['even']+=1
        else:
            D['old']+=1
    print(D)

l=[1,2,3,4,5,6,7,8,9,10]
even_old_count(l)