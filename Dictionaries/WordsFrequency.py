words=list(input("Enter a series of strings").split())
frequency={}
for i in words:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(f"{frequency.items()}")
   