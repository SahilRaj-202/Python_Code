#--write a program to display the pattern of star given s follow
# * * * * *
# * * * *
# * * *
# * *
# *

num=7

for i in range (1,6,1):
    num=num-1;
    for j in range(1 ,num,1):
            print(" * ",end=" ")
    print()