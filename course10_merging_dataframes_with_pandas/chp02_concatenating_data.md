# Chapter 02: Concatenating Data

## 01. Appending Series with nonunique Indices
The Series bronze and silver, which have been printed in the IPython Shell, represent the 5 countries that won the most bronze and silver Olympic medals respectively between 1896 & 2008. The Indexes of both Series are called Country and the values are the corresponding number of medals won.

If you were to run the command combined = bronze.append(silver), how many rows would combined have? And how many rows would combined.loc['United States'] return? Find out for yourself by running these commands in the IPython Shell.

### Possible Answers
* combined has 5 rows and combined.loc['United States'] is empty (0 rows).
press 1
* combined has 10 rows and combined.loc['United States'] has 2 rows.
press 2
* combined has 6 rows and combined.loc['United States'] has 1 row.
press 3
* combined has 5 rows and combined.loc['United States'] has 2 rows.
press 4

#### Script:
```
bronze
Country
United States     1052.0
Soviet Union       584.0
United Kingdom     505.0
France             475.0
Germany            454.0
Name: Total, dtype: float64

silver
Country
United States     1195.0
Soviet Union       627.0
United Kingdom     591.0
France             461.0
Italy              394.0
Name: Total, dtype: float64

In [1]: combined = bronze.append(silver)

In [2]: combined.loc['United States']
Out[2]: 
Country
United States    1052.0
United States    1195.0
Name: Total, dtype: float64
```

#### Answer:
2

#### Comment:
Correct! The combined Series has 10 rows and combined.loc['United States'] has two rows, since the index value 'United States' occurs in both series bronze and silver.

## 02. Appending pandas Series
In this exercise, you'll load sales data from the months January, February, and March into DataFrames. Then, you'll extract Series with the 'Units' column from each and append them together with method chaining using .append().

To check that the stacking worked, you'll print slices from these Series, and finally, you'll add the result to figure out the total units sold in the first quarter.

### Instructions:
* Read the files 'sales-jan-2015.csv', 'sales-feb-2015.csv' and 'sales-mar-2015.csv' into the DataFrames jan, feb, and mar respectively.
* Use parse_dates=True and index_col='Date'.
* Extract the 'Units' column of jan, feb, and mar to create the Series jan_units, feb_units, and mar_units respectively.
* Construct the Series quarter1 by appending feb_units to jan_units and then appending mar_units to the result. Use chained calls to the .append() method to do this.
* Verify that quarter1 has the individual Series stacked vertically. To do this:
* Print the slice containing rows from jan 27, 2015 to feb 2, 2015.
* Print the slice containing rows from feb 26, 2015 to mar 7, 2015.
* Compute and print the total number of units sold from the Series quarter1. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv', index_col='Date', parse_dates=True)

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv', index_col='Date', parse_dates=True)

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv', index_col='Date', parse_dates=True)

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015':'march 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())
```
#### Output:
```
<script.py> output:
    Date
    2015-01-27 07:11:55    18
    2015-02-02 08:33:01     3
    2015-02-02 20:54:49     9
    Name: Units, dtype: int64
    Date
    2015-02-26 08:57:45     4
    2015-02-26 08:58:51     1
    2015-03-06 10:11:45    17
    2015-03-06 02:03:56    17
    Name: Units, dtype: int64
    642
