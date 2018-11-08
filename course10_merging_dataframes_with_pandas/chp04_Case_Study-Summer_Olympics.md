# Chapter 04: Case Study - Summer Olympics

## 01. Loading Olympic edition DataFrame
In this chapter, you'll be using The Guardian's Olympic medal dataset.

Your first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.

Initially, editions has 26 rows (one for each Olympic edition, i.e., a year in which the Olympics was held) and 7 columns: 'Edition', 'Bronze', 'Gold', 'Silver', 'Grand Total', 'City', and 'Country'.

For the analysis that follows, you won't need the overall medal counts, so you want to keep only the useful columns from editions: 'Edition', 'Grand Total', City, and Country.

### Instructions:
* Read file_path into a DataFrame called editions. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'. You'll have to use the option sep='\t' because the file uses tabs to delimit fields (pd.read_csv() expects commas by default).
* Select only the columns 'Edition', 'Grand Total', 'City', and 'Country' from editions.
* Print the final DataFrame editions in entirety (there are only 26 rows). This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
#Import pandas
import pandas as pd

# Create file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path, sep = '\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)
```
#### Output:
```
<script.py> output:
        Edition  Grand Total         City                     Country
    0      1896          151       Athens                      Greece
    1      1900          512        Paris                      France
    2      1904          470    St. Louis               United States
    3      1908          804       London              United Kingdom
    4      1912          885    Stockholm                      Sweden
    5      1920         1298      Antwerp                     Belgium
    6      1924          884        Paris                      France
    7      1928          710    Amsterdam                 Netherlands
    8      1932          615  Los Angeles               United States
    9      1936          875       Berlin                     Germany
    10     1948          814       London              United Kingdom
    11     1952          889     Helsinki                     Finland
    12     1956          885    Melbourne                   Australia
    13     1960          882         Rome                       Italy
    14     1964         1010        Tokyo                       Japan
    15     1968         1031  Mexico City                      Mexico
    16     1972         1185       Munich  West Germany (now Germany)
    17     1976         1305     Montreal                      Canada
    18     1980         1387       Moscow       U.S.S.R. (now Russia)
    19     1984         1459  Los Angeles               United States
    20     1988         1546        Seoul                 South Korea
    21     1992         1705    Barcelona                       Spain
    22     1996         1859      Atlanta               United States
    23     2000         2015       Sydney                   Australia
    24     2004         1998       Athens                      Greece
    25     2008         2042      Beijing                       China
```
#### Comment:
Great work! Next, you'll prepare a DataFrame of IOC codes.

## 02. Loading IOC codes DataFrame
Your task here is to prepare a DataFrame ioc_codes from a comma-separated values (CSV) file.

Initially, ioc_codes has 200 rows (one for each country) and 3 columns: 'Country', 'NOC', & 'ISO code'.

For the analysis that follows, you want to keep only the useful columns from ioc_codes: 'Country' and 'NOC' (the column 'NOC' contains three-letter codes representing each country).

### Instructions:
* Read file_path into a DataFrame called ioc_codes. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'.
* Select only the columns 'Country' and 'NOC' from ioc_codes.
* Print the leading 5 and trailing 5 rows of the DataFrame ioc_codes (there are 200 rows in total). This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Import pandas
import pandas as pd

# Create the file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())
```
#### Output:
```
<script.py> output:
               Country  NOC
    0      Afghanistan  AFG
    1          Albania  ALB
    2          Algeria  ALG
    3  American Samoa*  ASA
    4          Andorra  AND
                 Country  NOC
    196          Vietnam  VIE
    197  Virgin Islands*  ISV
    198            Yemen  YEM
    199           Zambia  ZAM
    200         Zimbabwe  ZIM
```
#### Comment:
Excellent work!

## 03. Building medals DataFrame
Here, you'll start with the DataFrame editions from the previous exercise.

You have a sequence of files summer_1896.csv, summer_1900.csv, ..., summer_2008.csv, one for each Olympic edition (year).

