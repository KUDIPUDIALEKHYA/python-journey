numbers=input("enter a continuous series of number")
first=int(numbers[0])
valid=True
for i in numbers[1:]:
    if (first:=first+1)!=int(i):
        valid=False
        break
        

print(valid)
