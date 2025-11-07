'''
====================
Exercise 1
====================

1. Import the file rainfall.csv
2. Compute:
    - the total annual rainfall 
    - the average monthly rainfall
    - the maximum and minimum monthly rainfall 

'''

import csv

with open('rainfall.csv') as file:

    data = csv.reader(file)

    data_list = list(data)

# List to store rainfall values
monthly_rainfall = []

# Convert string representation of rainfall values to numerical data
for ii in data_list[1]:
    monthly_rainfall.append(float(ii))

total_annual_rainfall = sum(monthly_rainfall)
average_monthly_rainfall = total_annual_rainfall / len(monthly_rainfall)
maximum_monthly_rainfall = max(monthly_rainfall)
minimum_monthly_rainfall = min(monthly_rainfall)

print('total annual rainfall:', total_annual_rainfall)
print('the average monthly rainfall:', average_monthly_rainfall)
print('the maximummonthly rainfall:', maximum_monthly_rainfall)
print('the minimum monthly rainfall:', minimum_monthly_rainfall)