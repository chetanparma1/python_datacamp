# Chapter 01: Preparing Data

## Reading DataFrames from multiple files
When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.

The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.

The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).

### Instructions:
* Import pandas as pd.
* Read the file 'Bronze.csv' into a DataFrame called bronze.
* Read the file 'Silver.csv' into a DataFrame called silver.
* Read the file 'Gold.csv' into a DataFrame called gold.
* Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.

#### Script:
```
# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())
```
#### Output:
```
<script.py> output:
       NOC         Country   Total
    0  USA   United States  2088.0
    1  URS    Soviet Union   838.0
    2  GBR  United Kingdom   498.0
    3  FRA          France   378.0
    4  GER         Germany   407.0
```
#### Comment:
Well done! Reading csv files into DataFrames like this should now be second nature to you!

## 02. Reading DataFrames from multiple files in a loop
As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.

Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.

Here, you'll continue working with <a href="https://www.theguardian.com/sport/datablog/2012/jun/25/olympic-medal-winner-list-data">The Guardian's Olympic medal dataset</a>.

### Instructions:
* Create a list of file names called filenames with three strings 'Gold.csv', 'Silver.csv', & 'Bronze.csv'. This has been done for you.
* Use a for loop to create another list called dataframes containing the three DataFrames loaded from filenames:
** Iterate over filenames.
** Read each CSV file in filenames into a DataFrame and append it to dataframes by using pd.read_csv() inside a call to .append().
* Print the first 5 rows of the first DataFrame of the list dataframes. This has been done for you, so hit 'Submit Answer' to see the results.

#### Script:
```
# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())
```
#### Output:
```
<script.py> output:
       NOC         Country   Total
    0  USA   United States  2088.0
    1  URS    Soviet Union   838.0
    2  GBR  United Kingdom   498.0
    3  FRA          France   378.0
    4  GER         Germany   407.0

```
#### Comment:
Great work! When you are dealing with multiple csv files like this, it is more efficient to read them into DataFrames using a loop.

## 03. Combining DataFrames from multiple data files
In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.

Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.

### Instructions:
* Construct a copy of the DataFrame gold called medals using the .copy() method.
* Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
* Rename the columns of medals by assigning new_labels to medals.columns.
* Create new columns 'Silver' and 'Bronze' in medals using silver['Total'] & bronze['Total'].
* Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())
```
#### Output:
```
<script.py> output:
       NOC         Country    Gold  Silver  Bronze
    0  USA   United States  2088.0  1195.0  1052.0
    1  URS    Soviet Union   838.0   627.0   584.0
    2  GBR  United Kingdom   498.0   591.0   505.0
    3  FRA          France   378.0   461.0   475.0
    4  GER         Germany   407.0   350.0   454.0
```
#### Comment:
Excellent! Later in this course, you'll learn far more powerful tools for combining DataFrames!

## 04. Sorting DataFrame with the Index & columns
It is often useful to rearrange the sequence of the rows of a DataFrame by sorting. You don't have to implement these yourself; the principal methods for doing this are .sort_index() and .sort_values().

In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.

### Instructions:
* Read 'monthly_max_temp.csv' into a DataFrame called weather1 with 'Month' as the index.
* Sort the index of weather1 in alphabetical order using the .sort_index() method and store the result in weather2.
* Sort the index of weather1 in reverse alphabetical order by specifying the additional keyword argument ascending=False inside .sort_index().
* Use the .sort_values() method to sort weather1 in increasing numerical order according to the values of the column 'Max TemperatureF'.

#### Script:
```
# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())
```
#### Output:
```
<script.py> output:
           Max TemperatureF
    Month                  
    Jan                  68
    Feb                  60
    Mar                  68
    Apr                  84
    May                  88
           Max TemperatureF
    Month                  
    Apr                  84
    Aug                  86
    Dec                  68
    Feb                  60
    Jan                  68
           Max TemperatureF
    Month                  
    Sep                  90
    Oct                  84
    Nov                  72
    May                  88
    Mar                  68
           Max TemperatureF
    Month                  
    Feb                  60
    Jan                  68
    Mar                  68
    Dec                  68
    Nov                  72
