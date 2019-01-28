# Chapter 04: Putting It All Together: A Case Study

## 01. Introducing the project dataset
For the final chapter, you'll be looking at some of the Gapminder datasets combined into one tidy file called "gapminder_tidy.csv". This data set is available as a pandas DataFrame under the variable name data.

It is always a good idea to begin with some Exploratory Data Analysis. Pandas has a number of built-in methods that help with this. For example, data.head() displays the first five rows/entries of data, while data.tail() displays the last five rows/entries. data.shape gives you information about how many rows and columns there are in the data set. Another particularly useful method is data.info(), which provides a concise summary of data, including information about the number of entries, columns, data type of each column, and number of non-null entries in each column.

Use the IPython Shell and the pandas methods mentioned above to explore this data set. How many entries and columns does this data set have?

### Possible Answers
* 7 entries, 10111 columns.
* 10111 entries, 7 columns.
* 9000 entries, 7 columns.

#### Script:
```
In [1]: data.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 10111 entries, 1964 to 2006
Data columns (total 7 columns):
Country            10111 non-null object
fertility          10100 non-null float64
life               10111 non-null float64
population         10108 non-null float64
child_mortality    9210 non-null float64
gdp                9000 non-null float64
region             10111 non-null object
dtypes: float64(5), object(2)
memory usage: 631.9+ KB

In [2]: 
```
#### Answer:
2

#### Comment:
Correct! There are 10111 entries, or rows, and 7 columns in the data set. Both the data.info() and data.shape methods provide this information.
