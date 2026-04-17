password=input("Enter a password")
hasUpper=any(char.isupper() for char in password)
haslower=any(char.islower() for char in password)
hasdigit=any(char.isdigit() for char in password)
valid_password=hasUpper and haslower and hasdigit and len(password)>=8 
print(valid_password)