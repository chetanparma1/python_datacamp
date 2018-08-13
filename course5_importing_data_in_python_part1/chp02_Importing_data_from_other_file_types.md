# Chapter 2: Importing data from other file types

## Not so flat any more
In Chapter 1, you learned how to use the IPython magic command ! ls to explore your current working directory. You can also do this natively in Python using the library os, which consists of miscellaneous operating system interfaces.

The first line of the following code imports the library os, the second line stores the name of the current directory in a string called wd and the third outputs the contents of the directory in a list to the shell.
```
import os
wd = os.getcwd()
os.listdir(wd)
```
Run this code in the IPython shell and answer the following questions. Ignore the files that begin with ..

Check out the contents of your current directory and answer the following questions: (1) which file is in your directory strucand NOT an example of a flat file; (2) why is it not a flat file?

### Instructions:
Possible Answers <br />
* database.db is not a flat file because relational databases contain structured relationships and flat files do not. <br />
press 1
*battledeath.xlsx is not a flat because it is a spreadsheet consisting of many sheets, not a single table. <br />
press 2
* titanic.txt is not a flat file because it is a .txt, not a .csv. <br />
press 3

```
In [1]: import os

In [2]: wd = os.getcwd()

In [3]: os.listdir(wd)
Out[3]: ['titanic.txt', 'battledeath.xlsx']
```
#### Comments:
Correct!

## Loading a pickled file
There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries. If you want your files to be human readable, you may want to save them as text files in a clever manner. JSONs, which you will see in a later chapter, are appropriate for Python dictionaries.

However, if you merely want to be able to import them into Python, you can serialize them. All this means is converting the object into a sequence of bytes, or a bytestream.

In this exercise, you'll import the pickle package, open a previously pickled data structure from a file and load it.

### Instructions:
* Import the pickle package.
* Complete the second argument of open() so that it is read only for a binary file. This argument will be a string of two letters, one signifying 'read only', the other 'binary'.
* Pass the correct argument to pickle.load(); it should use the variable that is bound to open.
* Print the data, d.
* Print the datatype of d; take your mind back to your previous use of the function type().

```{python}
# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

```
#### Output:
```
<script.py> output:
    {'Airline': '8', 'June': '69.4', 'Aug': '85', 'Mar': '84.4'}
    <class 'dict'>
```

##### Comments:
Awesome!

## Listing sheets in Excel files
Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in time. You won't always want to do so in Excel, however!

Here, you'll learn how to use pandas to import Excel spreadsheets and how to list the names of the sheets in any loaded .xlsx file.

Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of the sheet names using the attribute spreadsheet.sheet_names.

Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various countries over several years.

### Instructions
* Assign the filename to the variable file.
* Pass the correct argument to pd.ExcelFile() to load the file using pandas.
* Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.

```{python}
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
```
#### Output:
```
<script.py> output:
    ['2002', '2004']
```

##### Comments:
Good job!
