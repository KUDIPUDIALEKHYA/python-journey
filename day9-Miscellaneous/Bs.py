nums=list(map(int,input("Enter the elements").split()))
snum=int(input("enter your number"))
low=0
high=len(nums)-1
mid=(low+high)//2
while low<=high:
    if snum>nums[mid]:
        low=mid
        mid=(low+high)//2
    elif snum<nums[mid]:
        high=mid
        mid=(low+high)//2
    
print("element found")

