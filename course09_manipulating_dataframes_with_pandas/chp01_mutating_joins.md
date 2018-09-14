# Chapter 01: Mutating Joins

## 01. Index ordering
In this exercise, the DataFrame election is provided for you. It contains the 2012 US election results for the state of Pennsylvania with county names as row indices. Your job is to select 'Bedford' county and the'winner' column. Which method is the preferred way?

Feel free to explore the DataFrame in the IPython Shell.

### Possible Answers
election['Bedford', 'winner']
press 1
election['Bedford']['winner']
press 2
election['eggs']['Bedford']
press 3
election.loc['Bedford', 'winner']
press 4
election.iloc['Bedford', 'winner']
press 5

#### Script and Output
```
In [1]: election
Out[1]: 
               state   total      Obama     Romney  winner   voters
county                                                             
Adams             PA   41973  35.482334  63.112001  Romney    61156
Allegheny         PA  614671  56.640219  42.185820   Obama   924351
Armstrong         PA   28322  30.696985  67.901278  Romney    42147
Beaver            PA   80015  46.032619  52.637630  Romney   115157
Bedford           PA   21444  22.057452  76.986570  Romney    32189
Berks             PA  163253  48.939376  49.528646  Romney   250356
Blair             PA   47631  32.575424  66.133401  Romney    85328
Bradford          PA   22501  36.847251  61.450602  Romney    40490
Bucks             PA  319407  49.966970  48.801686   Obama   435606
Butler            PA   88924  31.920516  66.816607  Romney   122762
Cambria           PA   57718  40.162514  57.978447  Romney    86988
Cameron           PA    1967  34.417895  64.260295  Romney     3651
Carbon            PA   24232  45.559591  52.451304  Romney    39017
Centre            PA   68801  48.948416  48.977486  Romney   112949
Chester           PA  248295  49.228539  49.650617  Romney   337822
Clarion           PA   15227  31.069810  67.170158  Romney    24120
Clearfield        PA   31894  34.780837  63.657741  Romney    51174
Clinton           PA   12663  43.457317  54.813235  Romney    22969
Columbia          PA   24305  42.888295  55.317836  Romney    39888
Crawford          PA   33089  39.360513  58.922905  Romney    54711
Cumberland        PA  109964  39.997636  58.532793  Romney   158194
Dauphin           PA  122625  52.362080  46.351070   Obama   178924
Delaware          PA  272853  60.400655  38.581214   Obama   397338
Elk               PA   12425  41.400402  57.134809  Romney    20302
Erie              PA  112732  57.779512  40.895221   Obama   176851
Fayette           PA   48196  45.317039  53.624782  Romney    91681
Forest            PA    2308  38.734835  59.835355  Romney     3232
Franklin          PA   62802  30.110506  68.583803  Romney    87406
Fulton            PA    6148  21.096291  77.748861  Romney     9344
Greene            PA   13726  40.536209  58.174268  Romney    22663
...              ...     ...        ...        ...     ...      ...
Lebanon           PA   53771  35.288538  63.249707  Romney    81476
Lehigh            PA  144922  53.152040  45.604532   Obama   226453
Luzerne           PA  123741  51.699922  46.847043   Obama   194137
Lycoming          PA   46214  32.682737  65.975678  Romney    68064
McKean            PA   15014  35.033968  63.234315  Romney    25861
Mercer            PA   48065  48.022470  50.564860  Romney    75238
Mifflin           PA   16311  26.111213  72.913984  Romney    24445
Monroe            PA   59312  56.364648  42.318586   Obama   108879
Montgomery        PA  401787  56.637223  42.286834   Obama   551105
Montour           PA    7787  38.859638  59.535123  Romney    13518
Northampton       PA  125883  51.646370  47.061160   Obama   209414
Northumberland    PA   31512  39.324702  58.758568  Romney    54978
Perry             PA   18240  29.769737  68.591009  Romney    27245
Philadelphia      PA  653598  85.224251  14.051451   Obama  1099197
Pike              PA   23164  43.904334  54.882576  Romney    41840
Potter            PA    7205  26.259542  72.158223  Romney    10913
Schuylkill        PA   57505  42.523259  55.918616  Romney    86316
Snyder            PA   14962  31.225772  67.170164  Romney    21573
Somerset          PA   33875  27.808118  70.656827  Romney    51860
Sullivan          PA    2934  35.037491  63.360600  Romney     4242
Susquehanna       PA   17930  38.432794  59.871723  Romney    26163
Tioga             PA   15943  31.694160  66.480587  Romney    26001
Union             PA   16187  37.455983  60.931612  Romney    23950
Venango           PA   20775  35.951865  62.228640  Romney    32773
Warren            PA   16462  41.112866  57.192322  Romney    29111
Washington        PA   90078  42.744066  56.012567  Romney   142331
Wayne             PA   20966  38.815225  59.768196  Romney    32577
Westmoreland      PA  168709  37.567646  61.306154  Romney   238006
Wyoming           PA   11214  42.910647  55.189941  Romney    17255
York              PA  186394  38.695452  59.860296  Romney   280280

[67 rows x 6 columns]

In [2]: election.info()
<class 'pandas.core.frame.DataFrame'>
Index: 67 entries, Adams to York
Data columns (total 6 columns):
state     67 non-null object
total     67 non-null int64
Obama     67 non-null float64
Romney    67 non-null float64
winner    67 non-null object
voters    67 non-null int64
dtypes: float64(2), int64(2), object(2)
memory usage: 6.2+ KB
```
##### Answer:
4

