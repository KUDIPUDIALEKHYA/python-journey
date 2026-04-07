ip=str(input("Enter an input")).lower()
if len(ip)!=1:
    print("Enter a valid single alphabet!")
elif ip in 'aeiou':
    print(f"your input {ip} is a vowel")
else:
    print(f"your input {ip} is a constant") 