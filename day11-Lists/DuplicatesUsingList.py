a = list(map(int, input("Enter list 1: ").split()))
b = list(map(int, input("Enter list 2: ").split()))
result = a.copy()
for i in b:
    if i not in result:
        result.append(i)
print("Merged list:", result)
