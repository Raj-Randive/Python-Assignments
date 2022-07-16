import random
import matplotlib.pyplot as Plot
import numpy as np

list1=[]
print("List 1")
for i in range (0,100):
    x=random.randint(0,100)
    list1.append(x)

print(list1)
print("\n")

list2=[]
print("List 2")
for i in range (0,100):
    x=random.randint(0,100)
    list2.append(x)

print(list2)
print("\n")

list3=[]
print("List 3")
for i in range (0,100):
    x=random.randint(0,100)
    list3.append(x)

print(list3)
print("\n")

list4=[]
print("List 4")
for i in range (0,100):
    x=random.randint(0,100)
    list4.append(x)

print(list4)
print("\n")

list5=[]
print("List 5")
for i in range (0,100):
    x=random.randint(0,100)
    list5.append(x)

print(list5)
print("\n")




# *************************************************************************************************





avg_list=[]
average=0

for i in range(0,100):
    average = (list1[i]+list2[i]+list3[i]+list4[i]+list5[i])/5
    avg_list.append(average)

print("Average List")
print(avg_list)
print("\n\n")





# ************************************************************************************



countA=0
countB=0
countC=0
countD=0
countE=0

grade_list=[]
for i in avg_list:
    if (i >80):
        value="A"
        countA +=1
    elif(i>60 and i<79.99):
        value="B"
        countB +=1
    elif(i>40 and i<59.99):
        value="C"
        countC +=1
    elif(i>30 and i<39.99):
        value="D"
        countD +=1
    else:
        value="E"
        countE +=1


    grade_list.append(value)

print("Grade List")
print(grade_list)
print("\n\n")



# open file
with open(r'E:/.txt', 'w') as gradelist:
    for item in grade_list:
        # write each item on a new line
        gradelist.write("%s\n" % item)
    print('Done')
    print("\n\n")





# ************************************************************************************************



print(f"Frequency of A: {countA},\nFrequency of B: {countB},\nFrequency of c: {countC},\nFrequency of D: {countD},\nFrequency of E: {countE}\n")



#Plotting Graph
x = np.array(['A', 'B', 'C', 'D', 'E'])
Plot.xlabel("Grades")

y = np.array([countA, countB, countC, countD, countE])
Plot.ylabel("Frequency of Grades")

Plot.bar(x, y, color = "Red", width= 0.5)
Plot.show()






