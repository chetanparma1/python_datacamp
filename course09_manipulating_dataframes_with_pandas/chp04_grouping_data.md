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

## 08. Filling missing data (imputation) by group
Many statistical and machine learning packages cannot determine the best action to take when missing data entries are encountered. Dealing with missing data is natural in pandas (both in using the default behavior and in defining a custom behavior). In Chapter 1, you practiced using the .dropna() method to drop missing values. Now, you will practice imputing missing values. You can use .groupby() and .transform() to fill missing data appropriately for each group.

Your job is to fill in missing 'age' values for passengers on the Titanic with the median age from their 'gender' and 'pclass'. To do this, you'll group by the 'sex' and 'pclass' columns and transform each group with a custom function to call .fillna() and impute the median value.

The DataFrame has been pre-loaded as titanic. Explore it in the IPython Shell by printing the output of titanic.tail(10). Notice in particular the NaNs in the 'age' column.

### Instructions:
* Group titanic by 'sex' and 'pclass'. Save the result as by_sex_class.
* Write a function called impute_median() that fills missing values with the median of a series. This has been done for you.
* Call .transform() with impute_median on the 'age' column of by_sex_class.
* Print the output of titanic.tail(10). This has been done for you - hit 'Submit Answer' to see how the missing values have now been imputed.

