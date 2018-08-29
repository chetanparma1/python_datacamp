# Chapter 05: Case Study

## 01. Exploratory analysis
Whenever you obtain a new dataset, your first task should always be to do some exploratory analysis to get a better understanding of the data and diagnose it for any potential issues.

The Gapminder data for the 19th century has been loaded into a DataFrame called g1800s. In the IPython Shell, use pandas methods such as .head(), .info(), and .describe(), and DataFrame attributes like .columns and .shape to explore it.

Use the information that you acquire from your exploratory analysis to choose the true statement from the options provided below. 

### Instructions
* The DataFrame has 259 rows and 100 columns.  &emsp;&emsp;  press 1
* The DataFrame has no missing values encoded as NaN.  &emsp;&emsp;  press 2
* 100 of the columns are of type float64 and 1 column is of type object.  &emsp;&emsp;  press 3
* The DataFrame takes up 203.2+ KB of memory.  &emsp;&emsp;  press 4

#### Script & Output
```
In [1]: g1800s.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 260 entries, 0 to 259
Columns: 101 entries, Life expectancy to 1899
dtypes: float64(100), object(1)
memory usage: 205.2+ KB

In [6]: g1800s.head()
Out[6]: 
         Life expectancy   1800   1801   1802   1803   1804   1805   1806  \
0               Abkhazia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
1            Afghanistan  28.21  28.20  28.19  28.18  28.17  28.16  28.15   
2  Akrotiri and Dhekelia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
3                Albania  35.40  35.40  35.40  35.40  35.40  35.40  35.40   
4                Algeria  28.82  28.82  28.82  28.82  28.82  28.82  28.82   

    1807   1808  ...     1890   1891   1892   1893   1894   1895   1896  \
0    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN    NaN   
1  28.14  28.13  ...    27.29  27.28  27.27  27.26  27.25  27.24  27.23   
2    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN    NaN   
3  35.40  35.40  ...    35.40  35.40  35.40  35.40  35.40  35.40  35.40   
4  28.82  28.82  ...    28.82  28.82  28.82  28.82  28.82  28.82  28.82   

    1897   1898   1899  
0    NaN    NaN    NaN  
1  27.22  27.21  27.20  
2    NaN    NaN    NaN  
3  35.40  35.40  35.40  
4  28.82  28.82  28.82  

[5 rows x 101 columns]
```

##### Answer:
3

##### Comment:
Exactly! This information is provided by the g1800s.info(). 'Life expectancy' is the only column in the DataFrame that is not of type float64.
