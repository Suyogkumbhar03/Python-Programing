import pandas as pd

data = {
    'Department': ['CSE', 'CSE', 'IT', 'IT', 'ENTC'],
    'Marks': [80, 70, 90, 85, 75]
}

df = pd.DataFrame(data)


avg_marks = df.groupby('Department')['Marks'].mean()

print("Average marks by department:")
print(avg_marks)
