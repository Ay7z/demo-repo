# ============================================
#       PANDAS DATAFRAME CHEATSHEET
#       Including Brackets Guide!
# ============================================

import pandas as pd

# ── CREATING A DATAFRAME ─────────────────────

# From dictionary — most common
data = {
    "Name":       ["Rahul", "Priya", "Amit"],   # {} for dict
    "Age":        [25, 28, 32],                  # [] for list
    "Department": ["Sales", "Marketing", "Tech"],
    "Salary":     [45000, 52000, 61000]
}
df = pd.DataFrame(data)   # () for function call

# From CSV file
df = pd.read_csv("file.csv")

# From Excel file
df = pd.read_excel("file.xlsx")

# ── BRACKETS GUIDE ───────────────────────────

# () → function calls
df.head()
df.info()
df.describe()
df.isnull()
df.value_counts()

# [] → accessing columns and filtering
df["Salary"]                    # single column
df[["Name", "Salary"]]          # multiple columns
df[df["Salary"] > 50000]        # filtering

# {} → creating dictionaries
data = {"Name": "Rahul", "Age": 25}
df.rename(columns={"Department": "Dept"}, inplace=True)

# COMMON MISTAKE:
# df("Salary")   ❌ wrong — () means function call
# df["Salary"]   ✅ right — [] means access column

# ── PROPERTIES ───────────────────────────────

df.shape        # (6, 4)  → rows and columns
df.columns      # column names
df.index        # row index
df.dtypes       # data type of each column
df.size         # total elements

# ── EXPLORING ────────────────────────────────

df.head()       # first 5 rows
df.head(3)      # first 3 rows
df.tail()       # last 5 rows
df.tail(2)      # last 2 rows
df.info()       # full summary
df.describe()   # statistics (mean, min, max etc)

# ── ACCESSING COLUMNS ────────────────────────

df["Salary"]              # single column → Series
df[["Name", "Salary"]]    # multiple columns → DataFrame

# ── ILOC — POSITION BASED ────────────────────

df.iloc[0]          # first row
df.iloc[-1]         # last row
df.iloc[1:4]        # rows 1 to 3
df.iloc[1:4, :2]    # rows 1-3, first 2 columns
df.iloc[:, 0]       # all rows, first column

# ── LOC — LABEL BASED ────────────────────────

df.loc[0]                        # row by index
df.loc[0:2]                      # rows 0 to 2
df.loc[:, "Salary"]              # all rows, Salary column
df.loc[0:2, "Name":"Age"]        # rows 0-2, Name to Age

# ── CONDITIONAL SELECTION ────────────────────

df.loc[df["Salary"] > 50000]              # salary above 50000
df.loc[df["Department"] == "Sales"]       # Sales dept only
df.loc[df["Age"] % 2 == 0, "Age"]         # even ages only

# Multiple conditions
df.loc[(df["Salary"] > 50000) & (df["Dept"] == "Tech")]   # AND
df.loc[(df["Salary"] < 50000) | (df["Dept"] == "Tech")]   # OR

# ── MISSING VALUES ───────────────────────────

df.isnull()           # True/False for every cell
df.isnull().sum()     # count missing per column ← most useful!

# ── MODIFYING ────────────────────────────────

# Modify existing column
df["Salary"] = df["Salary"] + 10000      # add bonus
df["Salary"] = df["Salary"] * 1.10       # 10% raise

# Add new column
df["Tax"]              = df["Salary"] * 0.10   # 10% tax
df["Promotion Salary"] = df["Salary"] * 2      # double salary
df["Level"]            = df["Salary"].apply(lambda x: "Senior" if x > 55000 else "Junior")

# Rename column
df.rename(columns={"Department": "Dept"}, inplace=True)
# inplace=True → saves change permanently ✅
# without inplace=True → change is lost! ❌

# ── ANALYSIS ─────────────────────────────────

df["Dept"].unique()         # all unique values
df["Dept"].value_counts()   # count of each value

# ── PERCENTAGE REMINDER ──────────────────────

# 10% → * 0.10   NOT * 10 !!
# 18% → * 0.18
# 20% → * 0.20
# 10% increase → * 1.10
# 20% decrease → * 0.80

# ── BRACKETS QUICK REFERENCE ─────────────────

# ()  → function calls        → df.head()
# []  → column access/filter  → df["Salary"]
# {}  → dictionaries          → {"col": "new_col"}
# [[]]→ multiple columns      → df[["Name","Salary"]]

# FILTERING RULE:
# df[df["col"] > value]       ✅ always use []
# df(df["col"] > value)       ❌ never use ()

# ============================================
# ============================================
#    PANDAS DATA CLEANING & MERGING
#         CHEATSHEET
#    ⭐ = Most used in DA/DS jobs
# ============================================

import pandas as pd
import numpy as np

# ── 1. FINDING MISSING VALUES ────────────────

df.isnull()              # True/False for every cell
df.isnull().sum()        # ⭐ count missing per column
df.isnull().sum().sum()  # total missing in entire df
df.notnull()             # opposite of isnull()

