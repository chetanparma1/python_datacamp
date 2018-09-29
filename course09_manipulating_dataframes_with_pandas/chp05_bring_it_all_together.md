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
