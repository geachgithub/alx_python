#Tamprature converter function
def convert_to_celsius(fahrenheit):
    return round(number=((fahrenheit-32)*(5/9)),ndigits=1 or 2)
'''print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))'''