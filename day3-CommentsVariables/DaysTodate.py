a=int(input("Enter the number of days"))
years=month=days=0
years=(a//365)
a%=365
print("Years->",years)

month+=(a//30)
days=a%30
print("month->",month)

print("days->",days)
