# demonstrate the set function
print('Create set')
S1={1,2,3,4,5}
for i in S1 :
    print(i)  
print('\n')


# ---------------------in operator--- not in operator--------------

print('In || Not in Operator')
S2={1,2,3,4,5}
print(3 in S2)
print(6  not in S2)
print('\n')

# --------------------Add() function in set---------------------


print('Add function in set')
S3={1,2,3,4,5}
print('After value of set ',S3)
S3.add(6)
S3.add(7)
S3.add(8)
print('Before value of set ',S3)
print('\n')

# --------------------Clear()function in set---------------------

print('Clear function in set')
S3.clear()
print('Before value in set ',S3)
print('\n')
# --------------------Remove() function in set---------------------

print('Remove function in set')
S4={11,12,13,14,15}
print('After value of set ',S4)
S4.remove(15)
S4.remove(14)
S4.remove(13)
S4.remove(12)
print('Before value of set ',S4)
