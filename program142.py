# write a program to convert an octal number into binary

def convert_Oct_Bin(Number,Table):
    Binary=''
    for Digit in Number:
        Binary=Binary+Table[Digit]
    return Binary

octToBinaryTable={'0' :'000', '1' : '010',  '2':'010',
                 '3' :'011' ,'4' :'100', '5': '101', 
                 '6': '110', '7' :'111'}

result=convert_Oct_Bin("127",octToBinaryTable)
print(result)