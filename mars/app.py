import main
while(1):
    a=eval(input("Enter 1 to calculate distance:"))
    if a==1:
        inp=eval(input("Enter the travelled distance :"))
        mar=main.Mars
        mar.distance(inp)
    else:
        print("enter the proper key")
