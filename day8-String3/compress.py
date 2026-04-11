ip=input("Enter a string").lower()
count=1
res=""
for j in range(len(ip)):
    if j<len(ip)-1 and ip[j]==ip[j+1]:
        count+=1
    else:
        res+=ip[j]+str(count)   
        count=1 

print(res)
