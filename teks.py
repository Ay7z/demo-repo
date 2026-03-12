import numpy as np

# 12 months of revenue for a clothing store
revenue = np.array([55000, 62000, 48000,
                    71000, 83000, 79000,
                    66000, 74000, 88000,
                    91000, 95000, 110000])

months = revenue.reshape(3,4)
print(months)

print(months.shape)

print(months[1])

print(months.ravel())

products  = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
revenue   = np.array([200000, 150000, 80000, 60000, 30000])
costs     = np.array([140000, 105000, 56000, 42000, 21000])

profit = revenue - costs
print(profit)
profit_margin = profit/revenue*100
print('margin:',profit_margin)
forecast = revenue*1.15
print('forecast:', forecast)

import numpy as np

data    = np.array([4, 16, 25, 36, 64, 100])
angles  = np.array([0, 30, 45, 60, 90])
growth  = np.array([1, 2, 3, 4, 5])

print(np.sqrt(data))

radians= np.radians(angles)
print(np.sin(radians))
print(np.exp(growth))

import numpy as np

# 4 quarters x 3 products (Laptop, Phone, Tablet)
sales = np.array([
    [42000, 31000, 18000],   # Q1
    [55000, 28000, 22000],   # Q2
    [61000, 35000, 19000],   # Q3
    [70000, 40000, 25000]    # Q4
])

print(sales[1])
print(sales[:,1])
print(sales[2,2])

print(sales[1:3, 0:2])

salaries = np.array([
    [45000, 52000, 48000, 51000],   # Sales
    [62000, 58000, 65000, 60000],   # Tech
    [38000, 42000, 40000, 45000]    # Support
])

target = 50000

for item in np.nditer(salaries):

    if item > target:
        print(f"₹{item} ✅ Above target")
    else:
        print(f"₹{item} ❌ Below target")


