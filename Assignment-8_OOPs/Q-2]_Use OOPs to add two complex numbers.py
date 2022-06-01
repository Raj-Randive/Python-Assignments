print("\nThe Format for writing complex numbers : a + ib. \n")

class Complex:
    def initComplex(rajcode):
        rajcode.realpart = int(input("\tEnter the Real Part of Complex Number: "))
        rajcode.imgpart = int(input("\tEnter the Imaginary Part of Complex Number: "))

    def show(rajcode):
        print(rajcode.realpart, "+", rajcode.imgpart,"i")

    def sum(rajcode, c1, c2):
        rajcode.realPart = c1.realPart + c2.realPart
        rajcode.imgPart = c1.imgPart + c2.imgPart


c1 = Complex()
c2 = Complex()
c3 = Complex()
print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()
print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()



# print("\nEnter first complex number")
# c1 = Complex()
# print("\tFirst Complex Number: ", end="")
# c1.show()


# print("\n\nEnter second complex number")
# c2 = Complex()
# print("\tSecond Complex Number: ", end="")
# c2.show()


# print("\n\nSum of two complex numbers is: ", sum(c1,c2))

