numbers = tuple(input("Enter the numbers: "))
number = input("Enter the number: ")

count = 0
for i in numbers:
    if i == number:
        count += 1

print("Count:", count)