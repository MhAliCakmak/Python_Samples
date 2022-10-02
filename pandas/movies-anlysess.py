import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('movies.csv')
result=df
result=df.columns # get the column names
result=df.head() # get the first 5 rows
result=df.head(10) # get the first 10 rows
result=df.tail() # get the last 5 rows
result=df.tail(10) # get the last 10 rows

result=df["Title"] #get title of movie
result=df["Title"].head()
result=df[["Title","Genre"]].head() # get title and genre of movie
result=df[["Title","Genre"]].tail(7) # get title and genre of movie
result=df[5:10][["Title","Genre"]] # get title and genre of movie in 5 to 10 rows
result=df[df["International Sales (in $)"] > 100000000][["Title","Genre"]].head(50) # get the movies with international sales > 100000000]]]
# Display the data
print(result)