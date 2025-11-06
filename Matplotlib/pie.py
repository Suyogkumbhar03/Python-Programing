import matplotlib.pyplot as plt


fruits = ['Apple', 'Banana', 'Mango', 'Orange']
quantity = [40, 25, 30, 20]


plt.pie(quantity, labels=fruits, autopct='%1.1f%%')

plt.title("Fruit Distribution")
plt.show()
