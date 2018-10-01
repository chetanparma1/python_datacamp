# Chapter 05: Bring It All Together

## 01. Grouping and aggregating
The Olympic medal data for the following exercises comes from The Guardian. It comprises records of all events held at the Olympic games between 1896 and 2012.

Suppose you have loaded the data into a DataFrame medals. You now want to find the total number of medals awarded to the USA per edition. To do this, filter the 'USA' rows and use the groupby() function to put the 'Edition' column on the index:

USA_edition_grouped = medals.loc[medals.NOC == 'USA'].groupby('Edition')
Given the goal of finding the total number of USA medals awarded per edition, what column should you select and which aggregation method should you use?

### Possible Answers
* USA_edition_grouped['City'].mean()
press 1
* USA_edition_grouped['Athlete'].sum()
press 2
* USA_edition_grouped['Medal'].count()
press 3
* USA_edition_grouped['Gender'].first()
press 4

#### Script & Output:
```
In [1]: medals.head()
Out[1]: 
     City  Edition     Sport Discipline             Athlete  NOC Gender                       Event Event_gender   Medal
0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men              100m freestyle            M    Gold
1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men              100m freestyle            M  Silver
2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men  100m freestyle for sailors            M  Bronze
3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men  100m freestyle for sailors            M    Gold
4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men  100m freestyle for sailors            M  Silver


In [2]: medals.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 29216 entries, 0 to 29215
Data columns (total 10 columns):
City            29216 non-null object
Edition         29216 non-null int64
Sport           29216 non-null object
Discipline      29216 non-null object
Athlete         29216 non-null object
NOC             29216 non-null object
Gender          29216 non-null object
Event           29216 non-null object
Event_gender    29216 non-null object
Medal           29216 non-null object
dtypes: int64(1), object(9)
memory usage: 2.2+ MB


In [19]: medals.loc[medals['NOC'] == 'USA'].groupby('Edition')['Medal'].count()
Out[19]: 
Edition
1896     20
1900     55
1904    394
1908     63
1912    101
1920    193
1924    198
1928     84
1932    181
1936     92
1948    148
1952    130
1956    118
1960    112
1964    150
1968    149
1972    155
1976    155
1984    333
1988    193
1992    224
1996    260
2000    248
2004    264
2008    315
Name: Medal, dtype: int64
```

#### Answer:
3

#### Comment:
Correct - great work!

## 02. Using .value_counts() for ranking
For this exercise, you will use the pandas Series method .value_counts() to determine the top 15 countries ranked by total number of medals.

Notice that .value_counts() sorts by values by default. The result is returned as a Series of counts indexed by unique entries from the original Series with values (counts) ranked in descending order.

The DataFrame has been pre-loaded for you as medals.

### Instructions:
* Extract the 'NOC' column from the DataFrame medals and assign the result to country_names. Notice that this Series has repeated entries for every medal (of any type) a country has won in any Edition of the Olympics.
* Create a Series medal_counts by applying .value_counts() to the Series country_names.
* Print the top 15 countries ranked by total number of medals won. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# Select the 'NOC' column of medals: country_names
country_names = medals.NOC

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()
# medal_counts2 = medals.groupby(country_names)['Medal'].count()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))

```
#### Output:
```
<script.py> output:
    USA    4335
    URS    2049
    GBR    1594
    FRA    1314
    ITA    1228
    GER    1211
    AUS    1075
    HUN    1053
    SWE    1021
    GDR     825
    NED     782
    JPN     704
    CHN     679
    RUS     638
    ROU     624
    Name: NOC, dtype: int64