You will build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.

The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).

Once the dictionary of DataFrames is built up, you will combine the DataFrames using pd.concat().

### Instructions:
* Within the for loop:
** Create the file path. This has been done for you.
** Read file_path into a DataFrame. Assign the result to the year key of medals_dict.
** Select only the columns 'Athlete', 'NOC', and 'Medal' from medals_dict[year].
** Create a new column called 'Edition' in the DataFrame medals_dict[year] whose entries are all year.
* Concatenate the dictionary of DataFrames medals_dict into a DataFame called medals. Specify the keyword argument ignore_index=True to prevent repeated integer indices.
* Print the first and last 5 rows of medals. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Import pandas
import pandas as pd

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:

    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)
    
    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)
    
    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]
    
    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year
    
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict, ignore_index = True)

# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())
```

#### Output:
```

In [11]: editions
Out[11]: 
    Edition  Grand Total         City                     Country
0      1896          151       Athens                      Greece
1      1900          512        Paris                      France
2      1904          470    St. Louis               United States
3      1908          804       London              United Kingdom
4      1912          885    Stockholm                      Sweden
5      1920         1298      Antwerp                     Belgium
6      1924          884        Paris                      France
7      1928          710    Amsterdam                 Netherlands
8      1932          615  Los Angeles               United States
9      1936          875       Berlin                     Germany
10     1948          814       London              United Kingdom
11     1952          889     Helsinki                     Finland
12     1956          885    Melbourne                   Australia
13     1960          882         Rome                       Italy
14     1964         1010        Tokyo                       Japan
15     1968         1031  Mexico City                      Mexico
16     1972         1185       Munich  West Germany (now Germany)
17     1976         1305     Montreal                      Canada
18     1980         1387       Moscow       U.S.S.R. (now Russia)
19     1984         1459  Los Angeles               United States
20     1988         1546        Seoul                 South Korea
21     1992         1705    Barcelona                       Spain
22     1996         1859      Atlanta               United States
23     2000         2015       Sydney                   Australia
24     2004         1998       Athens                      Greece
25     2008         2042      Beijing                       China
```
```
In [21]: medals_dict[year].head()
Out[21]: 
      Sport Discipline           Athlete  NOC Gender         Event  \
0  Aquatics     Diving    GALPERIN, Gleb  RUS    Men  10m platform   
1  Aquatics     Diving  MITCHAM, Matthew  AUS    Men  10m platform   
2  Aquatics     Diving       ZHOU, Luxin  CHN    Men  10m platform   
3  Aquatics     Diving         WANG, Xin  CHN  Women  10m platform   
4  Aquatics     Diving      CHEN, Ruolin  CHN  Women  10m platform   

  Event_gender   Medal  
0            M  Bronze  
1            M    Gold  
2            M  Silver  
3            W  Bronze  
4            W    Gold
```
```
In [23]: medals_dict[year]
Out[23]: 
                    Athlete  NOC   Medal
