def list_Of_Even(start,end):
    output_List=[]
    for x in range(start,end):
        if(x%2==0):
         output_List.append(x)
    return output_List
print("The Even numbers are",list_Of_Even(10,20))