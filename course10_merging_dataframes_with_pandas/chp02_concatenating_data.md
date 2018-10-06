# Chapter 02: Concatenating Data

## 01. Appending Series with nonunique Indices
The Series bronze and silver, which have been printed in the IPython Shell, represent the 5 countries that won the most bronze and silver Olympic medals respectively between 1896 & 2008. The Indexes of both Series are called Country and the values are the corresponding number of medals won.

If you were to run the command combined = bronze.append(silver), how many rows would combined have? And how many rows would combined.loc['United States'] return? Find out for yourself by running these commands in the IPython Shell.

### Possible Answers
* combined has 5 rows and combined.loc['United States'] is empty (0 rows).
press 1
* combined has 10 rows and combined.loc['United States'] has 2 rows.
press 2
* combined has 6 rows and combined.loc['United States'] has 1 row.
press 3
* combined has 5 rows and combined.loc['United States'] has 2 rows.
press 4

#### Script:
```
bronze
Country
United States     1052.0
Soviet Union       584.0
United Kingdom     505.0
France             475.0
Germany            454.0
Name: Total, dtype: float64

silver
Country
United States     1195.0
Soviet Union       627.0
United Kingdom     591.0
France             461.0
Italy              394.0
Name: Total, dtype: float64

In [1]: combined = bronze.append(silver)

In [2]: combined.loc['United States']
Out[2]: 
Country
United States    1052.0
United States    1195.0
Name: Total, dtype: float64
```

#### Answer:
2

#### Comment:
Correct! The combined Series has 10 rows and combined.loc['United States'] has two rows, since the index value 'United States' occurs in both series bronze and silver.

## 02. Appending pandas Series
In this exercise, you'll load sales data from the months January, February, and March into DataFrames. Then, you'll extract Series with the 'Units' column from each and append them together with method chaining using .append().

To check that the stacking worked, you'll print slices from these Series, and finally, you'll add the result to figure out the total units sold in the first quarter.

### Instructions:
* Read the files 'sales-jan-2015.csv', 'sales-feb-2015.csv' and 'sales-mar-2015.csv' into the DataFrames jan, feb, and mar respectively.
* Use parse_dates=True and index_col='Date'.
* Extract the 'Units' column of jan, feb, and mar to create the Series jan_units, feb_units, and mar_units respectively.
* Construct the Series quarter1 by appending feb_units to jan_units and then appending mar_units to the result. Use chained calls to the .append() method to do this.
* Verify that quarter1 has the individual Series stacked vertically. To do this:
* Print the slice containing rows from jan 27, 2015 to feb 2, 2015.
* Print the slice containing rows from feb 26, 2015 to mar 7, 2015.
* Compute and print the total number of units sold from the Series quarter1. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv', index_col='Date', parse_dates=True)

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv', index_col='Date', parse_dates=True)

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv', index_col='Date', parse_dates=True)

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015':'march 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())
```
#### Output:
```
<script.py> output:
    Date
    2015-01-27 07:11:55    18
    2015-02-02 08:33:01     3
    2015-02-02 20:54:49     9
    Name: Units, dtype: int64
    Date
    2015-02-26 08:57:45     4
    2015-02-26 08:58:51     1
    2015-03-06 10:11:45    17
    2015-03-06 02:03:56    17
    Name: Units, dtype: int64
    642
```
#### Comment:
Well done! As you can see, appending pandas Series is very straightforward!