```
#### Comment:
Good job! Being able to sort DataFrames is an important skill. When your DataFrames are sorted, it becomes easier to see how you can combine them.

## 05. Reindexing DataFrame from a list
Sorting methods are not the only way to change DataFrame Indexes. There is also the .reindex() method.

In this exercise, you'll reindex a DataFrame of quarterly-sampled mean temperature values to contain monthly samples (this is an example of upsampling or increasing the rate of samples, which you may recall from the <a href="https://www.datacamp.com/courses/pandas-foundations">pandas Foundations</a> course).

The original data has the first month's abbreviation of the quarter (three-month interval) on the Index, namely Apr, Jan, Jul, and Oct. This data has been loaded into a DataFrame called weather1 and has been printed in its entirety in the IPython Shell. Notice it has only four rows (corresponding to the first month of each quarter) and that the rows are not sorted chronologically.

You'll initially use a list of all twelve month abbreviations and subsequently apply the .ffill() method to forward-fill the null entries when upsampling. This list of month abbreviations has been pre-loaded as year.

### Instructions:
* Reorder the rows of weather1 using the .reindex() method with the list year as the argument, which contains the abbreviations for each month.
* Reorder the rows of weather1 just as you did above, this time chaining the .ffill() method to replace the null values with the last preceding non-null value.

#### Script:
```
# Import pandas
import pandas as pd

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)
```
#### Output:
```
<script.py> output:
           Mean TemperatureF
    Month                   
    Jan            32.133333
    Feb                  NaN
    Mar                  NaN
    Apr            61.956044
    May                  NaN
    Jun                  NaN
    Jul            68.934783
    Aug                  NaN
    Sep                  NaN
    Oct            43.434783
    Nov                  NaN
    Dec                  NaN
           Mean TemperatureF
    Month                   
    Jan            32.133333
    Feb            32.133333
    Mar            32.133333
    Apr            61.956044
    May            61.956044
    Jun            61.956044
    Jul            68.934783
    Aug            68.934783
    Sep            68.934783
    Oct            43.434783
    Nov            43.434783
    Dec            43.434783
```
#### Comment:
Great work! Notice that values corresponding to months missing from weather1 are filled with NaN values in weather2. This does not happen in weather3, since you used forward-fill.

## 06. Reindexing using another DataFrame Index
Another common technique is to reindex a DataFrame using the Index of another DataFrame. The DataFrame .reindex() method can accept the Index of a DataFrame or Series as input. You can access the Index of a DataFrame with its .index attribute.

The Baby Names Dataset from data.gov summarizes counts of names (with genders) from births registered in the US since 1881. In this exercise, you will start with two baby-names DataFrames names_1981 and names_1881 loaded for you.

The DataFrames names_1981 and names_1881 both have a MultiIndex with levels name and gender giving unique labels to counts in each row. If you're interested in seeing how the MultiIndexes were set up, names_1981 and names_1881 were read in using the following commands:
```
names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))
```
As you can see by looking at their shapes, which have been printed in the IPython Shell, the DataFrame corresponding to 1981 births is much larger, reflecting the greater diversity of names in 1981 as compared to 1881.

Your job here is to use the DataFrame .reindex() and .dropna() methods to make a DataFrame common_names counting names from 1881 that were still popular in 1981.

### Instructions:
* Create a new DataFrame common_names by reindexing names_1981 using the Index of the DataFrame names_1881 of older names.
* Print the shape of the new common_names DataFrame. This has been done for you. It should be the same as that of names_1881.
* Drop the rows of common_names that have null counts using the .dropna() method. These rows correspond to names that fell out of fashion between 1881 & 1981.
* Print the shape of the reassigned common_names DataFrame. This has been done for you, so hit 'Submit Answer' to see the result!

#### Output:
```
# Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)
```
#### Output:
```
<script.py> output:
    (1935, 1)
    (1587, 1)
