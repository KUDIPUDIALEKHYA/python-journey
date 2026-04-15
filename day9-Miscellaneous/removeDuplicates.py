s=str(input("Enter a string")).lower()
ns=''
for i in s:
    if i not in ns:
        ns+=i
print(str(ns))