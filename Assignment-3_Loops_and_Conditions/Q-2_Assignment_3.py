l=['a', 'e', 'i', 'o', 'u']
i,count=1,0
while(i<=10):
    x = input(f"Enter Character {i}: ")
    x = x.lower()
    if x in l:
        count+=1
    i+=1
print(f"The number of Vowels are: {count}")
