ip=list(input("enter 5  numbers"))
max=min=ip[0]
for i in ip:
    if max<i:max=i
    elif min<i:min=i
    
print(f"The maximum and minimum values among these {ip} are {max} and {min} ")
