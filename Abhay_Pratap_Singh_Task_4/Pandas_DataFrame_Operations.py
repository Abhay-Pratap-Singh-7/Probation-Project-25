import pandas as pd

df = pd.DataFrame(
    {
        'Name': ['Adi','Bobby','Candy','Dior','Ena'],
        'Age': [20,21,19,22,20],
        'Marks': [85,90,75,95,88]
    }
)
print(df)
print()
print(df.iloc[:3,:])
print()
print(df.Name)
print()
print(df[df['Marks'] > 85])
print()
df['Grade'] = ['B','A','C','A','B']
print(df)
print()
df.pop('Age')
print(df)