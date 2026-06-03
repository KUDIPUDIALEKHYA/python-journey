nums = list(map(int, input("Enter numbers: ").split()))
snum=int(input("enter the number yyou want to find"))
low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == snum:
        print("Found at index", mid)
        break
    elif nums[mid] < snum:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")