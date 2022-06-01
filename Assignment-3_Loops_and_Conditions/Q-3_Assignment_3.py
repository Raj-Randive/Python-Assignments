sum = 0
for i in range (1,101):
    if(i%2==0 or i%3==0):
        sum+=i
print(f"The Sum of numbers from 1 to 100 which are divisible by either 2 0r 3 is: {sum}")