#### Script:
```
# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex', 'pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class['age'].transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))
```
#### Output:
```
In [3]: by_sex_class.head()
Out[3]: 
     pclass  survived                                               name     sex    age  sibsp  parch            ticket      fare    cabin embarked boat   body                                 home.dest
0         1         1                      Allen, Miss. Elisabeth Walton  female  29.00      0      0             24160  211.3375       B5        S    2    NaN                              St Louis, MO
1         1         1                     Allison, Master. Hudson Trevor    male   0.92      1      2            113781  151.5500  C22 C26        S   11    NaN           Montreal, PQ / Chesterville, ON
2         1         0                       Allison, Miss. Helen Loraine  female   2.00      1      2            113781  151.5500  C22 C26        S  NaN    NaN           Montreal, PQ / Chesterville, ON
3         1         0               Allison, Mr. Hudson Joshua Creighton    male  30.00      1      2            113781  151.5500  C22 C26        S  NaN  135.0           Montreal, PQ / Chesterville, ON
4         1         0    Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female  25.00      1      2            113781  151.5500  C22 C26        S  NaN    NaN           Montreal, PQ / Chesterville, ON
5         1         1                                Anderson, Mr. Harry    male  48.00      0      0             19952   26.5500      E12        S    3    NaN                              New York, NY
6         1         1                  Andrews, Miss. Kornelia Theodosia  female  63.00      1      0             13502   77.9583       D7        S   10    NaN                                Hudson, NY
7         1         0                             Andrews, Mr. Thomas Jr    male  39.00      0      0            112050    0.0000      A36        S  NaN    NaN                               Belfast, NI
8         1         1      Appleton, Mrs. Edward Dale (Charlotte Lamson)  female  53.00      2      0             11769   51.4792     C101        S    D    NaN                       Bayside, Queens, NY
9         1         0                            Artagaveytia, Mr. Ramon    male  71.00      0      0          PC 17609   49.5042      NaN        C  NaN   22.0                       Montevideo, Uruguay
323       2         0                                Abelson, Mr. Samuel    male  30.00      1      0         P/PP 3381   24.0000      NaN        C  NaN    NaN                       Russia New York, NY
324       2         1              Abelson, Mrs. Samuel (Hannah Wizosky)  female  28.00      1      0         P/PP 3381   24.0000      NaN        C   10    NaN                       Russia New York, NY
325       2         0                     Aldworth, Mr. Charles Augustus    male  30.00      0      0            248744   13.0000      NaN        S  NaN    NaN                        Bryn Mawr, PA, USA
326       2         0                         Andrew, Mr. Edgardo Samuel    male  18.00      0      0            231945   11.5000      NaN        S  NaN    NaN  Buenos Aires, Argentina / New Jersey, NJ
327       2         0                           Andrew, Mr. Frank Thomas    male  25.00      0      0        C.A. 34050   10.5000      NaN        S  NaN    NaN            Cornwall, England Houghton, MI
328       2         0                               Angle, Mr. William A    male  34.00      1      0            226875   26.0000      NaN        S  NaN    NaN                          Warwick, England
329       2         1  Angle, Mrs. William A (Florence "Mary" Agnes H...  female  36.00      1      0            226875   26.0000      NaN        S   11    NaN                          Warwick, England
333       2         1                            Ball, Mrs. (Ada E Hall)  female  36.00      0      0             28551   13.0000        D        S   10    NaN          Bristol, Avon / Jacksonville, FL
337       2         1                  Beane, Mrs. Edward (Ethel Clarke)  female  19.00      1      0              2908   26.0000      NaN        S   13    NaN                    Norwich / New York, NY
340       2         1                        Becker, Miss. Marion Louise  female   4.00      2      1            230136   39.0000       F4        S   11    NaN        Guntur, India / Benton Harbour, MI
600       3         0                                Abbing, Mr. Anthony    male  42.00      0      0         C.A. 5547    7.5500      NaN        S  NaN    NaN                                       NaN
601       3         0                      Abbott, Master. Eugene Joseph    male  13.00      0      2         C.A. 2673   20.2500      NaN        S  NaN    NaN                       East Providence, RI
602       3         0                        Abbott, Mr. Rossmore Edward    male  16.00      1      1         C.A. 2673   20.2500      NaN        S  NaN  190.0                       East Providence, RI
603       3         1                   Abbott, Mrs. Stanton (Rosa Hunt)  female  35.00      1      1         C.A. 2673   20.2500      NaN        S    A    NaN                       East Providence, RI
604       3         1                        Abelseth, Miss. Karen Marie  female  16.00      0      0            348125    7.6500      NaN        S   16    NaN                    Norway Los Angeles, CA
605       3         1                      Abelseth, Mr. Olaus Jorgensen    male  25.00      0      0            348122    7.6500    F G63        S    A    NaN                        Perkins County, SD
606       3         1           Abrahamsson, Mr. Abraham August Johannes    male  20.00      0      0  SOTON/O2 3101284    7.9250      NaN        S   15    NaN         Taalintehdas, Finland Hoboken, NJ
607       3         1          Abrahim, Mrs. Joseph (Sophie Halaut Easu)  female  18.00      0      0              2657    7.2292      NaN        C    C    NaN                            Greensburg, PA
610       3         0     Ahlin, Mrs. Johan (Johanna Persdotter Larsson)  female  40.00      1      0              7546    9.4750      NaN        S  NaN    NaN                         Sweden Akeley, MN
612       3         1                         Aks, Mrs. Sam (Leah Rosen)  female  18.00      0      1            392091    9.3500      NaN        S   13    NaN               London, England Norfolk, VA


In [7]: titanic.age.head()
Out[7]: 
0    29.00
1     0.92
2     2.00
3    30.00
4    25.00
Name: age, dtype: float64


In [8]: titanic.tail(10)
Out[8]: 
      pclass  survived                                     name     sex   age  sibsp  parch  ticket     fare cabin embarked boat   body home.dest
1299       3         0                      Yasbeck, Mr. Antoni    male  27.0      1      0    2659  14.4542   NaN        C    C    NaN       NaN
1300       3         1  Yasbeck, Mrs. Antoni (Selini Alexander)  female  15.0      1      0    2659  14.4542   NaN        C  NaN    NaN       NaN
1301       3         0                     Youseff, Mr. Gerious    male  45.5      0      0    2628   7.2250   NaN        C  NaN  312.0       NaN
1302       3         0                        Yousif, Mr. Wazli    male  25.0      0      0    2647   7.2250   NaN        C  NaN    NaN       NaN
1303       3         0                    Yousseff, Mr. Gerious    male  25.0      0      0    2627  14.4583   NaN        C  NaN    NaN       NaN
1304       3         0                     Zabour, Miss. Hileni  female  14.5      1      0    2665  14.4542   NaN        C  NaN  328.0       NaN
1305       3         0                    Zabour, Miss. Thamine  female  22.0      1      0    2665  14.4542   NaN        C  NaN    NaN       NaN
1306       3         0                Zakarian, Mr. Mapriededer    male  26.5      0      0    2656   7.2250   NaN        C  NaN  304.0       NaN
1307       3         0                      Zakarian, Mr. Ortin    male  27.0      0      0    2670   7.2250   NaN        C  NaN    NaN       NaN
1308       3         0                       Zimmerman, Mr. Leo    male  29.0      0      0  315082   7.8750   NaN        S  NaN    NaN       NaN
```

#### Comment:
Well done! Imputing missing values intelligently is always preferrable to dropping them entirely!

## 09. Other transformations with .apply
The .apply() method when used on a groupby object performs an arbitrary function on each of the groups. These functions can be aggregations, transformations or more complex workflows. The .apply() method will then combine the results in an intelligent way.

In this exercise, you're going to analyze economic disparity within regions of the world using the Gapminder data set for 2010. To do this you'll define a function to compute the aggregate spread of per capita GDP in each region and the individual country's z-score of the regional per capita GDP. You'll then select three countries - United States, Great Britain and China - to see a summary of the regional GDP and that country's z-score against the regional mean.

The 2010 Gapminder DataFrame is provided for you as gapminder_2010. Pandas has been imported as pd.

