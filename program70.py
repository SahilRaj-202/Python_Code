#--Write a Python Program to Print the Fibonacci sequence
def fibonacci_sequence(nterm):
   n1,n2=0,1
   count=0
   if nterm <=0:
      print("Please enter a positive number")
 
   elif nterm==1:
    print("Fibonacci sequence upto ",nterm,":")    
    print(n1)
   else:
    while count<nterm:
      print(n1)
      nth=n1+n2
      n1=n2
      n2=nth
      count=count+1

fibonacci_sequence(10)