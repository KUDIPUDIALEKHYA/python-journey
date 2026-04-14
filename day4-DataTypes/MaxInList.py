numbers=(input("Enter different numbers").split(" "))
numsList=[]
max=int(numbers[0])
for i in numbers:
    numsList.append(int(i)) 
    if max<int(i):
        max=int(i)
           
print(f"The maximum value among the different list of numbers is {max}")