```
#### Comment:
Excellent work! It looks like 348 names fell out of fashion between 1881 and 1981!

## 07. Adding unaligned DataFrames
The DataFrames january and february, which have been printed in the IPython Shell, represent the sales a company made in the corresponding months.

The Indexes in both DataFrames are called Company, identifying which company bought that quantity of units. The column Units is the number of units sold.

If you were to add these two DataFrames by executing the command total = january + february, how many rows would the resulting DataFrame have? Try this in the IPython Shell and find out for yourself.

### Possible Answers
* 3 rows.
press 1
* 4 rows.
press 2
* 5 rows.
press 3
* 6 rows.
press 4

#### Script & Output:
```
january
                  Units
Company                
Acme Corporation     19
Hooli                17
Initech              20
Mediacore            10
Streeplex            13

february
                  Units
Company                
Acme Corporation     15
Hooli                 3
Mediacore            13
Vandelay Inc         25

In [1]: total = january + february

In [2]: total
Out[2]: 
                  Units
Company                
Acme Corporation   34.0
Hooli              20.0
Initech             NaN
Mediacore          23.0
Streeplex           NaN
Vandelay Inc        NaN
```
#### Answer:
4

#### Comment:
Correct! january and february both consist of the sales of the Companies Acme Corporation, Hooli, and Mediacore. january has the additional two companies Initech and Streeplex, while february has the additional company Vandelay Inc. Together, they consist of the sales of 6 unique companies, and so total would have 6 rows.

## 08. Broadcasting in arithmetic formulas
In this exercise, you'll work with weather data pulled from wunderground.com. The DataFrame weather has been pre-loaded along with pandas as pd. It has 365 rows (observed each day of the year 2013 in Pittsburgh, PA) and 22 columns reflecting different weather measurements each day.

You'll subset a collection of columns related to temperature measurements in degrees Fahrenheit, convert them to degrees Celsius, and relabel the columns of the new DataFrame to reflect the change of units.

Remember, ordinary arithmetic operators (like +, -, *, and /) broadcast scalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.

### Instructions:
* Create a new DataFrame temps_f by extracting the columns 'Min TemperatureF', 'Mean TemperatureF', & 'Max TemperatureF' from weather as a new DataFrame temps_f. To do this, pass the relevant columns as a list to weather[].
* Create a new DataFrame temps_c from temps_f using the formula (temps_f - 32) * 5/9.
* Rename the columns of temps_c to replace 'F' with 'C' using the .str.replace('F', 'C') method on temps_c.columns.
* Print the first 5 rows of DataFrame temps_c. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32)*5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F', 'C')

# Print first 5 rows of temps_c
print(temps_c.head())
```

#### Output:
```
<script.py> output:
                Min TemperatureC  Mean TemperatureC  Max TemperatureC
    Date                                                             
    2013-01-01         -6.111111          -2.222222          0.000000
    2013-01-02         -8.333333          -6.111111         -3.888889
    2013-01-03         -8.888889          -4.444444          0.000000
    2013-01-04         -2.777778          -2.222222         -1.111111
    2013-01-05         -3.888889          -1.111111          1.111111
```

#### Comment:
Well done! In only three lines of code, you converted the units of 365 data points (over three columns) from degrees Fahrenheit to degrees Celsius.

## 09. Computing percentage growth of GDP
Your job in this exercise is to compute the yearly percent-change of US GDP (Gross Domestic Product) since 2008.

The data has been obtained from the Federal Reserve Bank of St. Louis and is available in the file GDP.csv, which contains quarterly data; you will resample it to annual sampling and then compute the annual growth of GDP. For a refresher on resampling, check out the relevant material from pandas Foundations.

