# ============================================
#         PANDAS SERIES CHEATSHEET
# ============================================

import pandas as pd

# ── CREATING A SERIES ────────────────────────

# From a list
s = pd.Series([120, 85, 200, 150, 95])

# From a list with custom index
s = pd.Series(
    [120, 85, 200, 150, 95],
    index=["Apple", "Banana", "Grapes", "Orange", "Strawberry"]
)

# From a list with name
s = pd.Series(
    [120, 85, 200, 150, 95],
    index=["Apple", "Banana", "Grapes", "Orange", "Strawberry"],
    name="Fruit Prices"
)

# From a dictionary
data = {"Apple": 120, "Banana": 85, "Grapes": 200}
s = pd.Series(data)

# From a tuple
data = (120, 85, 200, 150, 95)
s = pd.Series(data)

# ── SERIES PROPERTIES ────────────────────────

s.dtype     # data type        → int64, float64, object
s.index     # index values     → ['Apple', 'Banana'...]
s.name      # series name      → "Fruit Prices"
s.shape     # shape            → (5,)
s.size      # total elements   → 5
s.values    # just the values  → [120 85 200 150 95]

# ── CHANGING INDEX ───────────────────────────

s.index = ["Apple", "Banana", "Grapes", "Orange", "Strawberry"]

# ── ACCESSING VALUES ─────────────────────────

# iloc → access by POSITION number
s.iloc[0]       # first item
s.iloc[-1]      # last item
s.iloc[2]       # third item
s.iloc[0:4]     # first 4 items

# loc → access by LABEL name
s.loc["Apple"]          # single item by label
s.loc["Apple":"Grapes"] # range by label

# RC Rule
# iloc → position number  → s.iloc[0]
# loc  → label name       → s.loc["Apple"]

# ── CONDITIONAL SELECTION ────────────────────

s[s > 150]              # values above 150
s[s < 100]              # values below 100
s[s == 200]             # values equal to 200

# ── LOGICAL OPERATORS ────────────────────────

# AND → both conditions must be true
s[(s >= 100) & (s <= 175)]

# OR → at least one condition must be true
s[(s < 100) | (s > 175)]

# NOT → reverse the condition
s[~(s > 150)]

# IMPORTANT: Always use [] not () for filtering!
# s[condition]   ✅ correct
# s(condition)   ❌ wrong

# ── MODIFYING A SERIES ───────────────────────

# Change a value
s["Apple"] = 130

# Add a new value
s["Pineapple"] = 220

# Delete a value
s = s.drop("Pineapple")

# Apply math to entire series
s = s * 1.10     # 10% increase to all values

# ── CREATE FROM DICT AND TUPLE ───────────────

# Dictionary → keys become index automatically
data = {"Jan": 42000, "Feb": 55000, "Mar": 61000}
s = pd.Series(data)

# Tuple → needs manual index
data = (42000, 55000, 61000)
s = pd.Series(data, index=["Jan", "Feb", "Mar"])

# ── QUICK REFERENCE ──────────────────────────

# CREATING
# pd.Series(list)              → from list
# pd.Series(dict)              → from dictionary
# pd.Series(tuple)             → from tuple

# PROPERTIES
# s.dtype                      → data type
# s.index                      → index values
# s.name                       → series name
# s.shape                      → shape
# s.values                     → just values

# ACCESSING
# s.iloc[0]                    → by position
# s.loc["Apple"]               → by label
# s.iloc[0:4]                  → slice by position

# FILTERING
# s[s > 150]                   → above 150
# s[(s>=100) & (s<=175)]       → between 100 and 175
# s[(s<100) | (s>175)]         → outside range
# s[~(s > 150)]                → NOT above 150

# MODIFYING
# s["Apple"] = 130             → change value
# s["Pineapple"] = 220         → add new value
# s.drop("Apple")              → delete value
# s * 1.10                     → math on entire series

# ============================================
