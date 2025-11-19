#write a function which can accept or pass "n" number of non keyword variable length argument to calculate the sum of "n" number
def calc(*args):
    s=0;
    print("The number are as follows:")
    for num in args: 
        print(num,end=' ')
        s=s+num
    return s;
Total=calc(10)
print("Sum =",Total)
Total=calc(10,20)
print("\nSum =",Total)
Total=calc(10,20,30)
print("\nSum =",Total)
Total=calc(10,20,30,40)
print("\nSum =",Total)