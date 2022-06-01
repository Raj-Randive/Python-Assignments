import matplotlib.pyplot as plt
principal = 10000  #initialinvestment
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
plt.plot(values)
plt.title('5% Growth, CompoundedAnnually')
plt.xlabel('Years of Compounding')
plt.ylabel('Value of Principal ($)')
plt.show()  # Only for ides not for online google collab or jupyter
