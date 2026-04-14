s1=str(input("Enter a string")).lower()
s2=str(input("Enter a string")).lower()
ns1=list(s1)
ns2=list(s2)

for i in range(0,len(ns1)):
    for j in range(0,len(ns2)):
        if ns1[i]==ns2[j]:
            ns1[i]=''
            ns2[j]=''
            break

if ns1==ns2:
    print("It is a anagram")
else:
    print("It is not an anagram")