0            GALPERIN, Gleb  RUS  Bronze
1          MITCHAM, Matthew  AUS    Gold
2               ZHOU, Luxin  CHN  Silver
3                 WANG, Xin  CHN  Bronze
4              CHEN, Ruolin  CHN    Gold
5           HEYMANS, Emilie  CAN  Silver
6                  QIN, Kai  CHN  Bronze
7                 HE, Chong  CHN    Gold
8       DESPATIE, Alexandre  CAN  Silver
9                WU, Minxia  CHN  Bronze
10            GUO, Jingjing  CHN    Gold
11         PAKHALINA, Julia  RUS  Silver
12       DOBROSKOK, Dmitriy  RUS  Bronze
13           GALPERIN, Gleb  RUS  Bronze
14               HUO, Liang  CHN    Gold
15                 LIN, Yue  CHN    Gold
16        HAUSDING, Patrick  GER  Silver
17            KLEIN, Sascha  GER  Silver
18          ESPINOSA, Paola  MEX  Bronze
19           ORTIZ, Tatiana  MEX  Bronze
20             CHEN, Ruolin  CHN    Gold
21                WANG, Xin  CHN    Gold
22             COLE, Briony  AUS  Silver
23              WU, Melissa  AUS  Silver
24            KVASHA, Illya  UKR  Bronze
25        PRYGOROV, Oleksiy  UKR  Bronze
26                 QIN, Kai  CHN    Gold
27               WANG, Feng  CHN    Gold
28           KUNAKOV, Yuriy  RUS  Silver
29           SAUTIN, Dmitry  RUS  Silver
...                     ...  ...     ...
2012       MUTALIMOV, Marid  KAZ  Bronze
2013        TAYMAZOV, Artur  UZB    Gold
2014    AKHMEDOV, Bakhtiyar  RUS  Silver
2015          AMOYAN, Roman  ARM  Bronze
2016         PARK, Eun-Chul  KOR  Bronze
2017         MANKIEV, Nazyr  RUS    Gold
2018      BAYRAMOV, Rovshan  AZE  Silver
2019  TENGIZBAYEV, Nurbakyt  KAZ  Bronze
2020     TIUMENBAEV, Ruslan  KGZ  Bronze
2021     ALBIEV, Islam-Beka  RUS    Gold
2022       RAHIMOV, Vitaliy  AZE  Silver
2023     SIAMIONAU, Mikhail  BLR  Bronze
2024       VARDANYAN, Armen  UKR  Bronze
2025         GUENOT, Steeve  FRA    Gold
2026     BEGALIEV, Kanatbek  KGZ  Silver
2027     GUENOT, Christophe  FRA  Bronze
2028        YANAKIEV, Yavor  BUL  Bronze
2029    KVIRKELIA, Manuchar  GEO    Gold
2030       CHANG, Yongxiang  CHN  Silver
2031          AVLUCA, Nazmi  TUR  Bronze
2032       MINGUZZI, Andrea  ITA    Gold
2033          FODOR, Zoltan  HUN  Silver
2034        MAMBETOV, Asset  KAZ  Bronze
2035          WHEELER, Adam  USA  Bronze
2036     KHUSHTOV, Aslanbek  RUS    Gold
2037         ENGLICH, Mirko  GER  Silver
2038   MIZGAITIS, Mindaugas  LTU  Bronze
2039        PATRIKEEV, Yuri  ARM  Bronze
2040          LOPEZ, Mijain  CUB    Gold
2041         BAROEV, Khasan  RUS  Silver

[2042 rows x 3 columns]
```
```
In [26]: medals_dict[year].head()
Out[26]: 
            Athlete  NOC   Medal  Edition
