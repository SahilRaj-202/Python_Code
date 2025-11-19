#--write a program to display the pattern of star given s follow
# * 
# * * 
# * * *
# * * * *
# * * * * *
print("Start pattern display :")
n=1

for i in range(1,6,1):
    n=n+1
    for j in range(1,n,1):
        print(" * ",end=" ")
    print()



