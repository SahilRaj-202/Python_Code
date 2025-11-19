#-write program to calculate the salary of medical representation considering the sales bones and incentives--#
sales=float(input('Enter Total Sales of The Month :'))
if sales > 100000:
    basic=4000
    HRA=20*basic/100
    Da=110*basic/100
    Incentive=sales*10/100
    Bonus=1000
    Conveyance=500
else:
    basic=4000
    HRA=10*basic/100
    Da=110*basic/100
    Incentive=sales*4/100
    Bonus=1000
    Conveyance=500

    salary=basic+HRA+Da+Incentive+Bonus+Conveyance

    print('Salary Receipt of Employee :')
    print('Basic :',basic)
    print('HRA :',HRA)
    print('Da :',Da)
    print('Incentive :',Incentive)
    print('Bonus :',Bonus)
    print('Conveyance :',Conveyance)
    print('Gross Salary :',salary)
