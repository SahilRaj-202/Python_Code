def  print_Avg(list1):
    sum=0;
    print("The list of five element is ")
    for num in list1:
        print(num,end=" ")
        sum=sum+num
    avg=sum/len(list1)
    print("\n")
    print("The Average of listed five element is" ,avg)

list1=[10,20,30,40,50]
print_Avg(list1)