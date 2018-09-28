# Chapter 04: Grouping Data

## 01. Advantages of categorical data types
What are the main advantages of storing data explicitly as categorical types instead of object types?

### Possible Answers
* Computations are faster.
press 1
* Categorical data require less space in memory.
press 2
* All of the above.
press 3
* None of the above.
press 4

#### Answer:
3

#### Comment:
Correct! Computations are faster and categorical data require less space in memory.

## 02. Grouping by multiple columns
In this exercise, you will return to working with the Titanic dataset from Chapter 1 and use .groupby() to analyze the distribution of passengers who boarded the Titanic.

The 'pclass' column identifies which class of ticket was purchased by the passenger and the 'embarked' column indicates at which of the three ports the passenger boarded the Titanic. 'S' stands for Southampton, England, 'C' for Cherbourg, France and 'Q' for Queenstown, Ireland.

Your job is to first group by the 'pclass' column and count the number of rows in each class using the 'survived' column. You will then group by the 'embarked' and 'pclass' columns and count the number of passengers.

The DataFrame has been pre-loaded as titanic.

### Instructions:
* Group by the 'pclass' column and save the result as by_class.
* Aggregate the 'survived' column of by_class using .count(). Save the result as count_by_class.
* Print count_by_class. This has been done for you.
* Group titanic by the 'embarked' and 'pclass' columns. Save the result as by_mult.
* Aggregate the 'survived' column of by_mult using .count(). Save the result as count_mult.
* Print count_mult. This has been done for you, so hit 'Submit Answer' to view the result.

#### Script:
```
# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked', 'pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)
```
#### Output:
```
<script.py> output:
    pclass
    1    323
    2    277
    3    709
    Name: survived, dtype: int64
    embarked  pclass
    C         1         141
              2          28
              3         101
    Q         1           3
              2           7
              3         113
    S         1         177
              2         242
              3         495
    Name: survived, dtype: int64
```
#### Comment:
Well done! Grouping your data by certain columns like this and aggregating them by another column - in this case, 'survived' - allows you to carefully examine your data for interesting insights.

## 03. Grouping by another series
In this exercise, you'll use two data sets from Gapminder.org to investigate the average life expectancy (in years) at birth in 2010 for the 6 continental regions. To do this you'll read the life expectancy data per country into one pandas DataFrame and the association between country and region into another.

By setting the index of both DataFrames to the country name, you'll then use the region information to group the countries in the life expectancy DataFrame and compute the mean value for 2010.

The life expectancy CSV file is available to you in the variable life_fname and the regions filename is available in the variable regions_fname.

### Instructions:
* Read life_fname into a DataFrame called life and set the index to 'Country'.
* Read regions_fname into a DataFrame called regions and set the index to 'Country'.
* Group life by the region column of regions and store the result in life_by_region.
* Print the mean over the 2010 column of life_by_region.

#### Script:
```
# Read life_fname into a DataFrame: life
life = pd.read_csv(life_fname, index_col='Country')

# Read regions_fname into a DataFrame: regions
regions = pd.read_csv(regions_fname, index_col='Country')

# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())
```

#### Output:
```
<script.py> output:
    region
    America                       74.037350
    East Asia & Pacific           73.405750
    Europe & Central Asia         75.656387
    Middle East & North Africa    72.805333
    South Asia                    68.189750
    Sub-Saharan Africa            57.575080
    Name: 2010, dtype: float64
```

#### Comment:
Great work! It looks like the average life expectancy (in years) at birth in 2010 was highest in Europe & Central Asia and lowest in Sub-Saharan Africa.

## 04. Computing multiple aggregates of multiple columns
The .agg() method can be used with a tuple or list of aggregations as input. When applying multiple aggregations on multiple columns, the aggregated DataFrame has a multi-level column index.

In this exercise, you're going to group passengers on the Titanic by 'pclass' and aggregate the 'age' and 'fare' columns by the functions 'max' and 'median'. You'll then use multi-level selection to find the oldest passenger per class and the median fare price per class.

