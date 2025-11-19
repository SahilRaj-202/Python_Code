def list_Of_Odd(start,end):
    output_list=[]
    for num in range(start,end):
        if(num%2!=0):
            output_list.append(num)
    return output_list
print("The odd numbers are",list_Of_Odd(1,10))