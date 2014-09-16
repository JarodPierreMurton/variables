#Jarod Pierre Murton
#Code to convert temperature
#16/9/14

#program asks user to input a temperature in fahrenheit
fahrenheit = int(input("Please enter your temperature in fahenheit: "))

#works out the equivalent temperature in centigrade from the number given
centigrade = (fahrenheit-32) * (5/9)
#temperature is rounds to a whole number
centigrade = round(centigrade, 0)

#answer is displayed to the user
print("Your temperature in Centigrade is {0}" .format(centigrade))
