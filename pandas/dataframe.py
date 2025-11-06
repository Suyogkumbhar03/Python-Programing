import pandas as pd


data = {
    'Name': ['Suyog', 'Amit', 'Priya'],
    'Age': [20, 22, 21],
    'City': ['Kolhapur', 'Pune', 'Mumbai']
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
