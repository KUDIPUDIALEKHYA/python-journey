start=int(input("Enter the starting range for the prime numbers"))
end=int(input("Enter the ending range for the prime numbers"))
for i in range(start,end):
    for j in range(1,start):
        if i%j!=0:
            print(i)
            