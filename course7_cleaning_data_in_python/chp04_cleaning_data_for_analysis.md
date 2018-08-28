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

## 03. String parsing with regular expressions
In the video, Dan introduced you to the basics of regular expressions, which are powerful ways of defining patterns to match strings. This exercise will get you started with writing them.

When working with data, it is sometimes necessary to write a regular expression to look for properly entered values. Phone numbers in a dataset is a common field that needs to be checked for validity. Your job in this exercise is to define a regular expression to match US phone numbers that fit the pattern of `xxx-xxx-xxxx`.

The regular <a href="https://docs.python.org/3/library/re.html">expression module </a> in python is re. When performing pattern matching on data, since the pattern will be used for a match across multiple rows, it's better to compile the pattern first using `re.compile()`, and then use the compiled pattern to match values.

### Instructions:
* Import re.
* Compile a pattern that matches a phone number of the format xxx-xxx-xxxx.
* Use `\d{x}` to match x digits. Here you'll need to use it three times: twice to match 3 digits, and once to match 4 digits.
* Place the regular expression inside re.compile().
* Using the .match() method on prog, check whether the pattern matches the string '123-456-7890'.
* Using the same approach, now check whether the pattern matches the string '1123-456-7890'.

#### Script
```
# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))
```
##### Output:
```
<script.py> output:
    True
    False
```
##### Comment:
Fantastic! Regular expressions can seem challenging at first, but with practice, you'll get better and better at writing them! Here, as expected, the pattern matches the first string, but not the second.

## 04. Extracting numerical values from strings
Extracting numbers from strings is a common task, particularly when working with unstructured data or log files.

Say you have the following string: 'the recipe calls for 6 strawberries and 2 bananas'.

It would be useful to extract the 6 and the 2 from this string to be saved for later use when comparing strawberry to banana ratios.

When using a regular expression to extract multiple numbers (or multiple pattern matches, to be exact), you can use the re.findall() function. Dan did not discuss this in the video, but it is straightforward to use: You pass in a pattern and a string to re.findall(), and it will return a list of the matches.

### Instructions
* Import re.
* Write a pattern that will find all the numbers in the following string: 'the recipe calls for 10 strawberries and 1 banana'. To do this:
* Use the re.findall() function and pass it two arguments: the pattern, followed by the string.
\d is the pattern required to find digits. This should be followed with a + so that the previous element is matched one or more times. This ensures that 10 is viewed as one number and not as 1 and 0.
* Print the matches to confirm that your regular expression found the values 10 and 1.

#### Script
```
# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)
```
##### Output:
```
<script.py> output:
    ['10', '1']
```
##### Comment:
Excellent work - your regular expression successfully extracted the numeric values 10 and 1 from the string!!
