ip=input("Enter a string")
for i in range(len(ip)):
    for j in range (i+1,len(ip)+1):
        print(ip[i:j])
    