ip=str(input("Enter a string"))
j=0
for i in ip:
    j+=1
    if i not in ip[j:] and i not in ip[:j-1]:
        print (f"{i}")
        break
    