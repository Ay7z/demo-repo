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

