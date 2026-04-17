username=input("Enter a username")
is_valid=username[0].isalpha and username.isalnum and (5<=len(username)<=12)
print(is_valid)