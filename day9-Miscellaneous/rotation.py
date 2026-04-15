s1=str(input("Enter a string")).lower()
s2=str(input("Enter a string")).lower()
if len(s1)==len(s2) and s2 in s1+s1:
    print("It is a string rotation")
else:
    print("It is not a string rotation")