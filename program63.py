#-- write a program to add the sum of digits from 1 to 25,50 to 76,and 90 to 100.+
def sum(x,y):
    s=0;
    for i in range(x,y+1): 
        s=s+i
    print("the sum is",s)

sum(1,25)
sum(50,76)
sum(90,101)