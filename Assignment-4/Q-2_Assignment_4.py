def ASMD(a, b):
    print(f"Adding {a} with {b}\nAns: {a+b}")
    print(f"Subtracting {b} from {a}\nAns: {a-b}")
    print(f"Multiplying {a} with {b}\nAns: {a*b}")
    print(f"Dividing {a} by {b}\nAns: {int(a/b)}")
x = int(input("Enter the value of a\n> "))
y = int(input("Enter the value of b\n> "))
ASMD(x,y)