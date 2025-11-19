#-write a program to rad theweight of an object in grams and display its weight in kilograms and grams --#

w1=eval(input('Enter the Weight of Object in grams :'))
print('Weight og Object = ',w1 , 'grams')
w2=w1//1000;  # //used in find quotient
w3=w1%1000;   # % used in find remainder
print('Weight of Object = ',w3,' kg',w3,' grams')