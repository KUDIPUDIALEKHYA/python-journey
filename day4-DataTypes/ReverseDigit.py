a=int(input("Enter a number"))
reverse=str()
while a>0:
    reverse+=str(a%10)
    a//=10
print(reverse)
    