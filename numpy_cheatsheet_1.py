# ============================================
#         NUMPY COMPLETE CHEATSHEET
#         Updated after completing NumPy
# ============================================

import numpy as np

# ── 1. ARRAY CREATION ────────────────────────

a = np.array([1, 2, 3, 4, 5])               # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]])        # 2D array
c = np.arange(1, 13)                         # [1, 2, 3 ... 12]
d = np.linspace(0, 100, 5)                  # 5 evenly spaced numbers
e = np.zeros(5)                              # [0. 0. 0. 0. 0.]
f = np.ones(5)                               # [1. 1. 1. 1. 1.]
g = np.random.randint(1000, 9999, size=6)   # 6 random numbers

# ── ARRAY PROPERTIES ─────────────────────────

a.shape    # shape of array         → (5,) or (3,4)
a.dtype    # data type              → int64, float64
a.size     # total elements         → 5
a.ndim     # number of dimensions   → 1 or 2

# ── 2. RESHAPE & RAVEL ───────────────────────

sales = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

quarterly = sales.reshape(4, 3)   # 4 rows x 3 cols (4x3 MUST = 12)
flat      = quarterly.ravel()     # flatten back to 1D

# ── 3. ARITHMETIC OPERATIONS ─────────────────

revenue = np.array([100000, 150000, 130000])
costs   = np.array([70000,  95000,  85000])

profit   = revenue - costs          # subtract arrays
margin   = (profit / revenue) * 100 # percentage
forecast = revenue * 1.15           # 15% growth (1 + 0.15)

# Growth shortcuts
# 10% increase → multiply by 1.10
# 15% increase → multiply by 1.15
# 20% increase → multiply by 1.20
# 10% decrease → multiply by 0.90
# 20% decrease → multiply by 0.80

# ── 4. UFUNCS ────────────────────────────────

data    = np.array([4, 16, 25, 36, 64, 100])
angles  = np.array([0, 30, 45, 60, 90])
numbers = np.array([1, 2, 3, 4, 5])

# Math ufuncs
np.sqrt(data)                    # square root
np.sin(np.radians(angles))       # sine (always convert to radians first!)
np.exp(numbers)                  # exponential (e^x)
np.abs(numbers)                  # remove negative signs
np.round(numbers, 1)             # round to 1 decimal place

# Statistics ufuncs
np.sum(data)                     # total
np.mean(data)                    # average
np.max(data)                     # highest value
np.min(data)                     # lowest value
np.median(data)                  # middle value
np.std(data)                     # spread of data
np.argmax(data)                  # index of highest value
np.argmin(data)                  # index of lowest value
np.percentile(data, 75)          # 75th percentile

# ── 5. INDEXING & SLICING ────────────────────

sales = np.array([42000, 55000, 61000, 48000, 70000, 83000])

# 1D indexing
sales[0]      # first element
sales[-1]     # last element
sales[2]      # third element

# 1D slicing
sales[1:4]    # index 1 to 3 (not 4!)
sales[:3]     # first 3 elements
sales[3:]     # from index 3 to end

# 2D indexing & slicing (RC Rule — Row first, Column second)
table = np.array([
    [42000, 31000, 18000],   # Row 0 → Q1
    [55000, 28000, 22000],   # Row 1 → Q2
    [61000, 35000, 19000],   # Row 2 → Q3
    [70000, 40000, 25000]    # Row 3 → Q4
])

table[0]         # entire first row  (Q1)
table[1]         # entire second row (Q2)
table[:, 0]      # entire first column (Laptop)
table[:, 1]      # entire second column (Phone)
table[2][2]      # single value → Row 2, Col 2 (Q3, Tablet)
table[1:3, 0:2]  # rows 1-2, cols 0-1 (Q2&Q3, Laptop&Phone)

# TRICK TO REMEMBER
# RC Cola → Row first, Column second → table[ROW, COLUMN]
# :       → means everything/all
# [1:3]   → start AT 1, stop BEFORE 3

# ── 6. NDITER ────────────────────────────────

