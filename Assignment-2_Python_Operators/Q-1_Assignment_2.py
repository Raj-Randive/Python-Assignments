x,y = map(float, input("Enter any two numbers: ").split(" "))
a=x
b=y
print(f"Addition: {x+y}, \nSubtration: {x-y}, \nMultiplication: {x*y}, \nDivision: {x/y}, \nModulus: {x%y}, \nExponential: {x**y}, \nFloor Division: {x//y}")

print("Equal : ", x==y)
print("Not Equal : ", x!=y)
print("x > y : ", x>y)
print("x < y : ", x<y)
print("x >= y : ", x>=y)
print("x <= y : ", x<=y)

print("And : ", x and y)
print("Or : ", x or y)
print("not: ", not(x is y))

print("is : ", x is y)
print("is not : ", x is not y)

print("comma : ", (x,y))

x+=y
print("+= : ", x)

x-=y
print("-= : ", x)

x*=y
print("*= : ", x)

x/=y
print("/= : ", x)

x%=y
print("%= : ", x)

a//=b
print("//= : ", a)

a**=b
print("**= : ", a)