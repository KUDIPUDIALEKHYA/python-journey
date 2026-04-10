ip=str(input("Enter a string "))
nip=ip.split(" ")
print(nip)
max=""
maxl=i=0
while i<len(nip):
    if (len(nip[i])>maxl):
         max=nip[i]
         maxl=len(nip[i])
    i+=1
print(max)
