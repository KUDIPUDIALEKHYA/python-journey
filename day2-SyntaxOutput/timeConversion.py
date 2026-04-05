time=float(input("Enter the time"))
option=int(input("do u want to convert \n1:Hours to Minutues \n2:Minutes to hours"))
if option==1:
    print(f"{time} in minutues is {time*60}")
elif option==2:
    print(f"{time} in hours is {time*1/60}")
