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
