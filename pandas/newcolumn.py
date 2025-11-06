import pandas as pd

data = {
    'Name': ['Suyog', 'Amit', 'Priya'],
    'Maths': [80, 70, 90],
    'Science': [85, 75, 95]
}

df = pd.DataFrame(data)

# Add a new column for total marks
df['Total'] = df['Maths'] + df['Science']

print("DataFrame with Total Marks:")
print(df)
