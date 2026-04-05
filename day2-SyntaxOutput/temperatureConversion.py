temp=float(input("enter the temperature"))
option=int(input("do you want to convert 1:Fahrenheit to celsius or 2:Celsius to Fahrenheit"))
if option==1:
    print(f"{temp} fahrenheit in celsius is {(temp - 32) * 5/9}")
elif option==2:
    print(f"{temp} celcius in fahrenheit is  {(temp * 9/5) + 32}")