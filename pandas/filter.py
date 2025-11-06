import pandas as pd

data = {
    'Name': ['Suyog', 'Amit', 'Priya', 'Ravi'],
    'Marks': [85, 70, 95, 60]
}

df = pd.DataFrame(data)

# Filter students with marks greater than 75
filtered = df[df['Marks'] > 75]

print("Students with marks > 75:")
print(filtered)
