#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal
def convert(dec_num):
    print("The decimal value of",dec_num ,"is")
    print(bin(dec_num),"in binary ")
    print(oct(dec_num),"in octal")
    print(hex(dec_num),"is hexadecimal")
    print("\n")
convert(1)
convert(2)
convert(3)
convert(4)
convert(6)