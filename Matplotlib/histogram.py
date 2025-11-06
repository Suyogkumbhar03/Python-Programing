import matplotlib.pyplot as plt

# Data
marks = [55, 60, 65, 70, 72, 75, 80, 82, 85, 90, 92, 95]

# Create histogram
plt.hist(marks, bins=5, edgecolor='black')

plt.title("Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()
