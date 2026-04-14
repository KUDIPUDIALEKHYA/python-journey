a=int(input("Enter the number of days"))#accepting the number of days as the input
years=month=days=0
years=(a//365)#calculating the number of years
a%=365
print("Years->",years)#displaying number of years

month+=(a//30)#calculating number of months
days=a%30#calculating number of days

print("month->",month)#displaying number of months
print("days->",days)#displaying number of days
