ip = list(input("Enter numbers: "))
result = []
for i in ip:
    if i not in result:
        result.append(i)
print("Unique elements:", result)