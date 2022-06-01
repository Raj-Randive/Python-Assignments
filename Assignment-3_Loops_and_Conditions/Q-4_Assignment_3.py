x = float(input("Enter a length of side of square: "))
while(True):
    if(x<=0):
        x = float(input("Please enter a positive side/length: "))
    elif(x>0):
        break
print(f"The Area of the square is : {x*x}")
