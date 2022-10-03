import pandas as pd
import numpy as np

# Read the data
data = np.random.randint(0, 100, size=(5, 3))  # 10 rows, 5 columns
# A, B, C, D, E columns 1, 2, 3, 4, 5 rows
df = pd.DataFrame(data, index=list("12345"), columns=list('ABC'))
df = df.reindex(["1", "12", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

result = df
result = df.dropna()  # Drop the rows with NaN
result = df.drop("1", axis=0)  # Drop the row with index 0
result = df.drop("A", axis=1)  # Drop the column with index 0

result = df.fillna(0)  # Fill the NaN with 0
result = df.fillna(method="ffill")  # Fill the NaN with the previous value
result = df.fillna(method="bfill")  # Fill the NaN with the next value
result = df.isnull()  # Check if the values are NaN
result = df.notnull()  # Check if the values are not NaN
result = df.dropna(how="all")  # Drop the rows with all NaN
result = df.dropna(thresh=2)  # Drop the rows with 2 or more NaN
result = df.dropna(subset=["A"])  # Drop the rows with NaN in column A
result = df.dropna(how="any")  # Drop the rows with any NaN

# Display the data
print(result)
