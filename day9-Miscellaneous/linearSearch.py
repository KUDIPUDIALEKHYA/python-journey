nums = list(map(int, input("Enter numbers: ").split()))
snum=int(input("enter the number yyou want to find"))
for i in range(len(nums)):
    if snum==nums[i]:
        print(f"\n {snum} Found at {i+1} index")
    