0    GALPERIN, Gleb  RUS  Bronze     2008
1  MITCHAM, Matthew  AUS    Gold     2008
2       ZHOU, Luxin  CHN  Silver     2008
3         WANG, Xin  CHN  Bronze     2008
4      CHEN, Ruolin  CHN    Gold     2008
```
#### Comment:
Fantastic! You're now ready to begin analyzing the medal data.

## 04. Counting medals by country/edition in a pivot table
Here, you'll start with the concatenated DataFrame medals from the previous exercise.

You can construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic edition on the Index and with 138 country NOC codes as columns. If you want a refresher on pivot tables, it may be useful to refer back to the relevant exercises in <a href="https://campus.datacamp.com/courses/manipulating-dataframes-with-pandas/rearranging-and-reshaping-data?ex=14">Manipulating DataFrames with pandas</a>.

### Instructions:
* Construct a pivot table from the DataFrame medals, aggregating by count (by specifying the aggfunc parameter). Use 'Edition' as the index, 'Athlete' for the values, and 'NOC' for the columns.
* Print the first & last 5 rows of medal_counts. This has been done for you, so hit 'Submit Answer' to see the results!

#### Script:
```
# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index = 'Edition', values = 'Athlete', columns = 'NOC', aggfunc = 'count')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print(medal_counts.tail())
```

#### Output:
```
<script.py> output:
    NOC      AFG  AHO  ALG   ANZ  ARG  ARM  AUS   AUT  AZE  BAH  ...   URS  URU  \
    Edition                                                      ...              
    1896     NaN  NaN  NaN   NaN  NaN  NaN  2.0   5.0  NaN  NaN  ...   NaN  NaN   
    1900     NaN  NaN  NaN   NaN  NaN  NaN  5.0   6.0  NaN  NaN  ...   NaN  NaN   
    1904     NaN  NaN  NaN   NaN  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN   
    1908     NaN  NaN  NaN  19.0  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN   
    1912     NaN  NaN  NaN  10.0  NaN  NaN  NaN  14.0  NaN  NaN  ...   NaN  NaN   
    
    NOC        USA  UZB  VEN  VIE  YUG  ZAM  ZIM   ZZX  
    Edition                                             
    1896      20.0  NaN  NaN  NaN  NaN  NaN  NaN   6.0  
    1900      55.0  NaN  NaN  NaN  NaN  NaN  NaN  34.0  
    1904     394.0  NaN  NaN  NaN  NaN  NaN  NaN   8.0  
    1908      63.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN  
    1912     101.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN  
    
    [5 rows x 138 columns]
    NOC      AFG  AHO  ALG  ANZ   ARG  ARM    AUS  AUT  AZE  BAH ...   URS  URU  \
    Edition                                                      ...              
    1992     NaN  NaN  2.0  NaN   2.0  NaN   57.0  6.0  NaN  1.0 ...   NaN  NaN   
    1996     NaN  NaN  3.0  NaN  20.0  2.0  132.0  3.0  1.0  5.0 ...   NaN  NaN   
    2000     NaN  NaN  5.0  NaN  20.0  1.0  183.0  4.0  3.0  6.0 ...   NaN  1.0   
    2004     NaN  NaN  NaN  NaN  47.0  NaN  157.0  8.0  5.0  2.0 ...   NaN  NaN   
    2008     1.0  NaN  2.0  NaN  51.0  6.0  149.0  3.0  7.0  5.0 ...   NaN  NaN   
    
    NOC        USA  UZB  VEN  VIE   YUG  ZAM  ZIM  ZZX  
    Edition                                             
    1992     224.0  NaN  NaN  NaN   NaN  NaN  NaN  NaN  
    1996     260.0  2.0  NaN  NaN  26.0  1.0  NaN  NaN  
    2000     248.0  4.0  NaN  1.0  26.0  NaN  NaN  NaN  
    2004     264.0  5.0  2.0  NaN   NaN  NaN  3.0  NaN  
    2008     315.0  6.0  1.0  1.0   NaN  NaN  4.0  NaN  
    
    [5 rows x 138 columns]
