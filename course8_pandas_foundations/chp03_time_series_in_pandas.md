# Chapter 03: Time Series in Pandas

## 01. Reading and slicing times
For this exercise, we have read in the same data file using three different approaches:

* ```df1 = pd.read_csv(filename)```

* ```df2 = pd.read_csv(filename, parse_dates=['Date'])```

* ```df3 = pd.read_csv(filename, index_col='Date', parse_dates=True)```

Use the .head() and .info() methods in the IPython Shell to inspect the DataFrames. Then, try to index each DataFrame with a datetime string. Which of the resulting DataFrames allows you to easily index and slice data by dates using, for example, df1.loc['2010-Aug-01']?

### Possible Answers
* df1.   &emsp;&emsp;  press 1
* df1 and df2.  &emsp;&emsp;   press 2
* df2.   &emsp;&emsp;   press 3
* df2 and df3.   &emsp;&emsp;   press 4
* df3.   &emsp;&emsp;  press 5

#### Output:
```
In [1]: df1.head()
Out[1]: 
   Temperature       ...                  Date
0         46.2       ...        20100101 00:00
1         44.6       ...        20100101 01:00
2         44.1       ...        20100101 02:00
3         43.8       ...        20100101 03:00
4         43.5       ...        20100101 04:00

[5 rows x 4 columns]

In [2]: df1.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8759 entries, 0 to 8758
Data columns (total 4 columns):
Temperature    8759 non-null float64
DewPoint       8759 non-null float64
Pressure       8759 non-null float64
Date           8759 non-null object
dtypes: float64(3), object(1)
memory usage: 273.8+ KB

In [3]: df2.head()
Out[3]: 
   Temperature         ...                        Date
0         46.2         ...         2010-01-01 00:00:00
1         44.6         ...         2010-01-01 01:00:00
2         44.1         ...         2010-01-01 02:00:00
3         43.8         ...         2010-01-01 03:00:00
4         43.5         ...         2010-01-01 04:00:00

[5 rows x 4 columns]

In [4]: df2.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8759 entries, 0 to 8758
Data columns (total 4 columns):
Temperature    8759 non-null float64
DewPoint       8759 non-null float64
Pressure       8759 non-null float64
Date           8759 non-null datetime64[ns]
dtypes: datetime64[ns](1), float64(3)
memory usage: 273.8 KB

In [5]: df3.head()
Out[5]: 
                     Temperature    ...     Pressure
Date                                ...             
2010-01-01 00:00:00         46.2    ...          1.0
2010-01-01 01:00:00         44.6    ...          1.0
2010-01-01 02:00:00         44.1    ...          1.0
2010-01-01 03:00:00         43.8    ...          1.0
2010-01-01 04:00:00         43.5    ...          1.0

[5 rows x 3 columns]

In [6]: df3.info()
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 8759 entries, 2010-01-01 00:00:00 to 2010-12-31 23:00:00
Data columns (total 3 columns):
Temperature    8759 non-null float64
DewPoint       8759 non-null float64
Pressure       8759 non-null float64
dtypes: float64(3)
memory usage: 593.7 KB
```
##### Answer:
5

##### Comment:
Correct! This is why it is important to read in your data properly, especially when working with time series data.

## 02. Creating and using a DatetimeIndex
The pandas Index is a powerful way to handle time series data, so it is valuable to know how to build one yourself. Pandas provides the pd.to_datetime() function for just this task. For example, if passed the list of strings ['2015-01-01 091234','2015-01-01 091234'] and a format specification variable, such as format='%Y-%m-%d %H%M%S, pandas will parse the string into the proper datetime elements and build the datetime objects.

In this exercise, a list of temperature data and a list of date strings has been pre-loaded for you as temperature_list and date_list respectively. Your job is to use the .to_datetime() method to build a DatetimeIndex out of the list of date strings, and to then use it along with the list of temperature data to build a pandas Series.

### Instructions:
* Prepare a format string, time_format, using '%Y-%m-%d %H:%M' as the desired format.
* Convert date_list into a datetime object by using the pd.to_datetime() function. Specify the format string you defined above and assign the result to my_datetimes.
* Construct a pandas Series called time_series using pd.Series() with temperature_list and my_datetimes. Set the index of the Series to be my_datetimes.

