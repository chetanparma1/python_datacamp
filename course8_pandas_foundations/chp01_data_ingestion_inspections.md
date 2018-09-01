# Chapter 01: Data Ingestion andn Inspection

## 01. Inspecting your data
You can use the DataFrame methods .head() and .tail() to view the first few and last few rows of a DataFrame. In this exercise, we have imported pandas as pd and loaded population data from 1960 to 2014 as a DataFrame df. This dataset was obtained from the World Bank.

Your job is to use df.head() and df.tail() to verify that the first and last rows match a file on disk. In later exercises, you will see how to extract values from DataFrames with indexing, but for now, manually copy/paste or type values into assignment statements where needed. Select the correct answer for the first and last values in the 'Year' and 'Total Population' columns.

### Instructions
* First: 1980, 26183676.0; Last: 2000, 35.   			&emsp;&emsp;  	press 1
* First: 1960, 92495902.0; Last: 2014, 15245855.0.		&emsp;&emsp;	press 2
* First: 40.472, 2001; Last: 44.5, 1880.				&emsp;&emsp; 	press 3
* First: CSS, 104170.0; Last: USA, 95.203.				&emsp;&emsp;	press 4

#### Script
```
In [4]: df.Year.head()
Out[4]: 
0    1960
1    1960
2    1960
3    1960
4    1960
Name: Year, dtype: int64

In [5]: df.Year.tail()
Out[5]: 
13369    2014
13370    2014
13371    2014
13372    2014
13373    2014
Name: Year, dtype: int64
```

##### Answer:
2

##### Comment:
Great work! It's essential to inspect your data like this after you read it in.

## 02. DataFrame data types
Pandas is aware of the data types in the columns of your DataFrame. It is also aware of null and NaN ('Not-a-Number') types which often indicate missing data. In this exercise, we have imported pandas as pd and read in the world population data which contains some NaN values, a value often used as a place-holder for missing or otherwise invalid data entries. Your job is to use df.info() to determine information about the total count of non-null entries and infer the total count of 'null' entries, which likely indicates missing data. Select the best description of this data set from the following:

### Instructions
* The data is all of type float64 and none of it is missing.  &emsp;&emsp;  press 1
* The data is of mixed type, and 9914 of it is missing.   &emsp;&emsp;   press 2
* The data is of mixed type, and 3460 float64s are missing.   &emsp;&emsp;   press 3
* The data is all of type float64, and 3460 float64s are missing.   &emsp;&emsp;   press 4

#### Script & Output
```
In [2]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 13374 entries, 0 to 13373
Data columns (total 5 columns):
CountryName                      13374 non-null object
CountryCode                      13374 non-null object
Year                             13374 non-null int64
Total Population                 9914 non-null float64
Urban population (% of total)    13374 non-null float64
dtypes: float64(2), int64(1), object(2)
memory usage: 522.5+ KB
```
##### Answer:
3

##### Comment:
Well done! You'll learn how to deal with missing values later on in this course..

## 03. NumPy and pandas working together
Pandas depends upon and interoperates with NumPy, the Python library for fast numeric array computations. For example, you can use the DataFrame attribute .values to represent a DataFrame df as a NumPy array. You can also pass pandas data structures to NumPy methods. In this exercise, we have imported pandas as pd and loaded world population data every 10 years since 1960 into the DataFrame df. This dataset was derived from the one used in the previous exercise.

Your job is to extract the values and store them in an array using the attribute .values. You'll then use those values as input into the NumPy np.log10() method to compute the base 10 logarithm of the population values. Finally, you will pass the entire pandas DataFrame into the same NumPy np.log10() method and compare the results.

### Instructions:
* Import numpy using the standard alias np.
* Assign the numerical values in the DataFrame df to an array np_vals using the attribute values.
* Pass np_vals into the NumPy method log10() and store the results in np_vals_log10.
* Pass the entire df DataFrame into the NumPy method log10() and store the results in df_log10.
* Inspect the output of the print() code to see the type() of the variables that you created.

#### Script
```
# Import numpy
import numpy as np

# Create array of DataFrame values: np_vals
np_vals = df.values

# Create new array of base 10 logarithm values: np_vals_log10
np_vals_log10 = np.log10(np_vals)

# Create array of new DataFrame by passing df to np.log10(): df_log10
df_log10 = np.log10(df)

# Print original and new data containers
[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]
```

##### Output
```
<script.py> output:
    np_vals has type <class 'numpy.ndarray'>
    np_vals_log10 has type <class 'numpy.ndarray'>
    df has type <class 'pandas.core.frame.DataFrame'>
    df_log10 has type <class 'pandas.core.frame.DataFrame'>
```

##### Comment
Wonderful work! As a data scientist, you'll frequently interact with NumPy arrays, pandas Series, and pandas DataFrames, and you'll leverage a variety of NumPy and pandas methods to perform your desired computations. Understanding how NumPy and pandas work together will prove to be very useful.

## 04. Zip lists to build a DataFrame
In this exercise, you're going to make a pandas DataFrame of the top three countries to win gold medals since 1896 by first building a dictionary. list_keys contains the column names 'Country' and 'Total'. list_values contains the full names of each country and the number of gold medals awarded. The values have been taken from Wikipedia.

Your job is to use these lists to construct a list of tuples, use the list of tuples to construct a dictionary, and then use that dictionary to construct a DataFrame. In doing so, you'll make use of the list(), zip(), dict() and pd.DataFrame() functions. Pandas has already been imported as pd.

Note: The zip() function in Python 3 and above returns a special zip object, which is essentially a generator. To convert this zip object into a list, you'll need to use list(). You can learn more about the zip() function as well as generators in Python Data Science Toolbox (Part 2).

### Instructions
* Zip the 2 lists list_keys and list_values together into one list of (key, value) tuples. Be sure to convert the zip object into a list, and store the result in zipped.
* Inspect the contents of zipped using print(). This has been done for you.
* Construct a dictionary using zipped. Store the result as data.
* Construct a DataFrame using the dictionary. Store the result as df.

#### Script
```
# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)
```
##### Output:
```
Zip the 2 lists list_keys and list_values together into one list of (key, value) tuples. Be sure to convert the zip object into a list, and store the result in zipped.
Inspect the contents of zipped using print(). This has been done for you.
Construct a dictionary using zipped. Store the result as data.
Construct a DataFrame using the dictionary. Store the result as df.
```
##### Comment:
Fantastic! Being able to build DataFrames from scratch is an important skill.

## 05. Labeling your data
You can use the DataFrame attribute df.columns to view and assign new string labels to columns in a pandas DataFrame.

In this exercise, we have imported pandas as pd and defined a DataFrame df containing top Billboard hits from the 1980s (from Wikipedia). Each row has the year, artist, song name and the number of weeks at the top. However, this DataFrame has the column labels a, b, c, d. Your job is to use the df.columns attribute to re-assign descriptive column labels.

### Instructions
* Create a list of new column labels with 'year', 'artist', 'song', 'chart weeks', and assign it to list_labels.
* Assign your list of labels to df.columns.

#### Script
```
# Build a list of labels: list_labels
list_labels = list(['year', 'artist', 'song', 'chart weeks'])

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels
```
##### Comment:
Great work! You'll often need to rename column names like this to be more informative.
