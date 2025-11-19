#write a program to demonstrate inbuilt function in lists
# 1. len()
# 2. max()
# 3. min()
# 4. sum()
# 5. random.shuffle()
import random
list1=[1,2,3,4,5,6];
print("The size of list is",len(list1))
print("The maximun number of list is",max(list1))
print("The minimun number of list is",min(list1))
print("The sum of number of list is",sum(list1))
random.shuffle(list1)
print("The random shuffle number of list is",list1)