```
#### Comment:
Great work! As you can see, the pivot table DataFrame has mostly NaN entries (because most countries do not win any medals in a given Olympic edition).

## 05. Computing fraction of medals per Olympic edition
In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.

You can extract a Series with the total number of medals awarded in each Olympic edition.

The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method .divide() performs the broadcast as you require.

This gives you a normalized indication of each country's performance in each edition.

### Instructions
* Set the index of the DataFrame editions to be 'Edition' (using the method .set_index()). Save the result as totals.
* Extract the 'Grand Total' column from totals and assign the result back to totals.
* Divide the DataFrame medal_counts by totals along each row. You will have to use the .divide() method with the option axis='rows'. Assign the result to fractions.
* Print first & last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!

#### Script
```
# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
# fractions = medal_counts/totals
fractions = medal_counts.divide(totals, axis = 'rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())
```
#### Output:
```
<script.py> output:
    NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
    Edition                                                                    
    1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN   
    1900     NaN  NaN  NaN       NaN  NaN  NaN  0.009766  0.011719  NaN  NaN   
    1904     NaN  NaN  NaN       NaN  NaN  NaN       NaN  0.002128  NaN  NaN   
    1908     NaN  NaN  NaN  0.023632  NaN  NaN       NaN  0.001244  NaN  NaN   
    1912     NaN  NaN  NaN  0.011299  NaN  NaN       NaN  0.015819  NaN  NaN   
    
    NOC        ...     URS  URU       USA  UZB  VEN  VIE  YUG  ZAM  ZIM       ZZX  
    Edition    ...                                                                 
    1896       ...     NaN  NaN  0.132450  NaN  NaN  NaN  NaN  NaN  NaN  0.039735  
    1900       ...     NaN  NaN  0.107422  NaN  NaN  NaN  NaN  NaN  NaN  0.066406  
    1904       ...     NaN  NaN  0.838298  NaN  NaN  NaN  NaN  NaN  NaN  0.017021  
    1908       ...     NaN  NaN  0.078358  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
    1912       ...     NaN  NaN  0.114124  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
    
    [5 rows x 138 columns]
    NOC          AFG  AHO       ALG  ANZ       ARG       ARM       AUS       AUT  \
    Edition                                                                        
    1992         NaN  NaN  0.001173  NaN  0.001173       NaN  0.033431  0.003519   
    1996         NaN  NaN  0.001614  NaN  0.010758  0.001076  0.071006  0.001614   
    2000         NaN  NaN  0.002481  NaN  0.009926  0.000496  0.090819  0.001985   
    2004         NaN  NaN       NaN  NaN  0.023524       NaN  0.078579  0.004004   
    2008     0.00049  NaN  0.000979  NaN  0.024976  0.002938  0.072968  0.001469   
    
    NOC           AZE       BAH ...   URS       URU       USA       UZB       VEN  \
    Edition                     ...                                                 
    1992          NaN  0.000587 ...   NaN       NaN  0.131378       NaN       NaN   
    1996     0.000538  0.002690 ...   NaN       NaN  0.139860  0.001076       NaN   
    2000     0.001489  0.002978 ...   NaN  0.000496  0.123077  0.001985       NaN   
    2004     0.002503  0.001001 ...   NaN       NaN  0.132132  0.002503  0.001001   
    2008     0.003428  0.002449 ...   NaN       NaN  0.154261  0.002938  0.000490   
    
    NOC           VIE       YUG       ZAM       ZIM  ZZX  
    Edition                                               
    1992          NaN       NaN       NaN       NaN  NaN  
    1996          NaN  0.013986  0.000538       NaN  NaN  
    2000     0.000496  0.012903       NaN       NaN  NaN  
    2004          NaN       NaN       NaN  0.001502  NaN  
    2008     0.000490       NaN       NaN  0.001959  NaN  
    
    [5 rows x 138 columns]
```
#### Comment:
Well done!

## 06. Computing percentage change in fraction of medals won
Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.

To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.

The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the <a href="http://pandas.pydata.org/pandas-docs/stable/computation.html#expanding-windows">pandas documentation</a> has additional information.

### Instructions:
* Create mean_fractions by chaining the methods .expanding().mean() to fractions.
* Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100. Assign the result to fractions_change.
* Reset the index of fractions_change using the .reset_index() method. This will make 'Edition' an ordinary column.
* Print the first and last 5 rows of the DataFrame fractions_change. This has been done for you, so hit 'Submit Answer' to see the results!

#### Script:
```
# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change()*100

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print(fractions_change.tail())


# import pandas as pd
# asdf = pd.DataFrame({0:[1, 2, 3, 4], 1:[5, 6, 7, 8], 2: [9, 10, 11, 12]})

```

#### Output:
```
In [1]: editions.head()
Out[1]: 
   Edition  Grand Total       City         Country
0     1896          151     Athens          Greece
1     1900          512      Paris          France
2     1904          470  St. Louis   United States
3     1908          804     London  United Kingdom
4     1912          885  Stockholm          Sweden

In [2]: medals.head()
Out[2]: 
              Athlete  NOC   Medal  Edition
0       HAJOS, Alfred  HUN    Gold     1896
1    HERSCHMANN, Otto  AUT  Silver     1896
2   DRIVAS, Dimitrios  GRE  Bronze     1896
3  MALOKINIS, Ioannis  GRE    Gold     1896
4  CHASAPIS, Spiridon  GRE  Silver     1896

In [3]: medal_counts.head()
Out[3]: 
NOC      AFG  AHO  ALG   ANZ  ARG  ARM  AUS   AUT  AZE  BAH  ...   URS  URU  \
Edition                                                      ...              
1896     NaN  NaN  NaN   NaN  NaN  NaN  2.0   5.0  NaN  NaN  ...   NaN  NaN   
1900     NaN  NaN  NaN   NaN  NaN  NaN  5.0   6.0  NaN  NaN  ...   NaN  NaN   
1904     NaN  NaN  NaN   NaN  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN   
1908     NaN  NaN  NaN  19.0  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN   
1912     NaN  NaN  NaN  10.0  NaN  NaN  NaN  14.0  NaN  NaN  ...   NaN  NaN   

NOC        USA  UZB  VEN  VIE  YUG  ZAM  ZIM   ZZX  
Edition                                             
1896      20.0  NaN  NaN  NaN  NaN  NaN  NaN   6.0  
1900      55.0  NaN  NaN  NaN  NaN  NaN  NaN  34.0  
1904     394.0  NaN  NaN  NaN  NaN  NaN  NaN   8.0  
1908      63.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN  
1912     101.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN  

[5 rows x 138 columns]

In [4]: fractions.head()
Out[4]: 
NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
Edition                                                                    
1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN   
1900     NaN  NaN  NaN       NaN  NaN  NaN  0.009766  0.011719  NaN  NaN   
1904     NaN  NaN  NaN       NaN  NaN  NaN       NaN  0.002128  NaN  NaN   
1908     NaN  NaN  NaN  0.023632  NaN  NaN       NaN  0.001244  NaN  NaN   
1912     NaN  NaN  NaN  0.011299  NaN  NaN       NaN  0.015819  NaN  NaN   

NOC        ...     URS  URU       USA  UZB  VEN  VIE  YUG  ZAM  ZIM       ZZX  
Edition    ...                                                                 
1896       ...     NaN  NaN  0.132450  NaN  NaN  NaN  NaN  NaN  NaN  0.039735  
1900       ...     NaN  NaN  0.107422  NaN  NaN  NaN  NaN  NaN  NaN  0.066406  
1904       ...     NaN  NaN  0.838298  NaN  NaN  NaN  NaN  NaN  NaN  0.017021  
1908       ...     NaN  NaN  0.078358  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
1912       ...     NaN  NaN  0.114124  NaN  NaN  NaN  NaN  NaN  NaN       NaN  

[5 rows x 138 columns]

```
```
<script.py> output:
    NOC  Edition  AFG  AHO  ALG        ANZ  ARG  ARM        AUS        AUT  AZE  \
    0       1896  NaN  NaN  NaN        NaN  NaN  NaN        NaN        NaN  NaN   
    1       1900  NaN  NaN  NaN        NaN  NaN  NaN -13.134766 -32.304688  NaN   
    2       1904  NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -30.169386  NaN   
    3       1908  NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -23.013510  NaN   
    4       1912  NaN  NaN  NaN -26.092774  NaN  NaN   0.000000   6.254438  NaN   
    
    NOC    ...      URS  URU         USA  UZB  VEN  VIE  YUG  ZAM  ZIM        ZZX  
    0      ...      NaN  NaN         NaN  NaN  NaN  NaN  NaN  NaN  NaN        NaN  
    1      ...      NaN  NaN   -9.448242  NaN  NaN  NaN  NaN  NaN  NaN  33.561198  
    2      ...      NaN  NaN  199.651245  NaN  NaN  NaN  NaN  NaN  NaN -22.642384  
    3      ...      NaN  NaN  -19.549222  NaN  NaN  NaN  NaN  NaN  NaN   0.000000  
    4      ...      NaN  NaN  -12.105733  NaN  NaN  NaN  NaN  NaN  NaN   0.000000  
    
    [5 rows x 139 columns]
    NOC  Edition  AFG  AHO        ALG  ANZ       ARG        ARM        AUS  \
    21      1992  NaN  0.0  -7.214076  0.0 -6.767308        NaN   2.754114   
    22      1996  NaN  0.0   8.959211  0.0  1.306696        NaN  10.743275   
    23      2000  NaN  0.0  19.762488  0.0  0.515190 -26.935484  12.554986   
    24      2004  NaN  0.0   0.000000  0.0  9.625365   0.000000   8.161162   
    25      2008  NaN  0.0  -8.197807  0.0  8.588555  91.266408   6.086870   
    
    NOC       AUT        AZE ...   URS        URU       USA        UZB       VEN  \
    21  -3.034840        NaN ...   0.0   0.000000 -1.329330        NaN  0.000000   
    22  -3.876773        NaN ...   0.0   0.000000 -1.010378        NaN  0.000000   
    23  -3.464221  88.387097 ...   0.0 -12.025323 -1.341842  42.258065  0.000000   
    24  -2.186922  48.982144 ...   0.0   0.000000 -1.031922  21.170339 -1.615969   
    25  -3.389836  31.764436 ...   0.0   0.000000 -0.450031  14.610625 -6.987342   
    
    NOC       VIE       YUG        ZAM        ZIM  ZZX  
    21        NaN  0.000000   0.000000   0.000000  0.0  
    22        NaN -2.667732 -10.758472   0.000000  0.0  
    23        NaN -2.696445   0.000000   0.000000  0.0  
    24   0.000000  0.000000   0.000000 -43.491929  0.0  
    25  -0.661117  0.000000   0.000000 -23.316533  0.0  
    
    [5 rows x 139 columns]
```

#### Comment:
Great work!

## 07. Building hosts DataFrame
Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes. 
Once created, you will subset the Edition and NOC columns and set Edition as the Index.
There are some missing NOC values; you will set those explicitly.
Finally, you'll reset the Index & print the final DataFrame.

### Instructions:
* Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
* Clean up hosts by subsetting and setting the Index.
** Extract the columns 'Edition' and 'NOC'.
** Set 'Edition' column as the Index.
* Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for you.
* Reset the index of hosts using .reset_index(), which returns a new DataFrame.
* Hit 'Submit Answer' to see what hosts looks like!

#### Script:
```
# Import pandas
import pandas as pd

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions, ioc_codes, how = 'left')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition', 'NOC']].set_index('Edition')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)
```

#### Output:
```
In [3]: editions.head()
Out[3]: 
   Edition  Grand Total       City         Country
0     1896          151     Athens          Greece
1     1900          512      Paris          France
2     1904          470  St. Louis   United States
3     1908          804     London  United Kingdom
4     1912          885  Stockholm          Sweden

In [4]: ioc_codes.head()
Out[4]: 
           Country  NOC
0      Afghanistan  AFG
1          Albania  ALB
2          Algeria  ALG
3  American Samoa*  ASA
4          Andorra  AND

```
```
<script.py> output:
             NOC
    Edition     
    1972     NaN
    1980     NaN
    1988     NaN
        Edition  NOC
    0      1896  GRE
    1      1900  FRA
    2      1904  USA
    3      1908  GBR
    4      1912  SWE
    5      1920  BEL
    6      1924  FRA
    7      1928  NED
    8      1932  USA
    9      1936  GER
    10     1948  GBR
    11     1952  FIN
    12     1956  AUS
    13     1960  ITA
    14     1964  JPN
    15     1968  MEX
    16     1972  FRG
    17     1976  CAN
    18     1980  URS
    19     1984  USA
    20     1988  KOR
    21     1992  ESP
    22     1996  USA
    23     2000  AUS
    24     2004  GRE
    25     2008  CHN
```
#### Comment:
Good job! You now have a DataFrame consisting of all the hosts.