##### Comment:
Well done!

## 02. Positional and labeled indexing
Given a pair of label-based indices, sometimes it's necessary to find the corresponding positions. In this exercise, you will use the Pennsylvania election results again. The DataFrame is provided for you as election.

Find x and y such that election.iloc[x, y] == election.loc['Bedford', 'winner']. That is, what is the row position of 'Bedford', and the column position of 'winner'? Remember that the first position in Python is 0, not 1!

To answer this question, first explore the DataFrame using election.head() in the IPython Shell and inspect it with your eyes.

### Instructions:
* Explore the DataFrame in the IPython Shell using election.head().
* Assign the row position of election.loc['Bedford'] to x.
* Assign the column position of election['winner'] to y.
* Hit 'Submit Answer' to print the boolean equivalence of the .loc and .iloc selections.

#### Script
```
# Assign the row position of election.loc['Bedford']: x
x = 4

# Assign the column position of election['winner']: y
y = 4

# Print the boolean equivalence
print(election.iloc[x, y] == election.loc['Bedford', 'winner'])
```

##### Output:
```
In [1]: election.head()
Out[1]: 
          state   total      Obama     Romney  winner  voters
county                                                       
Adams        PA   41973  35.482334  63.112001  Romney   61156
Allegheny    PA  614671  56.640219  42.185820   Obama  924351
Armstrong    PA   28322  30.696985  67.901278  Romney   42147
Beaver       PA   80015  46.032619  52.637630  Romney  115157
Bedford      PA   21444  22.057452  76.986570  Romney   32189

<script.py> output:
    True
```
##### Comment:
Great work! Depending on the situation, you may wish to use .iloc[] over .loc[], and vice versa. The important thing to realize is you can achieve the exact same results using either approach.

## 03. Indexing and column rearrangement
There are circumstances in which it's useful to modify the order of your DataFrame columns. We do that now by extracting just two columns from the Pennsylvania election results DataFrame.

Your job is to read the CSV file and set the index to 'county'. You'll then assign a new DataFrame by selecting the list of columns ['winner', 'total', 'voters']. The CSV file is provided to you in the variable filename.

### Instructions
* Import pandas as pd.
* Read in filename using pd.read_csv() and set the index to 'county' by specifying the index_col parameter.
* Create a separate DataFrame results with the columns ['winner', 'total', 'voters'].
* Print the output using results.head(). This has been done for you, so hit 'Submit Answer' to see the new DataFrame!

