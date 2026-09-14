temperature=str(input("Enter temperature in Celsius: "))
fahrenheit= float(temperature)*9/5+32.0
print("Temperature in Fahrenheit:", fahrenheit)
if fahrenheit>100:
    print("It's hot outside!")
elif fahrenheit<32:
    print("It's cold outside!")
else: 
    print("The weather is moderate.")