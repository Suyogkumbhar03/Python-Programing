import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D']
marks = [85, 90, 75, 95]

plt.bar(students, marks, color='skyblue')
plt.title("Bar Graph Example")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
