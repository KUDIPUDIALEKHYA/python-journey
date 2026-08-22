marks = {
    "Rahul": 7,
    "Priya": 45,
    "Arjun": 99,
    "Sneha": 39,
    "Kiran": 91
}
max=0
print("Students who scored more than an average marks of 75")
for x,y in marks.items():
    if y>=75:
        print(f"{x}")

print("Highest Score is ")
for x in marks.values():
    if x>=max:
        max=x  
print(f"{max}")


   
    
    