```
#### Comment:
Well done! As you can see, appending pandas Series is very straightforward!

## 03. Concatenating pandas Series along row axis
Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.

Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().

You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.

### Instructions:
* Create an empty list called units. This has been done for you.
* Use a for loop to iterate over [jan, feb, mar]:
* In each iteration of the loop, append the 'Units' column of each DataFrame to units.
* Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
* Specify the keyword argument axis='rows' to stack the Series vertically.
* Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Initialize empty list: units
units = []

# Build the list of Series
# this will create a list of lists
for month in [jan, feb, mar]:
    units.append(month['Units'])

# Concatenate the list: quarter1
quarter1 = pd.concat(units, axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
```
#### Output:
```
In [4]: units
Out[4]: 
[Date
 2015-01-21 19:13:21    11
 2015-01-09 05:23:51     8
 2015-01-06 17:19:34    17
 2015-01-02 09:51:06    16
 2015-01-11 14:51:02    11
 2015-01-01 07:31:20    18
 2015-01-24 08:01:16     1
 2015-01-25 15:40:07     6
 2015-01-13 05:36:12     7
 2015-01-03 18:00:19    19
 2015-01-16 00:33:47    17
 2015-01-16 07:21:12    13
 2015-01-20 19:49:24    12
 2015-01-26 01:50:25    14
 2015-01-15 02:38:25    16
 2015-01-06 13:47:37    16
 2015-01-15 15:33:40     7
 2015-01-27 07:11:55    18
 2015-01-20 11:28:02    13
 2015-01-16 19:20:46     8
 Name: Units, dtype: int64, Date
 2015-02-26 08:57:45     4
 2015-02-16 12:09:19    10
 2015-02-03 14:14:18    13
 2015-02-02 08:33:01     3
 2015-02-25 00:29:00    10
 2015-02-05 01:53:06    19
 2015-02-09 08:57:30    19
 2015-02-11 20:03:08     7
 2015-02-04 21:52:45    14
 2015-02-09 13:09:55     7
 2015-02-07 22:58:10     1
 2015-02-11 22:50:44     4
 2015-02-26 08:58:51     1
 2015-02-05 22:05:03    10
 2015-02-04 15:36:29    13
 2015-02-19 16:02:58    10
 2015-02-19 10:59:33    16
 2015-02-02 20:54:49     9
 2015-02-21 05:01:26     3
 2015-02-21 20:41:47     3
 Name: Units, dtype: int64, Date
 2015-03-22 14:42:25     6
 2015-03-12 18:33:06    19
 2015-03-22 03:58:28     8
 2015-03-15 00:53:12    19
 2015-03-17 19:25:37    10
 2015-03-16 05:54:06     3
 2015-03-25 10:18:10     9
 2015-03-25 16:42:42    12
 2015-03-26 05:20:04     3
 2015-03-06 10:11:45    17
 2015-03-22 21:14:39    11
 2015-03-17 19:38:12     8
 2015-03-28 19:20:38     5
 2015-03-13 04:41:32     8
 2015-03-06 02:03:56    17
 2015-03-13 11:40:16    11
 2015-03-27 08:29:45     6
 2015-03-21 06:42:41    19
 2015-03-15 08:50:45    18
 2015-03-13 16:25:24     9
 Name: Units, dtype: int64]
 
 
 In [8]: quarter1
Out[8]: 
Date
2015-01-21 19:13:21    11
2015-01-09 05:23:51     8
2015-01-06 17:19:34    17
2015-01-02 09:51:06    16
2015-01-11 14:51:02    11
2015-01-01 07:31:20    18
2015-01-24 08:01:16     1
2015-01-25 15:40:07     6
2015-01-13 05:36:12     7
2015-01-03 18:00:19    19
2015-01-16 00:33:47    17
2015-01-16 07:21:12    13
2015-01-20 19:49:24    12
2015-01-26 01:50:25    14
2015-01-15 02:38:25    16
2015-01-06 13:47:37    16
2015-01-15 15:33:40     7
2015-01-27 07:11:55    18
2015-01-20 11:28:02    13
2015-01-16 19:20:46     8
2015-02-26 08:57:45     4
2015-02-16 12:09:19    10
2015-02-03 14:14:18    13
2015-02-02 08:33:01     3
2015-02-25 00:29:00    10
2015-02-05 01:53:06    19
2015-02-09 08:57:30    19
2015-02-11 20:03:08     7
2015-02-04 21:52:45    14
2015-02-09 13:09:55     7
2015-02-07 22:58:10     1
2015-02-11 22:50:44     4
2015-02-26 08:58:51     1
2015-02-05 22:05:03    10
2015-02-04 15:36:29    13
2015-02-19 16:02:58    10
2015-02-19 10:59:33    16
2015-02-02 20:54:49     9
2015-02-21 05:01:26     3
2015-02-21 20:41:47     3
2015-03-22 14:42:25     6
2015-03-12 18:33:06    19
2015-03-22 03:58:28     8
2015-03-15 00:53:12    19
2015-03-17 19:25:37    10
2015-03-16 05:54:06     3
2015-03-25 10:18:10     9
2015-03-25 16:42:42    12
2015-03-26 05:20:04     3
2015-03-06 10:11:45    17
2015-03-22 21:14:39    11
2015-03-17 19:38:12     8
2015-03-28 19:20:38     5
2015-03-13 04:41:32     8
2015-03-06 02:03:56    17
2015-03-13 11:40:16    11
2015-03-27 08:29:45     6
2015-03-21 06:42:41    19
2015-03-15 08:50:45    18
2015-03-13 16:25:24     9
Name: Units, dtype: int64


<script.py> output:
    Date
    2015-01-27 07:11:55    18
    2015-02-02 08:33:01     3
    2015-02-02 20:54:49     9
    Name: Units, dtype: int64
    Date
    2015-02-26 08:57:45     4
    2015-02-26 08:58:51     1
    2015-03-06 10:11:45    17
    2015-03-06 02:03:56    17
    Name: Units, dtype: int64
    
```
#### Comment:
Great work! As in this exercise, you can achieve the same results as appending by concatenating along the row axis.