The DataFrame has been pre-loaded as titanic.

### Instructions:
* Group titanic by 'pclass' and save the result as by_class.
* Select the 'age' and 'fare' columns from by_class and save the result as by_class_sub.
* Aggregate by_class_sub using 'max' and 'median'. You'll have to pass 'max' and 'median' in the form of a list to .agg().
* Use .loc[] to print all of the rows and the column specification ('age','max'). This has been done for you.
* Use .loc[] to print all of the rows and the column specification ('fare','median').

#### Script:
```
# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max', 'median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:, ('fare', 'median')])
```
#### Output:
```
<script.py> output:
    pclass
    1    80.0
    2    70.0
    3    74.0
    Name: (age, max), dtype: float64
    pclass
    1    60.0000
    2    15.0458
    3     8.0500
    Name: (fare, median), dtype: float64
```
#### Comment:
Fantastic work! It isn't surprising that the highest median fare was for the 1st passenger class.

## 05. Aggregating on index levels/fields
If you have a DataFrame with a multi-level row index, the individual levels can be used to perform the groupby. This allows advanced aggregation techniques to be applied along one or more levels in the index and across one or more columns.

In this exercise you'll use the full Gapminder dataset which contains yearly values of life expectancy, population, child mortality (per 1,000) and per capita gross domestic product (GDP) for every country in the world from 1964 to 2013.

Your job is to create a multi-level DataFrame of the columns 'Year', 'Region' and 'Country'. Next you'll group the DataFrame by the 'Year' and 'Region' levels. Finally, you'll apply a dictionary aggregation to compute the total population, spread of per capita GDP values and average child mortality rate.

The Gapminder CSV file is available as 'gapminder.csv'.

### Instructions:
* Read 'gapminder.csv' into a DataFrame with index_col=['Year','region','Country']. Sort the index.
* Group gapminder with a level of ['Year','region'] using its level parameter. Save the result as by_year_region.
* Define the function spread which returns the maximum and minimum of an input series. This has been done for you.
* Create a dictionary with 'population':'sum', 'child_mortality':'mean' and 'gdp':spread as aggregator. This has been done for you.
* Use the aggregator dictionary to aggregate by_year_region. Save the result as aggregated.
* Print the last 6 entries of aggregated. This has been done for you, so hit 'Submit Answer' to view the result.

#### Script:
```
# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder.csv', index_col=['Year', 'region', 'Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(['Year', 'region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))
```
#### Output:
```
<script.py> output:
                                     child_mortality    population       gdp
    Year region                                                             
    2013 America                           17.745833  9.629087e+08   49634.0
         East Asia & Pacific               22.285714  2.244209e+09  134744.0
         Europe & Central Asia              9.831875  8.968788e+08   86418.0
         Middle East & North Africa        20.221500  4.030504e+08  128676.0
         South Asia                        46.287500  1.701241e+09   11469.0
         Sub-Saharan Africa                76.944490  9.205996e+08   32035.0
```
#### Comment:
Excellent work! Are you able to see any correlations between population, child_mortality, and gdp?

## 06. Grouping on a function of the index
Groupby operations can also be performed on transformations of the index values. In the case of a DateTimeIndex, we can extract portions of the datetime over which to group.

In this exercise you'll read in a set of sample sales data from February 2015 and assign the 'Date' column as the index. Your job is to group the sales data by the day of the week and aggregate the sum of the 'Units' column.

Is there a day of the week that is more popular for customers? To find out, you're going to use .strftime('%a') to transform the index datetime values to abbreviated days of the week.

The sales data CSV file is available to you as 'sales.csv'.

### Instructions:
* Read 'sales.csv' into a DataFrame with index_col='Date' and parse_dates=True.
* Create a groupby object with sales.index.strftime('%a') as input and assign it to by_day.
* Aggregate the 'Units' column of by_day with the .sum() method. Save the result as units_sum.
* Print units_sum. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# Read file: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Create a groupby object: by_day
# strftime --> string to format date
# source: https://apidock.com/ruby/DateTime/strftime
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sums
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)

