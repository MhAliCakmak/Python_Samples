import pandas as pd 
import numpy as np

data=np.random.randint(0,100,size=(10,5)) # 10 rows, 5 columns
df=pd.DataFrame(data,columns=list('ABCDE')) # A, B, C, D, E columns
result=df
result=df.head() # first 5 rows
result=df.tail() # last 5 rows
result=df[["A","B"]].head()   # first 5 rows of column A and B
result=df[2:5][["A","B"]]    # rows 2,3,4 of column A and B


result=df > 50 # boolean dataframe
result=df[df > 50] # dataframe with values > 50
result=df[df["A"] > 50] # dataframe with values of column A > 50
result=df[df["A"] > 50][["A","B"]] # dataframe with values of column A > 50 and columns A and B
result=df[(df["A"] > 50) & (df["B"] > 50)]  # dataframe with values of column A > 50 and column B > 50
result=df[(df["A"] > 50) | (df["B"] > 50)]  # dataframe with values of column A > 50 or column B > 50
result=df[(df["A"] > 50) & (df["B"] > 50)][["A","B"]]  # dataframe with values of column A > 50 and column B > 50 and columns A and B

result=df.query('A > 50 and B > 50') # dataframe with values of column A > 50 and column B > 50
result=df.query('A > 50 and B > 50')[["A","B"]] # dataframe with values of column A > 50 and column B > 50 and columns A and B
print(result)
