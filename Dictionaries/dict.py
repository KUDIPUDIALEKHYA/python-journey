firstdict={
    "name":"alekhya",
     "age":20
}

print(firstdict.items())

#access:
print(f"Accessing an element in dict:{firstdict["name"]}")
#keys and values
print(f"Accessing keys and values in dict:{firstdict.keys(),firstdict.values(),firstdict.items()}")
#updating:
firstdict.update({"branch":"CSE(AI&ML)"})
print(f"Updating an element in dict:{firstdict.items()}")
#removing:
firstdict.pop("branch")
print(f"Removing an element in dict:{firstdict.items()}")
