
nums=list(map(int,input("Enter a series of numbers").split()))
frequency={}
for num in nums:
    if num in frequency.keys():
        frequency[num]+=1
    else:
        frequency[num]=1        
print(f"{frequency.items()}")
        
        