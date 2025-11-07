'''
================
Exercise 4
================

Write a program that:

1. Accepts multiple command-line arguments: 
        python3 analyze_data.py <input_file> <output_file> <operation>

        <input_file> : the name of a CSV file containing numeric data.    
        <output_file> : the name of the file to save the results.
        <operation> : a mathematical operation to perform on each column (sum, mean, or standard deviation). 

    Example terminal command:
        python3 Ex4.py data.csv results.csv mean

2. Reads numeric data from the input CSV file using the csv module.

3. Performs the specified operation on each numeric column.

4. Writes the results to the output CSV file.

5. Displays a summary message in the terminal.
'''