### Instructions:
* Read the file 'GDP.csv' into a DataFrame called gdp.
* Use parse_dates=True and index_col='DATE'.
* Create a DataFrame post2008 by slicing gdp such that it comprises all rows from 2008 onward.
* Print the last 8 rows of the slice post2008. This has been done for you. This data has quarterly frequency so the indices are separated by three-month intervals.
* Create the DataFrame yearly by resampling the slice post2008 by year. Remember, you need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; you will use the aggregation method .last() to select the last element when resampling.
* Compute the percentage growth of the resampled DataFrame yearly with .pct_change() * 100.

#### Script:
```
import pandas as pd

# Read 'GDP.csv' into a DataFrame: gdp
gdp = pd.read_csv('GDP.csv', index_col='DATE', parse_dates=True)

# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc['2008':]

# Print the last 8 rows of post2008
print(post2008.tail(8))

# Resample post2008 by year, keeping last(): yearly
yearly = post2008.resample('A').last()

# Print yearly
print(yearly)

# Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change()*100

# Print yearly again
print(yearly)
```
#### Output:
```
<script.py> output:
                  VALUE
    DATE               
    2014-07-01  17569.4
    2014-10-01  17692.2
    2015-01-01  17783.6
    2015-04-01  17998.3
    2015-07-01  18141.9
    2015-10-01  18222.8
    2016-01-01  18281.6
    2016-04-01  18436.5
                  VALUE
    DATE               
    2008-12-31  14549.9
    2009-12-31  14566.5
    2010-12-31  15230.2
    2011-12-31  15785.3
    2012-12-31  16297.3
    2013-12-31  16999.9
    2014-12-31  17692.2
    2015-12-31  18222.8
    2016-12-31  18436.5
                  VALUE    growth
    DATE                         
    2008-12-31  14549.9       NaN
    2009-12-31  14566.5  0.114090
    2010-12-31  15230.2  4.556345
    2011-12-31  15785.3  3.644732
    2012-12-31  16297.3  3.243524
    2013-12-31  16999.9  4.311144
    2014-12-31  17692.2  4.072377
    2015-12-31  18222.8  2.999062
    2016-12-31  18436.5  1.172707
```
#### Comment:
Fantastic! Note that the first column of the 'growth' column is NaN because there is no data for the year 2007.

## 10. Converting currency of stocks
In this exercise, stock prices in US Dollars for the S&P 500 in 2015 have been obtained from Yahoo Finance. The files sp500.csv for sp500 and exchange.csv for the exchange rates are both provided to you.

Using the daily exchange rate to Pounds Sterling, your task is to convert both the Open and Close column prices.

### Instructions:
* Read the DataFrames sp500 & exchange from the files 'sp500.csv' & 'exchange.csv' respectively..
* Use parse_dates=True and index_col='Date'.
* Extract the columns 'Open' & 'Close' from the DataFrame sp500 as a new DataFrame dollars and print the first 5 rows.
* Construct a new DataFrame pounds by converting US dollars to British pounds. You'll use the .multiply() method of dollars with exchange['GBP/USD'] and axis='rows'
* Print the first 5 rows of the new DataFrame pounds. This has been done for you, so hit 'Submit Answer' to see the results!.

#### Script
```
# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', index_col='Date', parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', index_col='Date', parse_dates=True)

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

# Print the head of pounds
print(pounds.head())
```
#### Output:
```
<script.py> output:
                       Open        Close
    Date                                
    2015-01-02  2058.899902  2058.199951
    2015-01-05  2054.439941  2020.579956
    2015-01-06  2022.150024  2002.609985
    2015-01-07  2005.550049  2025.900024
    2015-01-08  2030.609985  2062.139893
                       Open        Close
    Date                                
    2015-01-02  1340.364425  1339.908750
    2015-01-05  1348.616555  1326.389506
    2015-01-06  1332.515980  1319.639876
    2015-01-07  1330.562125  1344.063112
    2015-01-08  1343.268811  1364.126161

```
#### Comment:
Excellent! Now that you've become familiar with how to share information between DataFrames, you'll learn about concatenating DataFrames in the next chapter.
