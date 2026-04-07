ip=int(input("Enter a number"))
a=ip
reverse=str()
while a>0:
    reverse+=str(a%10)
    a//=10
if str(ip)==reverse:
    print("Your input is a palindrome")
else:
    print("Your input is not a palindrome")