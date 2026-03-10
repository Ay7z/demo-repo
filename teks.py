try:
    import numpy as np
except ImportError:
    print("Error: numpy is not installed. Please install it using 'pip install numpy'")
    exit()

#1d array
sales = np.array([42000,55000,61000,48000,70000])
print(sales)

monthly_sales = np.array([
    [258,369,698], #january
    [369,258,698], #february
    [698,258,369]  #march    
])
print (monthly_sales)

yearly_sales = np.array([
    [6555],   #2020
    [7555],   #2021
    [7000],   #2022
])
print(yearly_sales)

zeros = np.zeros(5)
print(zeros)

sales = np.array([42000, 55000, 61000, 48000, 70000, 83000])
print (sales[2])
print (sales[0:6])

import numpy as np

data = np.array([
    [42000, 31000, 18000],
    [55000, 28000, 22000],
    [61000, 35000, 19000]
])

print(data.shape)   # (3, 3) → 3 rows, 3 columns
print(data.ndim)    # 2      → 2 dimensional
print(data.size)    # 9      → total 9 elements
print(data.dtype)   # int64  → data type (integer)