```

#### Comment:
Well done! It looks like the top 5 countries here are USA, URS, GBR, FRA, and ITA.

## 03. Using .pivot_table() to count medals by type
Rather than ranking countries by total medals won and showing that list, you may want to see a bit more detail. You can use a pivot table to compute how many separate bronze, silver and gold medals each country won. That pivot table can then be used to repeat the previous computation to rank by total medals won.

In this exercise, you will use .pivot_table() first to aggregate the total medals by type. Then, you can use .sum() along the columns of the pivot table to produce a new column. When the modified pivot table is sorted by the total medals column, you can display the results from the last exercise with a bit more detail.

### Instructions:
* Construct a pivot table counted from the DataFrame medals aggregating by count. Use 'NOC' as the index, 'Athlete' for the values, and 'Medal' for the columns.
* Modify the DataFrame counted by adding a column counted['totals']. The new column 'totals' should contain the result of taking the sum along the columns (i.e., use .sum(axis='columns')).
* Overwrite the DataFrame counted by sorting it with the .sort_values() method. Specify the keyword argument ascending=False.
* Print the first 15 rows of counted using .head(15). This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC', columns='Medal', values='Athlete', aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values(by='totals', ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))
```
#### Output:
```
# counted before adding column 'totals'
In [7]: counted
Out[7]: 
Medal  Bronze    Gold  Silver
NOC                          
AFG       1.0     NaN     NaN
AHO       NaN     NaN     1.0
ALG       8.0     4.0     2.0
ANZ       5.0    20.0     4.0
ARG      88.0    68.0    83.0
ARM       7.0     1.0     1.0
AUS     413.0   293.0   369.0
AUT      44.0    21.0    81.0
AZE       9.0     4.0     3.0
BAH       5.0     9.0     9.0
BAR       1.0     NaN     NaN
BDI       NaN     1.0     NaN
BEL     150.0    91.0   167.0
BER       1.0     NaN     NaN
BLR      53.0    14.0    25.0
BOH       6.0     NaN     1.0
BRA     174.0    59.0   139.0
BUL     136.0    53.0   142.0
BWI       5.0     NaN     NaN
CAN     227.0   154.0   211.0
CHI      21.0     3.0     9.0
CHN     193.0   234.0   252.0
CIV       NaN     NaN     1.0
CMR       1.0    20.0     1.0
COL       7.0     1.0     3.0
CRC       2.0     1.0     1.0
CRO      18.0    31.0    30.0

# counted after adding column 'totals'
In [14]: counted.head(10)
Out[14]: 
Medal  Bronze    Gold  Silver  totals
NOC                                  
USA    1052.0  2088.0  1195.0  4335.0
URS     584.0   838.0   627.0  2049.0
GBR     505.0   498.0   591.0  1594.0
FRA     475.0   378.0   461.0  1314.0
ITA     374.0   460.0   394.0  1228.0
GER     454.0   407.0   350.0  1211.0
AUS     413.0   293.0   369.0  1075.0
HUN     345.0   400.0   308.0  1053.0
SWE     325.0   347.0   349.0  1021.0
GDR     225.0   329.0   271.0   825.0

<script.py> output:
    Medal  Bronze    Gold  Silver  totals
    NOC                                  
    USA    1052.0  2088.0  1195.0  4335.0
    URS     584.0   838.0   627.0  2049.0
    GBR     505.0   498.0   591.0  1594.0
    FRA     475.0   378.0   461.0  1314.0
    ITA     374.0   460.0   394.0  1228.0
    GER     454.0   407.0   350.0  1211.0
    AUS     413.0   293.0   369.0  1075.0
    HUN     345.0   400.0   308.0  1053.0
    SWE     325.0   347.0   349.0  1021.0
    GDR     225.0   329.0   271.0   825.0
    NED     320.0   212.0   250.0   782.0
    JPN     270.0   206.0   228.0   704.0
    CHN     193.0   234.0   252.0   679.0
    RUS     240.0   192.0   206.0   638.0
    ROU     282.0   155.0   187.0   624.0
```
#### Comment:
Fantastic work! Take a moment to look at the results and see if you find anything interesting!

## 04. Applying .drop_duplicates()
What could be the difference between the 'Event_gender' and 'Gender' columns? You should be able to evaluate your guess by looking at the unique values of the pairs (Event_gender, Gender) in the data. In particular, you should not see something like (Event_gender='M', Gender='Women'). However, you will see that, strangely enough, there is an observation with (Event_gender='W', Gender='Men').

The duplicates can be dropped using the .drop_duplicates() method, leaving behind the unique observations. The DataFrame has been loaded as medals.

### Instructions:
* Select the columns 'Event_gender' and 'Gender'.
* Create a dataframe ev_gen_uniques containing the unique pairs contained in ev_gen.
* Print ev_gen_uniques. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# Select columns: ev_gen
ev_gen = medals[['Event_gender', 'Gender']]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)
```

#### Output
```
<script.py> output:
          Event_gender Gender
    0                M    Men
    348              X    Men
    416              W  Women
    639              X  Women
    23675            W    Men
```
#### Comment:
Well done! You'll continue this exploration in the next two exercises.

## 05. Finding possible errors with .groupby()
You will now use .groupby() to continue your exploration. Your job is to group by 'Event_gender' and 'Gender' and count the rows.

You will see that there is only one suspicious row: This is likely a data error.

The DataFrame is available to you as medals.

### Instructions:
* Group medals by 'Event_gender' and 'Gender'.
* Create a medal_count_by_gender DataFrame with a group count using the .count() method.
* Print medal_count_by_gender. This has been done for you, so hit 'Submit Answer' to view the result.

#### Script:
```
# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender', 'Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)
```
#### Output:
```
<script.py> output:
                          City  Edition  Sport  Discipline  Athlete    NOC  Event  Medal
    Event_gender Gender                                                                 
    M            Men     20067    20067  20067       20067    20067  20067  20067  20067
    W            Men         1        1      1           1        1      1      1      1
                 Women    7277     7277   7277        7277     7277   7277   7277   7277
    X            Men      1653     1653   1653        1653     1653   1653   1653   1653
                 Women     218      218    218         218      218    218    218    218
```
#### Comment:
Great work! You're close to identifying the suspicious data point

## 06. Locating suspicious data
You will now inspect the suspect record by locating the offending row.

You will see that, according to the data, Joyce Chepchumba was a man that won a medal in a women's event. That is a data error as you can confirm with a web search.

### Instructions:
* Create a Boolean Series with a condition that captures the only row that has medals.Event_gender == 'W' and medals.Gender == 'Men'. Be sure to use the & operator.
* Use the Boolean Series to create a DataFrame called suspect with the suspicious row.
* Print suspect. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)
```
#### Output:
```
<script.py> output:
             City  Edition      Sport Discipline            Athlete  NOC Gender     Event Event_gender   Medal
    23675  Sydney     2000  Athletics  Athletics  CHEPCHUMBA, Joyce  KEN    Men  marathon            W  Bronze
```
#### Comment:
Fantastic! You have to always watch out for errors like this in your data.
