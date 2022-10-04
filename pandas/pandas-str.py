import pandas as pd

# Read the CSV file into a DataFrame: df
df = pd.read_csv('all_seasons.csv')


result = df
result = df.columns

result=df['player_name']


# Print data
print(result)