#### Script:
```
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)  

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)
```
##### Comment:
Great work!

## 03. Partial string indexing and slicing
Pandas time series support "partial string" indexing. What this means is that even when passed only a portion of the datetime, such as the date but not the time, pandas is remarkably good at doing what one would expect. Pandas datetime indexing also supports a wide variety of commonly used datetime string formats, even when mixed.

In this exercise, a time series that contains hourly weather data has been pre-loaded for you. This data was read using the parse_dates=True option in read_csv() with index_col="Dates" so that the Index is indeed a DatetimeIndex.

All data from the 'Temperature' column has been extracted into the variable ts0. Your job is to use a variety of natural date strings to extract one or more values from ts0.

After you are done, you will have three new variables - ts1, ts2, and ts3. You can slice these further to extract only the first and last entries of each. Try doing this after your submission for more practice.

### Instructions
* Extract data from ts0 for a single hour - the hour from 9pm to 10pm on 2010-10-11. Assign it to ts1.
* Extract data from ts0 for a single day - July 4th, 2010 - and assign it to ts2.
* Extract data from ts0 for the second half of December 2010 - 12/15/2010 to 12/31/2010. Assign it to ts3.

#### Script
```
# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00':'2010-10-11 22:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['July 4th, 2010']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']
```

##### Comment:
Well done!

## 04. Reindexing the Index
Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.

In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you are done, it would be informative to inspect your results.

### Instructions:
* Create a new time series ts3 by reindexing ts2 with the index of ts1. To do this, call .reindex() on ts2 and pass in the index of ts1 (ts1.index).
* Create another new time series, ts4, by calling the same .reindex() as above, but also specifiying a fill method, using the keyword argument method="ffill" to forward-fill values.
* Add ts1 + ts2. Assign the result to sum12.
* Add ts1 + ts3. Assign the result to sum13.
* Add ts1 + ts4, Assign the result to sum14.

#### Script
```
# Reindex without fill method: ts3
ts3 = ts2.reindex(index=ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(index=ts1.index, method='ffill')

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4
```

##### Comment:
Wonderful work! Understanding how indexing and reindexing works is a valuable skill.

## 05. Resampling and frequency
Pandas provides methods for resampling time series data. When downsampling or upsampling, the syntax is similar, but the methods called are different. Both use the concept of 'method chaining' - df.method1().method2().method3() - to direct the output from one method call to the input of the next, and so on, as a sequence of operations, one feeding into the next.

For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean(). 'D' is an <a href="http://pandas.pydata.org/pandas-docs/version/0.9.1/timeseries.html#offset-aliases">offset alias</a> for Pandas timeseries. 

In this exercise, a data set containing hourly temperature data has been pre-loaded for you. Your job is to resample the data using a variety of aggregation methods to answer a few questions.

### Instructions:
* Downsample the 'Temperature' column of df to 6 hour data using .resample('6h') and .mean(). Assign the result to df1.
* Downsample the 'Temperature' column of df to daily data using .resample('D') and then count the number of data points in each day with .count(). Assign the result df2.

#### Script
```
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('d').count()
```
##### Comment
Excellent job! You'll get a lot more practice with resampling in the coming exercises!

## 06. Separating and resampling
With pandas, you can resample in different ways on different subsets of your data. For example, resampling different months of data with different aggregations. In this exercise, the data set containing hourly temperature data from the last exercise has been pre-loaded.

Your job is to resample the data using a variety of aggregation methods. The DataFrame is available in the workspace as df. You will be working with the 'Temperature' column.

### Instructions:
* Use partial string indexing to extract temperature data for August 2010 into august.
* Use the temperature data for August and downsample to find the daily maximum temperatures. Store the result in august_highs.
* Use partial string indexing to extract temperature data for February 2010 into february.
* Use the temperature data for February and downsample to find the daily minimum temperatures. Store the result in february_lows.

#### Script
```
# Extract temperature data for August: august
august = df['Temperature']['2010-08']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['Temperature']['2010-02']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()
```
##### Comment:
Great work!