## 04. Appending DataFrames with ignore_index
In this exercise, you'll use the <a href="https://www.data.gov/developers/baby-names-dataset/">Baby Names Dataset</a> (from <a href="http://data.gov/">data.gov</a>) again. This time, both DataFrames names_1981 and names_1881 are loaded without specifying an Index column (so the default Indexes for both are RangeIndexes).

You'll use the DataFrame .append() method to make a DataFrame combined_names. To distinguish rows from the original two DataFrames, you'll add a 'year' column to each with the year (1881 or 1981 in this case). In addition, you'll specify ignore_index=True so that the index values are not used along the concatenation axis. The resulting axis will instead be labeled `0, 1, ..., n-1`, which is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information.

### Instructions:
* Create a 'year' column in the DataFrames names_1881 and names_1981, with values of 1881 and 1981 respectively. Recall that assigning a scalar value to a DataFrame column broadcasts that value throughout.
* Create a new DataFrame called combined_names by appending the rows of names_1981 underneath the rows of names_1881. Specify the keyword argument ignore_index=True to make a new RangeIndex of unique integers for each row.
* Print the shapes of all three DataFrames. This has been done for you.
* Extract all rows from combined_names that have the name 'Morgan'. To do this, use the .loc[] accessor with an appropriate filter. The relevant column of combined_names here is 'name'.

#### Script
```
# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
# print(combined_names[combined_names['name'] == 'Morgan'])
print(combined_names.loc[combined_names['name'] == 'Morgan'])
```
#### Output:
```
<script.py> output:
    (19455, 4)
    (1935, 4)
    (21390, 4)
             name gender  count  year
    1283   Morgan      M     23  1881
    2096   Morgan      F   1769  1981
    14390  Morgan      M    766  1981
```
#### Comment:
Great work!

## 05. Concatenating pandas DataFrames along column axis
The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.

In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more detail in later exercises).

The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and weather_mean respectively, and pandas has been imported as pd.

### Instructions:
* Create a new DataFrame called weather by concatenating the DataFrames weather_max and weather_mean horizontally.
* Pass the DataFrames to pd.concat() as a list and specify the keyword argument axis=1 to stack them horizontally.
* Print the new DataFrame weather.

#### Script:
```
# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concatenate([weather_max, weather_mean])

# Print weather
print(weather)
```

#### Output:
```
In [1]: weather_max
Out[1]: 
       Max TemperatureF
Month                  
Jan                  68
Apr                  89
Jul                  91
Oct                  84

In [2]: weather_mean
Out[2]: 
       Mean TemperatureF
Month                   
Apr            53.100000
Aug            70.000000
Dec            34.935484
Feb            28.714286
Jan            32.354839
Jul            72.870968
Jun            70.133333
Mar            35.000000
May            62.612903
Nov            39.800000
Oct            55.451613
Sep            63.766667

<script.py> output:
         Max TemperatureF  Mean TemperatureF
    Apr              89.0          53.100000
    Aug               NaN          70.000000
    Dec               NaN          34.935484
    Feb               NaN          28.714286
    Jan              68.0          32.354839
    Jul              91.0          72.870968
    Jun               NaN          70.133333
    Mar               NaN          35.000000
    May               NaN          62.612903
    Nov               NaN          39.800000
    Oct              84.0          55.451613
    Sep               NaN          63.766667
```
#### Comment:
Well done! This is where you start to see the advantages of concatenating over appending.

## 06. Reading multiple files to build a DataFrame
It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.

Here, you'll work with DataFrames compiled from <a href="https://www.theguardian.com/sport/datablog/2012/jun/25/olympic-medal-winner-list-data">The Guardian's Olympic medal dataset</a>.

pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.

