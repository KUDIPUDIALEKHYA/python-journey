ip=str(input("Enter a string"))

for i in ip:
    if i.islower():
        print(i.upper(),end="")
    elif i.isupper():
        print(i.lower(),end="")
    else:
        print(f"Invalid character found {i}!!!!!")