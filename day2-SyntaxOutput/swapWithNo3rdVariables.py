n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
print(f"numbers before swapping {n1} {n2}")
n2=n1+n2
n1=n2-n1
n2=n2-n1
print(f"numbers before swapping {n1} {n2}")