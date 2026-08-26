input=list(map(int,input("Enter a series of numbers").split()))
count={}
dup="False"
for i in count.items():
    if i in count:
        count[i]+1
        dup="True"

if dup:
    print("The list has duplicates")
        

        
