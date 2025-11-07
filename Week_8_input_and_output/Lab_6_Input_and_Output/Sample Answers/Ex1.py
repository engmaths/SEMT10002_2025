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

    print(data_list)


total_annual_rainfall = '???'
average_monthly_rainfall = '???'
maximum_monthly_rainfall = '???'
minimum_monthly_rainfall = '???'