```
#### Output:
```

In [8]: sales.head()
Out[8]: 
                             Company   Product  Units
Date                                                 
2015-02-02 08:30:00            Hooli  Software      3
2015-02-02 21:00:00        Mediacore  Hardware      9
2015-02-03 14:00:00          Initech  Software     13
2015-02-04 15:30:00        Streeplex  Software     13
2015-02-04 22:00:00  Acme Coporation  Hardware     14

<script.py> output:
    Mon    48
    Sat     7
    Thu    59
    Tue    13
    Wed    48
    Name: Units, dtype: int64
```
#### Comment:
Well done! It looks like Monday, Wednesday, and Thursday were the most popular days for customers!

## 07. Detecting outliers with Z-Scores
As Dhavide demonstrated in the video using the zscore function, you can apply a .transform() method after grouping to apply a function to groups of data independently. The z-score is also useful to find outliers: a z-score value of +/- 3 is generally considered to be an outlier.

In this example, you're going to normalize the Gapminder data in 2010 for life expectancy and fertility by the z-score per region. Using boolean indexing, you will filter out countries that have high fertility rates and low life expectancy for their region.

The Gapminder DataFrame for 2010 indexed by 'Country' is provided for you as gapminder_2010.

### Instructions:
* Import zscore from scipy.stats.
* Group gapminder_2010 by 'region' and transform the ['life','fertility'] columns by zscore.
* Construct a boolean Series of the bitwise or between standardized['life'] < -3 and standardized['fertility'] > 3.
* Filter gapminder_2010 using .loc[] and the outliers Boolean Series. Save the result as gm_outliers.
* Print gm_outliers. This has been done for you, so hit 'Submit Answer' to see the results.

#### Script:
```
# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')['life', 'fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)
```

#### Output:
```
In [13]: gapminder_2010.groupby('region')['life', 'fertility'].head()
Out[13]: 
                       life  fertility
Country                               
Afghanistan          59.612      5.659
Albania              76.780      1.741
Algeria              70.615      2.817
Angola               50.689      6.218
Antigua and Barbuda  75.437      2.130
Argentina            75.772      2.215
Armenia              74.291      1.550
Aruba                75.059      1.701
Australia            82.091      1.886
Austria              80.595      1.438
Azerbaijan           70.518      1.970
Bahamas              74.757      1.901
Bahrain              76.203      2.142
Bangladesh           69.449      2.277
Barbados             74.875      1.839
Belarus              69.613      1.460
Benin                58.797      5.095
Bhutan               67.015      2.375
Botswana             46.588      2.761
Brunei               77.956      2.051
Burkina Faso         55.081      5.869
Burundi              52.638      6.304
Cambodia             70.811      2.966
China                74.868      1.650
Djibouti             60.307      3.604
Egypt                70.478      2.883
Fiji                 69.258      2.670
India                65.650      2.563
Iran                 73.094      1.904
Maldives             76.779      2.339

In [14]: standardized.head()
Out[14]: 
                         life  fertility
Country                                 
Afghanistan         -1.743601   2.504732
Albania              0.226367   0.010964
Algeria             -0.440196  -0.003972
Angola              -0.882537   1.095653
Antigua and Barbuda  0.240607  -0.363761

In [16]: outliers.head()
Out[16]: 
Country
Afghanistan            False
Albania                False
Algeria                False
Angola                 False
Antigua and Barbuda    False
dtype: bool

In [19]: gm_outliers.head()
Out[19]: 
             fertility    life  population  child_mortality     gdp                 region
Country                                                                                   
Guatemala        3.974  71.100  14388929.0             34.5  6849.0                America
Haiti            3.350  45.000   9993247.0            208.8  1518.0                America
Tajikistan       3.780  66.830   6878637.0             52.6  2110.0  Europe & Central Asia
Timor-Leste      6.237  65.952   1124355.0             63.8  1777.0    East Asia & Pacific
```
#### Comment:
Wonderful work! Using z-scores like this is a great way to identify outliers in your data.
