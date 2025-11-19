#consider a list with five different celsius values.convert all the celsius values into fahrenheit
print("All the elements with Celsius values:")
print("Celsius",end="")
celsius=[10,20,31.3,40,39.2]
print("Celsius to Fahrenheit Conversions")
print("Fahrenheit",end="")
fahrenheit=[((9/5)*x+32) for x in celsius]
print(fahrenheit)