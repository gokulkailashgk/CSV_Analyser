# 📊 CSV Data Analyzer

A beginner-friendly Python project for **loading, exploring, and analyzing CSV datasets using Pandas**. The project performs basic data inspection, generates statistical summaries, and identifies missing values.
---

## 📌 Overview

**CSV Data Analyzer** is a simple data analysis project built with Python and Pandas.

It is designed to demonstrate the fundamental steps involved in working with CSV datasets, including:

* Loading CSV data
* Inspecting dataset structure
* Viewing records
* Generating descriptive statistics
* Detecting missing values

The project uses a sample personal-expense dataset for demonstration purposes. The dataset contains **fictional data** and does not include real or sensitive personal information.

---

## ✨ Features

* 📂 **CSV File Loading** — Reads datasets using Pandas
* 👀 **Data Preview** — Displays the first five records
* 📋 **Dataset Information** — Shows columns, data types, and non-null values
* 📊 **Statistical Analysis** — Generates descriptive statistics
* 🔍 **Missing Value Detection** — Identifies missing values in each column
* 🐍 **Beginner Friendly** — Simple Python code suitable for learning Pandas

---

## 🛠️ Tech Stack

| Technology | Purpose                                |
| ---------- | -------------------------------------- |
| 🐍 Python  | Programming language                   |
| 🐼 Pandas  | Data loading, analysis, and inspection |
| 📄 CSV     | Dataset format                         |

---

## 📁 Project Structure

```text
CSV-Data-Analyzer/
│
├── csv_analyzer.py    # Main Python program
├── data.csv           # Sample expense dataset
└── README.md          # Project documentation
```

---

## 📊 Dataset

The project includes a sample dataset named **`data.csv`**.

The dataset represents fictional personal expense records and may contain information such as:

| Column        | Description                |
| ------------- | -------------------------- |
| `Date`        | Date of the expense        |
| `Category`    | Expense category           |
| `Description` | Description of the expense |
| `Amount`      | Amount spent               |

### Example

```text
Date,Category,Description,Amount
2026-01-01,Food,Grocery Shopping,1200
2026-01-03,Transport,Bus,300
2026-01-05,Shopping,Clothes,2500
2026-01-08,Food,Restaurant,800
```

> **Note:** The sample data is fictional and is included only for demonstration and testing.

---

## ⚙️ Installation

### Prerequisites

Before running the project, make sure you have:

* Python 3.x installed
* Basic knowledge of Python
* Pandas library

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CSV-Data-Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd CSV-Data-Analyzer
```

### 3. Install Dependencies

```bash
pip install pandas
```

If `pip` is not recognized, use:

```bash
python -m pip install pandas
```

---

## ▶️ Usage

Run the Python script using:

```bash
python csv_analyzer.py
```

The program reads `data.csv` and displays the analysis results in the terminal.

---

## 🔍 Analysis Performed

### 1. Load the CSV File

The project uses Pandas to read the CSV dataset.

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

### 2. Display First 5 Rows

```python
print(df.head())
```

This provides a quick preview of the dataset.

### 3. Display Dataset Information

```python
print(df.info())
```

This shows:

* Number of entries
* Column names
* Data types
* Non-null values

### 4. Generate Statistical Summary

```python
print(df.describe())
```

This provides statistics such as:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum
* Quartiles

### 5. Detect Missing Values

```python
print(df.isnull().sum())
```

This identifies the number of missing values in each column.

---

## 💻 Sample Output

A typical execution may produce output similar to:

```text
First 5 Rows:
         Date     Category        Description  Amount
0  2026-01-01         Food   Grocery Shopping    1200
1  2026-01-03    Transport                Bus     300
2  2026-01-05      Shopping            Clothes    2500
3  2026-01-08         Food          Restaurant     800

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries
Columns: 4 entries

Statistical Summary:
             Amount
count      4.000000
mean    1200.000000
min      300.000000
max     2500.000000

Missing Values:
Date            0
Category        0
Description     0
Amount          0
```

---

## 📚 Learning Outcomes

By completing this project, I learned how to:

* Read CSV files using Pandas
* Create and work with Pandas DataFrames
* Inspect dataset structure
* Analyze numerical data
* Generate descriptive statistics
* Identify missing values
* Perform basic data exploration
* Work with Python libraries for data analysis

---

## 🚀 Future Enhancements

The project can be extended with additional data-analysis capabilities:

* 📈 Add visualizations using Matplotlib
* 📊 Create expense-category charts
* 💰 Calculate total and average expenses
* 🔎 Add filtering and sorting options
* 🧹 Implement automatic missing-value handling
* 📅 Perform monthly expense analysis
* 📑 Generate automated analysis reports
* 🖥️ Build a simple web interface using Streamlit

---

## 🎯 Project Purpose

This project was created as a **beginner-level data analysis project** to practice Python and Pandas fundamentals.

It demonstrates the basic workflow of:

```text
CSV Dataset
     ↓
Load Data
     ↓
Inspect Data
     ↓
Analyze Data
     ↓
Check Missing Values
     ↓
Generate Insights
```

---

## 👩‍💻 Author

### Varshitha Pavuluri

Aspiring **Data Analyst** with an interest in data analysis, visualization, Python, SQL, and Business Intelligence.

* 💼 GitHub: [Varshitha Pavuluri](https://github.com/varshi99)
* 🌐 Portfolio: [Portfolio](https://varshitha-pavuluri.netlify.app/)

---

## ⭐ Support

If you found this project useful or helpful for learning Python and Pandas, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for **educational and learning purposes**.