#### Script
```
# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())

```
##### Output:
```
# Import pandas
import pandas as pd

# Read in filename and set the index: election
election = pd.read_csv(filename, index_col='county')

# Create a separate dataframe with the columns ['winner', 'total', 'voters']: results
results = election[['winner', 'total', 'voters']]

# Print the output of results.head()
print(results.head())

```
##### Comment:
Wonderful work! The original election DataFrame had 6 columns, but as you can see, your results DataFrame now has just the 3 columns: 'winner', 'total', and 'voters'.

## 04. Slicing rows
The Pennsylvania US election results data set that you have been using so far is ordered by county name. This means that county names can be sliced alphabetically. In this exercise, you're going to perform slicing on the county names of the election DataFrame from the previous exercises, which has been pre-loaded for you.

### Instructions
* Slice the row labels 'Perry' to 'Potter' and assign the output to p_counties.
* Print the p_counties DataFrame. This has been done for you.
* Slice the row labels 'Potter' to 'Perry' in reverse order. To do this for hypothetical row labels 'a' and 'b', you could use a stepsize of -1 like so: df.loc['b':'a':-1].
* Print the p_counties_rev DataFrame. This has also been done for you, so hit 'Submit Answer' to see the result of your slicing!

#### Script:
```
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter']

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry':-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

```
##### Output:
```
<script.py> output:
                 state   total      Obama     Romney  winner   voters
    county                                                           
    Perry           PA   18240  29.769737  68.591009  Romney    27245
    Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
    Pike            PA   23164  43.904334  54.882576  Romney    41840
    Potter          PA    7205  26.259542  72.158223  Romney    10913
                 state   total      Obama     Romney  winner   voters
    county                                                           
    Potter          PA    7205  26.259542  72.158223  Romney    10913
    Pike            PA   23164  43.904334  54.882576  Romney    41840
    Philadelphia    PA  653598  85.224251  14.051451   Obama  1099197
    Perry           PA   18240  29.769737  68.591009  Romney    27245

```
##### Comment:
Well done! It looks like Obama did particularly well in Philadelphia.

## 05. Subselecting DataFrames with lists
You can use lists to select specific row and column labels with the .loc[] accessor. In this exercise, your job is to select the counties ['Philadelphia', 'Centre', 'Fulton'] and the columns ['winner','Obama','Romney'] from the election DataFrame, which has been pre-loaded for you with the index set to 'county'.

### Instruction
* Create the list of row labels ['Philadelphia', 'Centre', 'Fulton'] and assign it to rows.
* Create the list of column labels ['winner', 'Obama', 'Romney'] and assign it to cols.
* Create a new DataFrame by selecting with rows and cols in .loc[] and assign it to three_counties.
* Print the three_counties DataFrame. This has been done for you, so hit 'Submit Answer' to see your new DataFrame.

#### Script:
```
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner', 'Obama', 'Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows, cols]

# Print the three_counties DataFrame
print(three_counties)
```
##### Output:
```
<script.py> output:
                  winner      Obama     Romney
    county                                    
    Philadelphia   Obama  85.224251  14.051451
    Centre        Romney  48.948416  48.977486
    Fulton        Romney  21.096291  77.748861
```
##### Comment:
Excellent work! If you know exactly which rows and columns are of interest to you, this is a useful approach for subselecting DataFrames.

## 06. Thresholding data
In this exercise, we have provided the Pennsylvania election results and included a column called 'turnout' that contains the percentage of voter turnout per county. Your job is to prepare a boolean array to select all of the rows and columns where voter turnout exceeded 70%.

As before, the DataFrame is available to you as election with the index set to 'county'.

### Instructions
* Create a boolean array of the condition where the 'turnout' column is greater than 70 and assign it to high_turnout.
* Filter the election DataFrame with the high_turnout array and assign it to high_turnout_df.
* Print the filtered DataFrame. This has been done for you, so hit 'Submit Answer' to see it!