salaries = np.array([
    [45000, 52000, 48000],
    [62000, 58000, 65000]
])

target = 50000

# Loop through every element of any dimension array
for item in np.nditer(salaries):
    if item > target:
        print(f"₹{item} ✅ Above target")
    else:
        print(f"₹{item} ❌ Below target")

# ── 7. NP.WHERE (IF logic) ───────────────────

sales = np.array([42000, 55000, 61000, 48000, 70000])

# Like Excel's IF function
status = np.where(sales > 60000, "✅ Hit", "❌ Missed")

# Nested conditions (like elif)
grades = np.where(sales >= 75000, "Excellent",
         np.where(sales >= 55000, "Good", "Poor"))

# ── 8. CORRELATION ───────────────────────────

ad_spend = np.array([10000, 15000, 20000, 25000])
revenue  = np.array([42000, 51000, 61000, 70000])

correlation = np.corrcoef(ad_spend, revenue)[0][1]
# +1.0 = perfect positive relationship
#  0.0 = no relationship
# -1.0 = perfect negative relationship

# ============================================
#   PROPERTIES vs FUNCTIONS — KEY DIFFERENCE
# ============================================

# PROPERTIES (no brackets) → just reading info
# array.shape
# array.dtype
# array.size
# array.ndim

# FUNCTIONS (need brackets) → doing something
# array.reshape(4, 3)
# array.ravel()
# np.mean(array)
# np.sum(array)

# ============================================
# ============================================
#         NUMPY PART 2 CHEATSHEET
# ============================================

import numpy as np

# 1. VIEWS VS COPY
original = np.array([10, 20, 30, 40, 50])
view = original.view()    # shares memory - change view = original changes!
copy = original.copy()    # independent  - change copy = original safe!
print(view.base is original)   # True  = VIEW
print(copy.base is original)   # False = COPY
# Always use .copy() when modifying data!

# 2. TRANSPOSE
sales = np.array([[42000, 31000, 18000],
                  [55000, 28000, 22000]])
transposed = sales.T            # shortcut
transposed = sales.transpose()  # longer way
# Shape flips! (3,4) becomes (4,3)

# 3. SWAPAXES
swapped = sales.swapaxes(0, 1)  # same as .T for 2D
# axis 0 = rows, axis 1 = columns

# 4. CONCATENATION
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
np.concatenate([a, b])           # 1D join
np.concatenate([a, b], axis=0)   # add rows
np.concatenate([a, b], axis=1)   # add columns

# 5. AGGREGATE FUNCTIONS
revenue = np.array([[120000, 85000],
                    [135000, 92000],
                    [98000,  78000]])
np.sum(revenue)            # total everything
np.sum(revenue, axis=1)    # total per ROW    (per quarter)
np.sum(revenue, axis=0)    # total per COLUMN (per product)
np.mean(revenue, axis=1)   # average per quarter
np.mean(revenue, axis=0)   # average per product
np.argmax(revenue)         # index of highest
# axis=0 = down columns, axis=1 = across rows

# 6. VECTORIZATION
salaries = np.array([45000, 52000, 61000, 48000, 55000])
increased = salaries * 1.12                              # 12% increase
after_tax = salaries * 0.90                              # 10% deduction
labels    = np.where(salaries > 55000, "Senior", "Junior")  # no loop needed

# 7. REPEAT & TILE
a = np.array([1, 2, 3])
np.repeat(a, 3)   # [1 1 1 2 2 2 3 3 3] each element repeated
np.tile(a, 3)     # [1 2 3 1 2 3 1 2 3] entire array repeated

# 8. VSTACK & HSTACK
h1 = np.array([[42000, 31000],
               [55000, 28000]])
h2 = np.array([[61000, 35000],
               [70000, 40000]])
product3 = np.array([[18000],
                     [22000],
                     [19000],
                     [25000]])

full_year = np.vstack([h1, h2])          # add rows    (4,2)
complete  = np.hstack([full_year, product3])  # add columns (4,3)

# vstack = np.concatenate(axis=0)
# hstack = np.concatenate(axis=1)

# ============================================