# -----------------------zip(*) function-------------------------
# matrix=[(1,2),(3,5),(6,7)]
# x=zip(*matrix)
# print(tuple(x))

#----------------------------------------------------------------
def print_all(State,Capital):
    print(State)
    print(Capital)

args='Bihar','Dehli'
print_all(*args)