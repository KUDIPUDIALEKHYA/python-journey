ip=str(input("Enter a string"))
rev=''
for i in ip:
    rev=i+rev
if rev==ip:
    print(f"Your string {ip} is a palindrome")
else:
    print(f"Your string {ip} is not a palindrome")