### Instructions:
* Iterate over medal_types in the for loop.
* Inside the for loop:
** Create file_name using string interpolation with the loop variable medal. This has been done for you. The expression "%s_top5.csv" % medal evaluates as a string with the value of medal replacing %s in the format string.
** Create the list of column names called columns. This has been done for you.
** Read file_name into a DataFrame called medal_df. Specify the keyword arguments header=0, index_col='Country', and names=columns to get the correct row and column Indexes.
** Append medal_df to medals using the list .append() method.
* Concatenate the list of DataFrames medals horizontally (using axis='columns') to create a single DataFrame called medals. Print it in its entirety.

#### Script:
```
for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name, header = 0, index_col='Country', names=columns)

    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals, axis = 'columns')

# Print medals
print(medals)
```

#### Output:
```
In [1]: medal_types
Out[1]: ['bronze', 'silver', 'gold']

<script.py> output:
                    bronze  silver    gold
    France           475.0   461.0     NaN
    Germany          454.0     NaN   407.0
    Italy              NaN   394.0   460.0
    Soviet Union     584.0   627.0   838.0
    United Kingdom   505.0   591.0   498.0
    United States   1052.0  1195.0  2088.0
```
#### Comment:
Fantastic! Being able to build DataFrames from multiple files like this can be incredibly useful.

## 07. Concatenating vertically to get MultiIndexed rows
When stacking a sequence of DataFrames vertically, it is sometimes desirable to construct a MultiIndex to indicate the DataFrame from which each row originated. This can be done by specifying the keys parameter in the call to pd.concat(), which generates a hierarchical index with the labels from keys as the outermost index label. So you don't have to rename the columns of each DataFrame as you load it. Instead, only the Index column needs to be specified.

Here, you'll continue working with DataFrames compiled from <a href="https://www.theguardian.com/sport/datablog/2012/jun/25/olympic-medal-winner-list-data">The Guardian's Olympic medal dataset</a>. Once again, pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.

### Instructions
* Within the for loop:
** Read file_name into a DataFrame called medal_df. Specify the index to be 'Country'.
** Append medal_df to medals.
* Concatenate the list of DataFrames medals into a single DataFrame called medals. Be sure to use the keyword argument keys=['bronze', 'silver', 'gold'] to create a vertically stacked DataFrame with a MultiIndex.
* Print the new DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name, index_col = 'Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals, keys = ['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)
```

#### Output:
```
<script.py> output:
                            Total
           Country               
    bronze United States   1052.0
           Soviet Union     584.0
           United Kingdom   505.0
           France           475.0
           Germany          454.0
    silver United States   1195.0
           Soviet Union     627.0
           United Kingdom   591.0
           France           461.0
           Italy            394.0
    gold   United States   2088.0
           Soviet Union     838.0
           United Kingdom   498.0
           Italy            460.0
           Germany          407.0
```
#### Comment:
Well done! Notice the MultiIndex of medals.

## 08. Slicing MultiIndexed DataFrames
This exercise picks up where the last ended (again using <a hre="https://www.theguardian.com/sport/datablog/2012/jun/25/olympic-medal-winner-list-data">The Guardian's Olympic medal dataset</a>).

You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out <a href="https://campus.datacamp.com/courses/manipulating-dataframes-with-pandas/advanced-indexing?ex=10">this exercise</a> from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.

pandas has been imported for you as pd and the DataFrame medals is already in your namespace.

### Instructions:
* Create a new DataFrame medals_sorted with the entries of medals sorted. Use .sort_index(level=0) to ensure the Index is sorted suitably.
* Print the number of bronze medals won by Germany and all of the silver medal data. This has been done for you.
* Create an alias for pd.IndexSlice called idx. A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex.
* Slice all the data on medals won by the United Kingdom. To do this, use the .loc[] accessor with idx[:,'United Kingdom'], :.

#### Script
```
# Sort the entries of medals: medals_sorted
# index levels are numbered from the inner to the outermost level. 
medals_sorted = medals.sort_index(level = 0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[(idx[:, 'United Kingdom']), :])
```
#### Output:
```
<script.py> output:
    Total    454.0
    Name: (bronze, Germany), dtype: float64
                     Total
    Country               
    France           461.0
    Italy            394.0
    Soviet Union     627.0
    United Kingdom   591.0
    United States   1195.0
                           Total
           Country              
    bronze United Kingdom  505.0
    silver United Kingdom  591.0
    gold   United Kingdom  498.0
