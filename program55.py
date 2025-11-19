#--write a program to display the pattern of star given s follow
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("number pattern dsiplay :")
n=1
for i in range(1,6,1):
    n=n+1
    for j  in range(1,n,1):
        print(j,end=" ")
    print()