The following function has been defined for your use:
```
def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})
```
### Instructions:
* Group gapminder_2010 by 'region'. Save the result as regional.
* Apply the provided disparity function on regional, and save the result as reg_disp.
* Use .loc[] to select ['United States','United Kingdom','China'] from reg_disp and print the results.

#### Script:
```
# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China'], :])
```
#### Output:
```
In [8]: gapminder_2010.head()
Out[8]: 
                     fertility    life  population  child_mortality      gdp                      region
Country                                                                                                 
Afghanistan              5.659  59.612  31411743.0            105.0   1637.0                  South Asia
Albania                  1.741  76.780   3204284.0             16.6   9374.0       Europe & Central Asia
Algeria                  2.817  70.615  35468208.0             27.4  12494.0  Middle East & North Africa
Angola                   6.218  50.689  19081912.0            182.5   7047.0          Sub-Saharan Africa
Antigua and Barbuda      2.130  75.437     88710.0              9.9  20567.0                     America


In [9]: regional.head()
Out[9]: 
                     fertility    life    population  child_mortality      gdp                      region
Country                                                                                                   
Afghanistan              5.659  59.612  3.141174e+07           105.00   1637.0                  South Asia
Albania                  1.741  76.780  3.204284e+06            16.60   9374.0       Europe & Central Asia
Algeria                  2.817  70.615  3.546821e+07            27.40  12494.0  Middle East & North Africa
Angola                   6.218  50.689  1.908191e+07           182.50   7047.0          Sub-Saharan Africa
Antigua and Barbuda      2.130  75.437  8.871000e+04             9.90  20567.0                     America
Argentina                2.215  75.772  4.041238e+07            14.60  15765.0                     America
Armenia                  1.550  74.291  3.092072e+06            18.00   6508.0       Europe & Central Asia
Aruba                    1.701  75.059  1.074880e+05            17.84  33288.0                     America
Australia                1.886  82.091  2.226838e+07             4.80  41330.0         East Asia & Pacific
Austria                  1.438  80.595  8.393644e+06             4.40  42861.0       Europe & Central Asia
Azerbaijan               1.970  70.518  9.187783e+06            39.00  15950.0       Europe & Central Asia
Bahamas                  1.901  74.757  3.428770e+05            13.90  22915.0                     America
Bahrain                  2.142  76.203  1.261835e+06             8.30  40553.0  Middle East & North Africa
Bangladesh               2.277  69.449  1.486921e+08            49.60   2459.0                  South Asia
Barbados                 1.839  74.875  2.733310e+05            14.70  15297.0                     America
Belarus                  1.460  69.613  9.595421e+06             6.10  15703.0       Europe & Central Asia
Benin                    5.095  58.797  8.849892e+06           111.60   1637.0          Sub-Saharan Africa
Bhutan                   2.375  67.015  7.259400e+05            42.30   6516.0                  South Asia
Botswana                 2.761  46.588  2.006945e+06            60.30  13642.0          Sub-Saharan Africa
Brunei                   2.051  77.956  3.989200e+05             9.30  70636.0         East Asia & Pacific
Burkina Faso             5.869  55.081  1.646871e+07           113.50   1431.0          Sub-Saharan Africa
Burundi                  6.304  52.638  8.382849e+06            98.80    725.0          Sub-Saharan Africa
Cambodia                 2.966  70.811  1.413826e+07            43.10   2513.0         East Asia & Pacific
China                    1.650  74.868  1.341335e+09            15.70   9430.0         East Asia & Pacific
Djibouti                 3.604  60.307  8.887160e+05            76.10   2665.0  Middle East & North Africa
Egypt                    2.883  70.478  8.112108e+07            29.00  10615.0  Middle East & North Africa
Fiji                     2.670  69.258  8.606230e+05            23.90   7098.0         East Asia & Pacific
India                    2.563  65.650  1.224614e+09            59.90   4547.0                  South Asia
Iran                     1.904  73.094  7.397363e+07            19.20  16980.0  Middle East & North Africa
Maldives                 2.339  76.779  3.158850e+05            13.00  11674.0                  South Asia


In [10]: reg_disp.head()
Out[10]: 
                     regional spread(gdp)    z(gdp)
Country                                            
Afghanistan                       10037.0 -1.011602
Albania                           89037.0 -0.986190
Algeria                          125319.0 -0.550537
Angola                            33817.0  0.398221
Antigua and Barbuda               47855.0  0.431274


In [11]: reg_disp.loc[['United States','United Kingdom','China'], :]
Out[11]: 
                regional spread(gdp)    z(gdp)
Country                                       
United States                47855.0  3.013374
United Kingdom               89037.0  0.572873
China                        96993.0 -0.432756

```

#### Comment:
Great work!
