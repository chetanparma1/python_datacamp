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
Well done! You'll learn how to deal with missing values later on in this course.
