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

import numpy as np

sales = np.array([42000, 55000, 61000, 48000, 70000, 83000])

#Create a view of sales and change first element to 99999 — print original to see if it changed
#create a copy of sales and change first element to 11111 — print original to see if it changed
#Check if your view and copy are views using .base

view = sales.view()

view[0] = 99999
print('sales after view change:', sales)


copy = sales.copy()
copy[0] = 11111
print('sales after copy change:', sales)

print(view.base is sales)
print(copy.base is sales)

import numpy as np

# 3 months x 4 products
sales = np.array([
    [15000, 22000, 18000, 30000],   # January
    [25000, 30000, 28000, 35000],   # February
    [20000, 27000, 24000, 32000]    # March
])

print(sales.shape)

transposed = sales.T
print('Transposed:')
print(transposed)
print(transposed.shape)

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

swapped = np.swapaxes(data, 0, 1)
print('swapped:', swapped)

import numpy as np

# First half of year
h1 = np.array([42000, 55000, 61000])

# Second half of year
h2 = np.array([48000, 70000, 83000])

# Q1 and Q2 data — 2 products
q1_q2 = np.array([[42000, 31000],
                   [55000, 28000]])

# Q3 and Q4 data — 2 products
q3_q4 = np.array([[61000, 35000],
                   [70000, 40000]])


full_year = np.concatenate([h1, h2])
print("full year :", full_year)
whole  = np.concatenate([q1_q2, q3_q4], axis = 0)
print(whole)

import numpy as np

# 4 quarters x 3 products
revenue = np.array([
    [120000, 85000,  45000],   # Q1
    [135000, 92000,  52000],   # Q2
    [98000,  78000,  48000],   # Q3
    [150000, 105000, 61000]    # Q4
])

sales = np.sum(revenue)
avg_sales = np.average(revenue)


print(sales)

print(np.sum(revenue, axis=1))
print(np.sum(revenue, axis=0))
print(np.mean(revenue, axis=1))

totals= np.sum(revenue, axis=1)
np.argmax(totals)
print(np.argmax(totals))

import numpy as np

employees = ["Rahul", "Priya", "Amit", "Sneha", "Ravi"]
salaries  = np.array([45000, 62000, 58000, 71000, 53000])

highest_paid = np.argmax(salaries)
print(f"Highest paid employee: {employees[highest_paid]} with salary ₹{salaries[highest_paid]}")

import numpy as np

salaries  = np.array([45000, 52000, 61000, 48000, 55000, 70000])
threshold = 55000

print(salaries * 1.12)
print(salaries * 0.90)
print(np.where(salaries > threshold, 'senior', 'junior'))
levels = np.where(salaries > threshold, 'senior', 'junior')
print(sum(levels == "senior"))

import numpy as np

quarters = np.array(["Q1", "Q2", "Q3", "Q4"])
tax_rate = np.array([0.18])
ratings  = np.array([1, 2, 3])

thrice = np.tile(quarters , 3)
print(thrice)
twelve = np.repeat(tax_rate, 12)
print(twelve)
twice = np.repeat(ratings, 2)
print(twice)

import numpy as np

# First half of year — 2 products
h1 = np.array([[42000, 31000],   # Q1
               [55000, 28000]])  # Q2

# Second half of year — 2 products
h2 = np.array([[61000, 35000],   # Q3
               [70000, 40000]])  # Q4

# Third product — all 4 quarters
product3 = np.array([[18000],
                     [22000],
                     [19000],
                     [25000]])

full_year = (np.vstack([h1, h2]))
print('full year:', full_year)

full_yearr = np.hstack([full_year, product3])
print(full_yearr)

print(full_yearr.shape)

students = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [45, 72, 38, 85, 55, 91]

for mark in marks:
    if mark >= 50:
        print(f'{mark} ✅ passed')
    else:
        print(f'{mark} ❌ failed')
        
products = ["Laptop", "Phone", "Tablet"]
prices   = [80000,    45000,   32000]


### Task
#Loop through and print each product with **18% GST added** to the price.

for i in range(len(products)) :
    print(products[i])
    
for i in range(len(products)) :
    print(products[i], prices[i])
    
    for i in range(len(products)) :
        gst_price = prices[i] * 1.18
        print(products[i], gst_price)
        
employees = ["Rahul", "Priya", "Amit", "Sneha", "Ravi"]

for i in range(len(employees)) :
    print(f'{i+1}. {employees[i]}')
    
temperatures = [38, 42, 35, 40, 28, 33, 45]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(len(temperatures)) :
    if temperatures[i] > 37 :
        print(f'{days[i]}: {temperatures[i]} 🔥 Hot')
    else :
        print(f'{days[i]}: {temperatures[i]} ❄️ Cool')

students = ["Rahul", "Priya", "Amit", "Sneha", "Ravi"]
marks    = [45, 82, 38, 91, 55]
for i, name in enumerate(students) :
    mark = marks[i]
    
    if mark >= 90 :
        grade = "A 🌟"
    elif mark >= 75 :
        grade = "B 👍"
    elif mark >= 50 :
        grade = 'c ✅'
    else:
        grade = 'F ❌'
    print(f"{name} → {mark} | Grade: {grade}")
    

sales = np.array([42000, np.nan, 61000, np.nan, 70000])
print('before :', sales)

sales[np.isnan(sales)] = 0
print('after :', sales)

mean = np.nanmean(sales)
print('mean: ', mean)

sales = np.array([42000, np.nan, 61000, np.inf, 70000, np.nan])

print('missing values: ', np.isnan(sales))
print('indefinite values: ', np.isinf(sales))
print('finite values;', np.isfinite(sales))

mean =np.nanmean(sales[np.isfinite(sales)])
sales[np.isinf(sales)] = mean
sales[np.isnan(sales)] = mean

print('cleaned sales:', sales)  
print('average', np.mean(sales))
print('total:', np.sum(sales))

import numpy as np

sales = np.array([42000, np.nan, 61000, np.inf, 70000, np.nan])

print(np.isnan(sales))
print(np.isinf(sales))
print(np.isfinite(sales))

mean = np.nanmean(sales[np.isfinite(sales)])
sales[np.isinf(sales)] = mean
sales[np.isnan(sales)] = mean

print(np.sum(sales))
print(np.mean(sales))

import pandas as pd

fruits = pd.Series(
    [120, 85, 200, 150, 95, 175], name = 'fruit_prices',
    index=["Apple", "Banana", "Grapes", "Orange", "Strawberry", "Mango"]
)

print(fruits.index, fruits.name, fruits.shape)

print(fruits.loc['Grapes'])

print(fruits.iloc[2])

print(fruits.loc['Apple':'Orange'])

print(fruits[fruits > 150])

print(fruits[(fruits >= 100) & (fruits <= 150)])

fruits['Apple'] = 130
print(fruits)

fruits['pineapple'] = 180
print(fruits)