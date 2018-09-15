# Chapter 02: Advanced Indexing

## 01. Index values and names
Which one of the following index operations does not raise an error?

The sales DataFrame which you have seen in the videos of the previous chapter has been pre-loaded for you and is available for exploration in the IPython Shell.

```
     eggs  salt  spam
month                  
Jan      47  12.0    17
Feb     110  50.0    31
Mar     221  89.0    72
Apr      77  87.0    20
May     132   NaN    52
Jun     205  60.0    55
```

### Possible Answers
* sales.index[0] = 'JAN'.
press 1
* sales.index[0] = sales.index[0].upper().
press 2
* sales.index = range(len(sales)).
press 3

#### Script & Output:
```
In [1]: sales
Out[1]: 
       eggs  salt  spam
month                  
Jan      47  12.0    17
Feb     110  50.0    31
Mar     221  89.0    72
Apr      77  87.0    20
May     132   NaN    52
Jun     205  60.0    55

In [2]: sales.index[0]='JAN'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sales.index[0]='JAN'
  File "<stdin>", line 2050, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations

In [3]: sales.index[0] = sales.index[0].upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sales.index[0] = sales.index[0].upper()
  File "<stdin>", line 2050, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations

In [4]: sales.index = range(len(sales))
```
##### Answer: 
3

##### Comment:
Well done!

## 02. Changing index of a DataFrame
As you saw in the previous exercise, indexes are immutable objects. This means that if you want to change or modify the index in a DataFrame, then you need to change the whole index. You will do this now, using a list comprehension to create the new index.

A list comprehension is a succinct way to generate a list in one line. For example, the following list comprehension generates a list that contains the cubes of all numbers from 0 to 9: `cubes = [i**3 for i in range(10)]`. This is equivalent to the following code:
```
cubes = []
for i in range(10):
    cubes.append(i**3)
```
Before getting started, print the sales DataFrame in the IPython Shell and verify that the index is given by month abbreviations containing lowercase characters.

### Instructions:
* Create a list new_idx with the same elements as in sales.index, but with all characters capitalized.
* Assign new_idx to sales.index.
* Print the sales dataframe. This has been done for you, so hit 'Submit Answer' and to see how the index changed.

#### Script
```
# Create the list of new indexes: new_idx
new_idx = [idx.upper() for idx in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)
```
##### Output:
```
<script.py> output:
         eggs  salt  spam
    JAN    47  12.0    17
    FEB   110  50.0    31
    MAR   221  89.0    72
    APR    77  87.0    20
    MAY   132   NaN    52
    JUN   205  60.0    55
```
##### Comment:
Well done! Notice the DataFrame's new index!

## 03. Changing index name labels
Notice that in the previous exercise, the index was not labeled with a name. In this exercise, you will set its name to 'MONTHS'.

Similarly, if all the columns are related in some way, you can provide a label for the set of columns.

To get started, print the sales DataFrame in the IPython Shell and verify that the index has no name, only its data (the month names).

### Instructions:
* Assign the string 'MONTHS' to sales.index.name to create a name for the index.
* Print the sales dataframe to see the index name you just created.
* Now assign the string 'PRODUCTS' to sales.columns.name to give a name to the set of columns.
* Print the sales dataframe again to see the columns name you just created.

#### Script:
```
# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)
```
##### Output:
```
<script.py> output:
            eggs  salt  spam
    MONTHS                  
    JAN       47  12.0    17
    FEB      110  50.0    31
    MAR      221  89.0    72
    APR       77  87.0    20
    MAY      132   NaN    52
    JUN      205  60.0    55
    PRODUCTS  eggs  salt  spam
    MONTHS                    
    JAN         47  12.0    17
    FEB        110  50.0    31
    MAR        221  89.0    72
    APR         77  87.0    20
    MAY        132   NaN    52
    JUN        205  60.0    55
```
##### Comment:
Wonderful work! Notice how in the first DataFrame, the index has a label, and in the second DataFrame, both the index as well as the columns have labels.

## 04. Building an index, then a DataFrame
You can also build the DataFrame and index independently, and then put them together. If you take this route, be careful, as any mistakes in generating the DataFrame or the index can cause the data and the index to be aligned incorrectly.

In this exercise, the sales DataFrame has been provided for you without the month index. Your job is to build this index separately and then assign it to the sales DataFrame. Before getting started, print the sales DataFrame in the IPython Shell and note that it's missing the month information.

### Instructions:
* Generate a list months with the data `['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']`. This has been done for you.
* Assign months to sales.index.
* Print the modified sales dataframe and verify that you now have month information in the index.

#### Script
```
# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)
```
##### Output:
```
<script.py> output:
         eggs  salt  spam
    Jan    47  12.0    17
    Feb   110  50.0    31
    Mar   221  89.0    72
    Apr    77  87.0    20
    May   132   NaN    52
    Jun   205  60.0    55
```

##### Comment:
Excellent work! You're getting the hang of working with indexes. You'll now move onto learning about hierarchical indexes!
