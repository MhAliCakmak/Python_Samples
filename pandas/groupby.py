import pandas as pd
from telegram import PersonalDetails

# Read the data
PersonalDetails = {
    "Name": ["John", "Jane", "Joe", "Jill", "Jack"],
    "Age": [25, 30, 20, 35, 40],
    "Salary": [10000, 20000, 15000, 30000, 40000],
    "City": ["New York", "Los Angeles", "Chicago", "New York", "Philadelphia"],
    "Department": ["IT", "HR", "IT", "HR", "IT"]
}
df = pd.DataFrame(PersonalDetails)

# Display the data
result = df
result = df["Salary"].sum()
result = df.groupby("Department").groups  # Group by Department
result = df.groupby("Department").get_group("IT")  # Get the group of IT
# Group by Department and City
result = df.groupby(["Department", "City"]).groups
result = df.groupby("Department")["Salary"].sum()  # Sum of the groups
result = df.groupby("Department")["Salary"].mean()  # Mean of the groups
result = df.groupby("Department")["Salary"].max()  # Max of the groups
result = df.groupby("Department")["Salary"].min()  # Min of the groups
result = df.groupby("Department")["Salary"].count()  # Count of the groups
# Standard Deviation of the groups
result = df.groupby("Department")["Salary"].std()
result = df.groupby("Department")["Salary"].var()  # Variance of the groups
result = df.groupby("Department")["Salary"].describe()  # Describe the groups
result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "max", "min", "count", "std", "var"])  # Aggregate the groups
result = df.groupby("Department")["Age"].agg(
    ["sum", "mean", "max", "min", "count", "std", "var"]).loc["IT"]  # Aggregate the groups of IT
result = df.groupby("Department")["Age"].agg(["sum", "mean", "max", "min", "count",
                                              "std", "var"]).loc["IT"]["mean"]  # Aggregate the groups of IT and get the mean
print(result)
