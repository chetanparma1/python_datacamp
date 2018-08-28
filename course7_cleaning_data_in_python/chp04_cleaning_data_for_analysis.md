# Chapter 04: Cleaning Data for Analysis

## 01. Converting data types
In this exercise, you'll see how ensuring all categorical variables in a DataFrame are of type category reduces memory usage.

The tips dataset has been loaded into a DataFrame called tips. This data contains information about how much a customer tipped, whether the customer was male or female, a smoker or not, etc.

Look at the output of tips.info() in the IPython Shell. You'll note that two columns that should be categorical - sex and smoker - are instead of type object, which is pandas' way of storing arbitrary strings. Your job is to convert these two columns to type category and note the reduced memory usage.

### Instructions:
* Convert the sex column of the tips DataFrame to type 'category' using the .astype() method.
* Convert the smoker column of the tips DataFrame.
* Print the memory usage of tips after converting the data types of the columns. Use the .info() method to do this.

#### Script
```
# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())
```

##### Output
```
In [2]: tips.head()
Out[2]: 
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 7 columns):
    total_bill    244 non-null float64
    tip           244 non-null float64
    sex           244 non-null category
    smoker        244 non-null category
    day           244 non-null object
    time          244 non-null object
    size          244 non-null int64
    dtypes: category(2), float64(2), int64(1), object(2)
    memory usage: 10.1+ KB
    None
```
##### Comment:
Excellent! By converting sex and smoker to categorical variables, the memory usage of the DataFrame went down from 13.4 KB to 10.1KB. This may seem like a small difference here, but when you're dealing with large datasets, the reduction in memory usage can be very significant!

## 02. Working with numeric data
If you expect the data type of a column to be numeric (int or float), but instead it is of type object, this typically means that there is a non numeric value in the column, which also signifies bad data.

You can use the pd.to_numeric() function to convert a column into a numeric data type. If the function raises an error, you can be sure that there is a bad value within the column. You can either use the techniques you learned in Chapter 1 to do some exploratory data analysis and find the bad value, or you can choose to ignore or coerce the value into a missing value, NaN.

A modified version of the tips dataset has been pre-loaded into a DataFrame called tips. For instructional purposes, it has been pre-processed to introduce some 'bad' data for you to clean. Use the .info() method to explore this. You'll note that the total_bill and tip columns, which should be numeric, are instead of type object. Your job is to fix this.

### Instrutions;
* Use pd.to_numeric() to convert the 'total_bill' column of tips to a numeric data type. Coerce the errors to NaN by specifying the keyword argument errors='coerce'.
* Convert the 'tip' column of 'tips' to a numeric data type exactly as you did for the 'total_bill' column.
* Print the info of tips to confirm that the data types of 'total_bill' and 'tips' are numeric.

#### Script
```
# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors = 'coerce')

# Print the info of tips
print(tips.info())
```
##### Output
```
In [1]: tips.head()
Out[1]: 
  total_bill   tip     sex smoker  day    time  size
0      16.99  1.01  Female     No  Sun  Dinner   2.0
1    missing  1.66    Male    NaN  Sun  Dinner   3.0
2      21.01   3.5    Male     No  Sun  Dinner   3.0
3      23.68  3.31    Male     No  Sun  Dinner   2.0
4      24.59  3.61  Female     No  Sun  Dinner   4.0

In [2]: tips.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
total_bill    244 non-null object
tip           244 non-null object
sex           234 non-null category
smoker        229 non-null category
day           243 non-null category
time          227 non-null category
size          231 non-null float64
dtypes: category(4), float64(1), object(2)
memory usage: 6.9+ KB
```
##### Comment
Great work! The 'total_bill' and 'tip' columns in this DataFrame are stored as object types because the string 'missing' is used in these columns to encode missing values. By coercing the values into a numeric type, they become proper NaN values.
