import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\varsh\Downloads\csv-data-analyzer-main\csv-data-analyzer-main\data.csv"
)

print("First 5 Rows:")
print(df.head())

print("\nSummary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

amounts = np.array(df["Amount"])

print("\nNumPy Calculations")
print("Total Expense:", np.sum(amounts))
print("Average Expense:", np.mean(amounts))
print("Maximum Expense:", np.max(amounts))
print("Minimum Expense:", np.min(amounts))
print("Standard Deviation:", np.std(amounts))

gst_amounts = amounts * 1.18

print("\nExpenses after adding 18% GST:")
print(gst_amounts)

category_expense = df.groupby("Category")["Amount"].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_expense.index, category_expense.values)
plt.xlabel("Category")
plt.ylabel("Total Expense")
plt.title("Expense by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.plot(df.index, df["Amount"], marker="o")
plt.xlabel("Transaction Number")
plt.ylabel("Amount")
plt.title("Expense Trend")
plt.grid(True)
plt.show()