```
#### Comment:
Great work! It looks like only the United States and the Soviet Union have won more Silver medals than the United Kingdom.

## 09. Concatenating horizontally to get MultiIndexed columns
It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.

Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.

### Instructions:
* Construct a new DataFrame february with MultiIndexed columns by concatenating the list dataframes.
* Use axis=1 to stack the DataFrames horizontally and the keyword argument keys=['Hardware', 'Software', 'Service'] to construct a hierarchical Index from each DataFrame.
* Print summary information from the new DataFrame february using the .info() method. This has been done for you.
* Create an alias called idx for pd.IndexSlice.
* Extract a slice called slice_2_8 from february (using .loc[] & idx) that comprises rows between Feb. 2, 2015 to Feb. 8, 2015 from columns under 'Company'.
* Print the slice_2_8. This has been done for you, so hit 'Submit Answer' to see the sliced data!

#### Script:
```
# Concatenate dataframes: february
february = pd.concat(dataframes, axis = 1, keys = ['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['2015-02-02':'2015-02-08', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)
```

#### Output:
```
In [15]: dataframes
Out[15]: 
[                             Company   Product  Units
 Date                                                 
 2015-02-04 21:52:45  Acme Coporation  Hardware     14
 2015-02-07 22:58:10  Acme Coporation  Hardware      1
 2015-02-19 10:59:33        Mediacore  Hardware     16
 2015-02-02 20:54:49        Mediacore  Hardware      9
 2015-02-21 20:41:47            Hooli  Hardware      3,
                              Company   Product  Units
 Date                                                 
 2015-02-16 12:09:19            Hooli  Software     10
 2015-02-03 14:14:18          Initech  Software     13
 2015-02-02 08:33:01            Hooli  Software      3
 2015-02-05 01:53:06  Acme Coporation  Software     19
 2015-02-11 20:03:08          Initech  Software      7
 2015-02-09 13:09:55        Mediacore  Software      7
 2015-02-11 22:50:44            Hooli  Software      4
 2015-02-04 15:36:29        Streeplex  Software     13
 2015-02-21 05:01:26        Mediacore  Software      3,
                        Company  Product  Units
 Date                                          
 2015-02-26 08:57:45  Streeplex  Service      4
 2015-02-25 00:29:00    Initech  Service     10
 2015-02-09 08:57:30  Streeplex  Service     19
 2015-02-26 08:58:51  Streeplex  Service      1
 2015-02-05 22:05:03      Hooli  Service     10
 2015-02-19 16:02:58  Mediacore  Service     10]
```
```
In [11]: february
Out[11]: 
                            Hardware                         Software  \
                             Company   Product Units          Company   
Date                                                                    
2015-02-02 08:33:01              NaN       NaN   NaN            Hooli   
2015-02-02 20:54:49        Mediacore  Hardware   9.0              NaN   
2015-02-03 14:14:18              NaN       NaN   NaN          Initech   
2015-02-04 15:36:29              NaN       NaN   NaN        Streeplex   
2015-02-04 21:52:45  Acme Coporation  Hardware  14.0              NaN   
2015-02-05 01:53:06              NaN       NaN   NaN  Acme Coporation   
2015-02-05 22:05:03              NaN       NaN   NaN              NaN   
2015-02-07 22:58:10  Acme Coporation  Hardware   1.0              NaN   
2015-02-09 08:57:30              NaN       NaN   NaN              NaN   
2015-02-09 13:09:55              NaN       NaN   NaN        Mediacore   
2015-02-11 20:03:08              NaN       NaN   NaN          Initech   
2015-02-11 22:50:44              NaN       NaN   NaN            Hooli   
2015-02-16 12:09:19              NaN       NaN   NaN            Hooli   
2015-02-19 10:59:33        Mediacore  Hardware  16.0              NaN   
2015-02-19 16:02:58              NaN       NaN   NaN              NaN   
2015-02-21 05:01:26              NaN       NaN   NaN        Mediacore   
2015-02-21 20:41:47            Hooli  Hardware   3.0              NaN   
2015-02-25 00:29:00              NaN       NaN   NaN              NaN   
2015-02-26 08:57:45              NaN       NaN   NaN              NaN   
2015-02-26 08:58:51              NaN       NaN   NaN              NaN   

                                       Service                 
                      Product Units    Company  Product Units  
Date                                                           
2015-02-02 08:33:01  Software   3.0        NaN      NaN   NaN  
2015-02-02 20:54:49       NaN   NaN        NaN      NaN   NaN  
2015-02-03 14:14:18  Software  13.0        NaN      NaN   NaN  
2015-02-04 15:36:29  Software  13.0        NaN      NaN   NaN  
2015-02-04 21:52:45       NaN   NaN        NaN      NaN   NaN  
2015-02-05 01:53:06  Software  19.0        NaN      NaN   NaN  
2015-02-05 22:05:03       NaN   NaN      Hooli  Service  10.0  
2015-02-07 22:58:10       NaN   NaN        NaN      NaN   NaN  
2015-02-09 08:57:30       NaN   NaN  Streeplex  Service  19.0  
2015-02-09 13:09:55  Software   7.0        NaN      NaN   NaN  
2015-02-11 20:03:08  Software   7.0        NaN      NaN   NaN  
2015-02-11 22:50:44  Software   4.0        NaN      NaN   NaN  
2015-02-16 12:09:19  Software  10.0        NaN      NaN   NaN  
2015-02-19 10:59:33       NaN   NaN        NaN      NaN   NaN  
2015-02-19 16:02:58       NaN   NaN  Mediacore  Service  10.0  
2015-02-21 05:01:26  Software   3.0        NaN      NaN   NaN  
2015-02-21 20:41:47       NaN   NaN        NaN      NaN   NaN  
2015-02-25 00:29:00       NaN   NaN    Initech  Service  10.0  
2015-02-26 08:57:45       NaN   NaN  Streeplex  Service   4.0  
2015-02-26 08:58:51       NaN   NaN  Streeplex  Service   1.0
```
```
<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 20 entries, 2015-02-02 08:33:01 to 2015-02-26 08:58:51
    Data columns (total 9 columns):
    (Hardware, Company)    5 non-null object
    (Hardware, Product)    5 non-null object
    (Hardware, Units)      5 non-null float64
    (Software, Company)    9 non-null object
    (Software, Product)    9 non-null object
    (Software, Units)      9 non-null float64
    (Service, Company)     6 non-null object
    (Service, Product)     6 non-null object
    (Service, Units)       6 non-null float64
    dtypes: float64(3), object(6)
    memory usage: 1.6+ KB
    None
                                Hardware         Software Service
                                 Company          Company Company
    Date                                                         
    2015-02-02 08:33:01              NaN            Hooli     NaN
    2015-02-02 20:54:49        Mediacore              NaN     NaN
    2015-02-03 14:14:18              NaN          Initech     NaN
    2015-02-04 15:36:29              NaN        Streeplex     NaN
    2015-02-04 21:52:45  Acme Coporation              NaN     NaN
    2015-02-05 01:53:06              NaN  Acme Coporation     NaN
    2015-02-05 22:05:03              NaN              NaN   Hooli
    2015-02-07 22:58:10  Acme Coporation              NaN     NaN
```

#### Comment:
Excellent work! Working with MultiIndexes and MultiIndexed columns can seem tricky at first, but with practice, it will become second nature.

## 10. Concatenating DataFrames from a dict
You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.

### Instructions:
* Create a list called month_list consisting of the tuples ('january', jan), ('february', feb), and ('march', mar).
* Create an empty dictionary called month_dict.
* Inside the for loop:
** Group month_data by 'Company' and use .sum() to aggregate.
* Construct a new DataFrame called sales by concatenating the DataFrames stored in month_dict.
* Create an alias for pd.IndexSlice and print all sales by 'Mediacore'. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Make the list of tuples: month_list
month_list = [('january', jan), ('february', feb), ('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])

```
#### Output:
```
In [1]: jan
Out[1]: 
                   Date          Company   Product  Units
0   2015-01-21 19:13:21        Streeplex  Hardware     11
1   2015-01-09 05:23:51        Streeplex   Service      8
2   2015-01-06 17:19:34          Initech  Hardware     17
3   2015-01-02 09:51:06            Hooli  Hardware     16
4   2015-01-11 14:51:02            Hooli  Hardware     11
5   2015-01-01 07:31:20  Acme Coporation  Software     18
6   2015-01-24 08:01:16          Initech  Software      1
7   2015-01-25 15:40:07          Initech   Service      6
8   2015-01-13 05:36:12            Hooli   Service      7
9   2015-01-03 18:00:19            Hooli   Service     19
10  2015-01-16 00:33:47            Hooli  Hardware     17
11  2015-01-16 07:21:12          Initech   Service     13
12  2015-01-20 19:49:24  Acme Coporation  Hardware     12
13  2015-01-26 01:50:25  Acme Coporation  Software     14
14  2015-01-15 02:38:25  Acme Coporation   Service     16
15  2015-01-06 13:47:37  Acme Coporation  Software     16
16  2015-01-15 15:33:40        Mediacore  Hardware      7
17  2015-01-27 07:11:55        Streeplex   Service     18
18  2015-01-20 11:28:02        Streeplex  Software     13
19  2015-01-16 19:20:46        Mediacore   Service      8

In [2]: feb
Out[2]: 
                   Date          Company   Product  Units
0   2015-02-26 08:57:45        Streeplex   Service      4
1   2015-02-16 12:09:19            Hooli  Software     10
2   2015-02-03 14:14:18          Initech  Software     13
3   2015-02-02 08:33:01            Hooli  Software      3
4   2015-02-25 00:29:00          Initech   Service     10
5   2015-02-05 01:53:06  Acme Coporation  Software     19
6   2015-02-09 08:57:30        Streeplex   Service     19
7   2015-02-11 20:03:08          Initech  Software      7
8   2015-02-04 21:52:45  Acme Coporation  Hardware     14
9   2015-02-09 13:09:55        Mediacore  Software      7
10  2015-02-07 22:58:10  Acme Coporation  Hardware      1
11  2015-02-11 22:50:44            Hooli  Software      4
12  2015-02-26 08:58:51        Streeplex   Service      1
13  2015-02-05 22:05:03            Hooli   Service     10
14  2015-02-04 15:36:29        Streeplex  Software     13
15  2015-02-19 16:02:58        Mediacore   Service     10
16  2015-02-19 10:59:33        Mediacore  Hardware     16
17  2015-02-02 20:54:49        Mediacore  Hardware      9
18  2015-02-21 05:01:26        Mediacore  Software      3
19  2015-02-21 20:41:47            Hooli  Hardware      3

In [3]: mar
Out[3]: 
                   Date          Company   Product  Units
0   2015-03-22 14:42:25        Mediacore  Software      6
1   2015-03-12 18:33:06          Initech   Service     19
2   2015-03-22 03:58:28        Streeplex  Software      8
3   2015-03-15 00:53:12            Hooli  Hardware     19
4   2015-03-17 19:25:37            Hooli  Hardware     10
5   2015-03-16 05:54:06        Mediacore  Software      3
6   2015-03-25 10:18:10          Initech  Hardware      9
7   2015-03-25 16:42:42        Streeplex  Hardware     12
8   2015-03-26 05:20:04        Streeplex  Software      3
9   2015-03-06 10:11:45        Mediacore  Software     17
10  2015-03-22 21:14:39          Initech  Hardware     11
11  2015-03-17 19:38:12            Hooli  Hardware      8
12  2015-03-28 19:20:38  Acme Coporation   Service      5
13  2015-03-13 04:41:32        Streeplex  Hardware      8
14  2015-03-06 02:03:56        Mediacore  Software     17
15  2015-03-13 11:40:16          Initech  Software     11
16  2015-03-27 08:29:45        Mediacore  Software      6
17  2015-03-21 06:42:41        Mediacore  Hardware     19
18  2015-03-15 08:50:45          Initech  Hardware     18
19  2015-03-13 16:25:24        Streeplex  Software      9
```
```
In [17]: month_list
Out[17]: 
[('january',                    Date          Company   Product  Units
  0   2015-01-21 19:13:21        Streeplex  Hardware     11
  1   2015-01-09 05:23:51        Streeplex   Service      8
  2   2015-01-06 17:19:34          Initech  Hardware     17
  3   2015-01-02 09:51:06            Hooli  Hardware     16
  4   2015-01-11 14:51:02            Hooli  Hardware     11
  5   2015-01-01 07:31:20  Acme Coporation  Software     18
  6   2015-01-24 08:01:16          Initech  Software      1
  7   2015-01-25 15:40:07          Initech   Service      6
  8   2015-01-13 05:36:12            Hooli   Service      7
  9   2015-01-03 18:00:19            Hooli   Service     19
  10  2015-01-16 00:33:47            Hooli  Hardware     17
  11  2015-01-16 07:21:12          Initech   Service     13
  12  2015-01-20 19:49:24  Acme Coporation  Hardware     12
  13  2015-01-26 01:50:25  Acme Coporation  Software     14
  14  2015-01-15 02:38:25  Acme Coporation   Service     16
  15  2015-01-06 13:47:37  Acme Coporation  Software     16
  16  2015-01-15 15:33:40        Mediacore  Hardware      7
  17  2015-01-27 07:11:55        Streeplex   Service     18
  18  2015-01-20 11:28:02        Streeplex  Software     13
  19  2015-01-16 19:20:46        Mediacore   Service      8),
 ('february',                    Date          Company   Product  Units
  0   2015-02-26 08:57:45        Streeplex   Service      4
  1   2015-02-16 12:09:19            Hooli  Software     10
  2   2015-02-03 14:14:18          Initech  Software     13
  3   2015-02-02 08:33:01            Hooli  Software      3
  4   2015-02-25 00:29:00          Initech   Service     10
  5   2015-02-05 01:53:06  Acme Coporation  Software     19
  6   2015-02-09 08:57:30        Streeplex   Service     19
  7   2015-02-11 20:03:08          Initech  Software      7
  8   2015-02-04 21:52:45  Acme Coporation  Hardware     14
  9   2015-02-09 13:09:55        Mediacore  Software      7
  10  2015-02-07 22:58:10  Acme Coporation  Hardware      1
  11  2015-02-11 22:50:44            Hooli  Software      4
  12  2015-02-26 08:58:51        Streeplex   Service      1
  13  2015-02-05 22:05:03            Hooli   Service     10
  14  2015-02-04 15:36:29        Streeplex  Software     13
  15  2015-02-19 16:02:58        Mediacore   Service     10
  16  2015-02-19 10:59:33        Mediacore  Hardware     16
  17  2015-02-02 20:54:49        Mediacore  Hardware      9
  18  2015-02-21 05:01:26        Mediacore  Software      3
  19  2015-02-21 20:41:47            Hooli  Hardware      3),
 ('march',                    Date          Company   Product  Units
  0   2015-03-22 14:42:25        Mediacore  Software      6
  1   2015-03-12 18:33:06          Initech   Service     19
  2   2015-03-22 03:58:28        Streeplex  Software      8
  3   2015-03-15 00:53:12            Hooli  Hardware     19
  4   2015-03-17 19:25:37            Hooli  Hardware     10
  5   2015-03-16 05:54:06        Mediacore  Software      3
  6   2015-03-25 10:18:10          Initech  Hardware      9
  7   2015-03-25 16:42:42        Streeplex  Hardware     12
  8   2015-03-26 05:20:04        Streeplex  Software      3
  9   2015-03-06 10:11:45        Mediacore  Software     17
  10  2015-03-22 21:14:39          Initech  Hardware     11
  11  2015-03-17 19:38:12            Hooli  Hardware      8
  12  2015-03-28 19:20:38  Acme Coporation   Service      5
  13  2015-03-13 04:41:32        Streeplex  Hardware      8
  14  2015-03-06 02:03:56        Mediacore  Software     17
  15  2015-03-13 11:40:16          Initech  Software     11
  16  2015-03-27 08:29:45        Mediacore  Software      6
  17  2015-03-21 06:42:41        Mediacore  Hardware     19
  18  2015-03-15 08:50:45          Initech  Hardware     18
  19  2015-03-13 16:25:24        Streeplex  Software      9)]
```

```
In [18]: month_dict
Out[18]: 
{'february':                  Units
 Company               
 Acme Coporation     34
 Hooli               30
 Initech             30
 Mediacore           45
 Streeplex           37, 'january':                  Units
 Company               
 Acme Coporation     76
 Hooli               70
 Initech             37
 Mediacore           15
 Streeplex           50, 'march':                  Units
 Company               
 Acme Coporation      5
 Hooli               37
 Initech             68
 Mediacore           68
 Streeplex           40}
```

```
<script.py> output:
                              Units
             Company               
    february Acme Coporation     34
             Hooli               30
             Initech             30
             Mediacore           45
             Streeplex           37
    january  Acme Coporation     76
             Hooli               70
             Initech             37
             Mediacore           15
             Streeplex           50
    march    Acme Coporation      5
             Hooli               37
             Initech             68
             Mediacore           68
             Streeplex           40
             
             
                        Units
             Company         
    february Mediacore     45
    january  Mediacore     15
    march    Mediacore     68
```
#### Comment:
Well done! Now that you've mastered of the basics of concatenating your data, it's time to learn about different types of joins!
