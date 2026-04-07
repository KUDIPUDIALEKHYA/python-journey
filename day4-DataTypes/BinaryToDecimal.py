ip=int(input("Enter a binary number"))
decimal=pos=0
while ip>0:
    decimal+=(ip%10)*(2**pos)
    ip//=10
    pos+=1
print(decimal)