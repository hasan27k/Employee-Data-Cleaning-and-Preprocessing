# importing the nessary lib
import pandas as pd
import numpy as np

# loadinf the dataset 
df = pd.read_csv(r"D:\New folder (4)\python_project\Emp.csv")
print(df.head())

# checking the missing values
print("Missing values in each column")
print(df.isnull().sum())

# fix column names (strip spaces)
df.columns = df.columns.str.strip()

df["Salary(INR)"].fillna(df["Salary(INR)"].mean(), inplace=True)
df["Performance Rating"].fillna(df["Performance Rating"].median(), inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove the duplicate records
df.drop_duplicates(inplace=True)

# replace negative salaries
df["Salary(INR)"] = np.where(df["Salary(INR)"] < 0,
                             df["Salary(INR)"].mean(),
                             df["Salary(INR)"])

salary_mean = df["Salary(INR)"].mean()
salary_standard = df["Salary(INR)"].std()
lower_bound = salary_mean - (3 * salary_standard)
upper_bound = salary_mean + (3 * salary_standard)  

# remove rows where salary is too high and too low
df = df[(df["Salary(INR)"] >= lower_bound) & (df["Salary(INR)"] <= upper_bound)]

df.to_csv("Emp1.csv", index=False)

print('data cleaning completed Saved as "Emp_clean.csv"')