# ── 2. DROPPING MISSING VALUES ───────────────

df.dropna()                      # drop rows with ANY missing
df.dropna(how="all")             # drop rows where ALL values missing
df.dropna(how="any")             # drop rows where ANY value missing
df.dropna(subset=["Age"])        # drop rows where Age is missing

# ── 3. FILLING MISSING VALUES ────────────────

df.fillna(0)                                    # fill ALL with 0
df["Age"].fillna(0, inplace=True)               # fill column with 0
df["Age"].fillna(df["Age"].mean(), inplace=True)      # ⭐ fill with mean
df["Sal"].fillna(df["Sal"].median(), inplace=True)    # ⭐ fill with median
df["col"].fillna(method="ffill", inplace=True)  # fill from PREVIOUS row
df["col"].fillna(method="bfill", inplace=True)  # fill from NEXT row

# WHEN TO USE WHICH:
# mean()   → best for normal data (salaries, ages)
# median() → best for skewed data (house prices, income)
# ffill()  → best for time series (stock prices, dates)
# bfill()  → best for time series (fill from future value)
# 0        → best for counts (missing = no sales = 0)

# ── 4. REPLACING VALUES ──────────────────────

df["Name"].replace("Rose", "Charlie", inplace=True)   # ⭐ single replace
df["Dept"].replace({                                   # multiple replace
    "HR": "Human Resources",
    "IT": "Information Technology"
}, inplace=True)

# ── 5. ADDING NEW ROW ────────────────────────

df.loc[len(df)] = ["Alice", 24, "HR", 60000]   # add row at end
#        ↑
#    len(df) = next available index

# ── 6. DUPLICATES ────────────────────────────

df[df.duplicated()]                    # ⭐ find duplicate rows
df[df.duplicated(keep="first")]        # mark later duplicates
df[df.duplicated(keep="last")]         # mark earlier duplicates
df[df.duplicated(keep=False)]          # mark ALL duplicates

df.drop_duplicates()                   # ⭐ remove duplicates
df.drop_duplicates(subset=["Name"])    # remove based on column
df.drop_duplicates(inplace=True)       # save changes

# ── 7. CONCATENATION ─────────────────────────

pd.concat([df1, df2])              # ⭐ stack vertically (more rows)
pd.concat([df1, df2], axis=0)      # same as above
pd.concat([df1, df2], axis=1)      # stack horizontally (more cols)
pd.concat([df1, df2], ignore_index=True)  # reset index after concat

# ── 8. MERGE ─────────────────────────────────

# Same column name in both dataframes
pd.merge(df1, df2, on="Dept")

# Different column names
pd.merge(df1, df2,
         left_on="Dept",           # ⭐ column in LEFT df
         right_on="Department")    # ⭐ column in RIGHT df

# Types of merge
pd.merge(df1, df2, on="Dept", how="inner")  # ⭐ only matching rows
pd.merge(df1, df2, on="Dept", how="left")   # all left + matching right
pd.merge(df1, df2, on="Dept", how="right")  # all right + matching left
pd.merge(df1, df2, on="Dept", how="outer")  # all rows from both

# ── MOST USED IN DA/DS JOBS ──────────────────

# ⭐⭐⭐ USE EVERY DAY
# df.isnull().sum()                 → find missing values
# df["col"].fillna(mean/median)     → fill missing values
# df.drop_duplicates()              → remove duplicates
# pd.concat([df1, df2])             → combine dataframes
# pd.merge(df1, df2, on="col")      → join dataframes

# ⭐⭐ USE OFTEN
# df.dropna()                       → drop missing rows
# df["col"].replace("old","new")    → fix wrong values
# df.loc[len(df)] = [values]        → add new row
# df[df.duplicated()]               → find duplicates

# ⭐ USE OCCASIONALLY
# fillna(method="ffill/bfill")      → time series filling
# pd.concat(axis=1)                 → horizontal stacking
# drop_duplicates(subset=["col"])   → targeted dedup

# ── DA VS DS USAGE ───────────────────────────

# DATA ANALYST uses most:
# → isnull().sum()      finding data quality issues
# → fillna(mean/median) cleaning missing values
# → drop_duplicates()   removing duplicate records
# → pd.merge()          combining sales/customer data
# → replace()           fixing wrong entries

# DATA SCIENTIST uses most:
# → fillna(mean/median) preparing data for ML models
# → drop_duplicates()   ensuring clean training data
# → pd.concat()         combining multiple datasets
# → pd.merge()          joining feature datasets
# → isnull().sum()      checking data quality

# ── CONCAT VS MERGE ──────────────────────────

# concat → stacking dataframes
#          same structure, more data
#          like adding more rows/cols

# merge  → joining on matching values
#          like VLOOKUP in Excel
#          like JOIN in SQL

# ── FILL VALUE GUIDE ─────────────────────────

# Numbers (salary, age)  → mean or median
# Categories (dept)      → mode (most common value)
# Time series            → ffill or bfill
# Counts (sales)         → 0
# ============================================
