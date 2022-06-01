a,b,c,d,e = map(int, input("Enter the five Numbers: ").split(" "))
print("The Quotient and Remainder respectively is: ", divmod(max(a,b,c,d,e),min(a,b,c,d,e)))