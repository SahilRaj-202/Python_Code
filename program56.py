#--write a program to display the pattern of star given s follow-#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3
# 1 2
# 1
print(" Number Pattern display :")
n=1
for i in range(1,5,1):
    n=n+1
    for j in range(1,n,1):
        print(j,end=" ")
    print()

n=5
for i in range(1,5,1):
    n=n-1
    for j in range(1,n,1):
        print(j,end=" ")
    print()

