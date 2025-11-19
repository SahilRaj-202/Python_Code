#write a program find the old tuple using function

def oldtuple(aTup):
    rTup=()
    index=0
    while index < len(aTup):
        rTup+=(aTup[index],)
        index+=2
t=[11,12,13,14,15,16,17,18,19]
print(oldtuple(t))