#### Script
```
# Create the boolean array: high_turnout
high_turnout = election.turnout > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)
```
##### Output:
```
<script.py> output:
                 state   total      Obama     Romney  winner  voters    turnout     margin
    county                                                                                
    Bucks           PA  319407  49.966970  48.801686   Obama  435606  73.324748   1.165284
    Butler          PA   88924  31.920516  66.816607  Romney  122762  72.436096  34.896091
    Chester         PA  248295  49.228539  49.650617  Romney  337822  73.498766   0.422079
    Forest          PA    2308  38.734835  59.835355  Romney    3232  71.410891  21.100520
    Franklin        PA   62802  30.110506  68.583803  Romney   87406  71.850903  38.473297
    Montgomery      PA  401787  56.637223  42.286834   Obama  551105  72.905708  14.350390
    Westmoreland    PA  168709  37.567646  61.306154  Romney  238006  70.884347  23.738508
```
##### COmment:
Well done!

## 07. Filtering columns using other columns
The election results DataFrame has a column labeled 'margin' which expresses the number of extra votes the winner received over the losing candidate. This number is given as a percentage of the total votes cast. It is reasonable to assume that in counties where this margin was less than 1%, the results would be too-close-to-call.

Your job is to use boolean selection to filter the rows where the margin was less than 1. You'll then convert these rows of the 'winner' column to np.nan to indicate that these results are too close to declare a winner.

The DataFrame has been pre-loaded for you as election.

### Insturctions:
* Import numpy as np.
* Create a boolean array for the condition where the 'margin' column is less than 1 and assign it to too_close.
* Convert the entries in the 'winner' column where the result was too close to call to np.nan.
* Print the output of election.info(). This has been done for you, so hit 'Submit Answer' to see the results.

#### Script
```
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = (election.margin < 1)

# Assign np.nan to the 'winner' column where the results were too close to call
election.winner[too_close] = np.nan

# Print the output of election.info()
print(election.info())

```
##### Output:
```
<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    Index: 67 entries, Adams to York
    Data columns (total 8 columns):
    state      67 non-null object
    total      67 non-null int64
    Obama      67 non-null float64
    Romney     67 non-null float64
    winner     64 non-null object
    voters     67 non-null int64
    turnout    67 non-null float64
    margin     67 non-null float64
    dtypes: float64(4), int64(2), object(2)
    memory usage: 4.7+ KB
    None
```
##### COmment:
Fantastic work!

## 08. Filtering using NaNs
In certain scenarios, it may be necessary to remove rows and columns with missing data from a DataFrame. The .dropna() method is used to perform this action. You'll now practice using this method on a dataset obtained from Vanderbilt University, which consists of data from passengers on the Titanic.

The DataFrame has been pre-loaded for you as titanic. Explore it in the IPython Shell and you will note that there are many NaNs. You will focus specifically on the 'age' and 'cabin' columns in this exercise. Your job is to use .dropna() to remove rows where any of these two columns contains missing data and rows where all of these two columns contain missing data.

You'll also use the .shape attribute, which returns the number of rows and columns in a tuple from a DataFrame, or the number of rows from a Series, to see the effect of dropping missing values from a DataFrame.

Finally, you'll use the thresh= keyword argument to drop columns from the full dataset that have less than 1000 non-missing values.

### Instructions:
* Select the 'age' and 'cabin' columns of titanic and create a new DataFrame df.
* Print the shape of df. This has been done for you.
* Drop rows in df with how='any' and print the shape.
* Drop rows in df with how='all' and print the shape.
* Drop columns from the titanic DataFrame that have less than 1000 non-missing values by specifying the thresh and axis keyword arguments. Print the output of .info() from this.

#### Script:
```
# Select the 'age' and 'cabin' columns: df
df = titanic[['age', 'cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())
```
##### Output:
```
<script.py> output:
    (1309, 2)
    (272, 2)
    (1069, 2)
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1309 entries, 0 to 1308
    Data columns (total 10 columns):
    pclass      1309 non-null int64
    survived    1309 non-null int64
    name        1309 non-null object
    sex         1309 non-null object
    age         1046 non-null float64
    sibsp       1309 non-null int64
    parch       1309 non-null int64
    ticket      1309 non-null object
    fare        1308 non-null float64
    embarked    1307 non-null object
    dtypes: float64(2), int64(4), object(4)
    memory usage: 102.3+ KB
    None
```
##### Comment:
Wonderful work! Usually you would want to avoid dropping too much of your data, but in some situations, it may be necessary.
