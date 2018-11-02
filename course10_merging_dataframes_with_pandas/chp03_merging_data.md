# Chapter 03: Merging Data

## 01. Merging company DataFrames
Suppose your company has operations in several different cities under several different managers. The DataFrames revenue and managers contain partial information related to the company. That is, the rows of the city columns don't quite match in revenue and managers (the Mendocino branch has no revenue yet since it just opened and the manager of Springfield branch recently left the company).

The DataFrames have been printed in the IPython Shell. If you were to run the command combined = pd.merge(revenue, managers, on='city'), how many rows would combined have?

### Possible Answers
* 0 rows. <br />
press 1
* 2 rows. <br />
press 2
* 3 rows. <br />
press 3
* 4 rows. <br />
press 4

#### Data
```
         city  revenue
0       Austin      100
1       Denver       83
2  Springfield        4

        city   manager
0     Austin  Charlers
1     Denver      Joel
2  Mendocino     Brett
```
#### Answer:
2

#### Comment:
Correct! Since the default strategy for pd.merge() is an inner join, combined will have 2 rows.

## 02. Merging on a specific column
This exercise follows on the last one with the DataFrames revenue and managers for your company. You expect your company to grow and, eventually, to operate in cities with the same name on different states. As such, you decide that every branch should have a numerical branch identifier. Thus, you add a branch_id column to both DataFrames. Moreover, new cities have been added to both the revenue and managers DataFrames as well. pandas has been imported as pd and both DataFrames are available in your namespace.

At present, there should be a 1-to-1 relationship between the city and branch_id fields. In that case, the result of a merge on the city columns ought to give you the same output as a merge on the branch_id columns. Do they? Can you spot an ambiguity in one of the DataFrames?

### Instructions:
* Using pd.merge(), merge the DataFrames revenue and managers on the 'city' column of each. Store the result as merge_by_city.
* Print the DataFrame merge_by_city. This has been done for you.
* Merge the DataFrames revenue and managers on the 'branch_id' column of each. Store the result as merge_by_id.
* Print the DataFrame merge_by_id. This has been done for you, so hit 'Submit Answer' to see the result!

#### Script:
```
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on = 'city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on = 'branch_id')

# Print merge_by_id
print(merge_by_id)
```

#### Output:
```
In [1]: revenue
Out[1]: 
   branch_id         city  revenue
0         10       Austin      100
1         20       Denver       83
2         30  Springfield        4
3         47    Mendocino      200

In [2]: managers
Out[2]: 
   branch_id         city  manager
0         10       Austin  Charles
1         20       Denver     Joel
2         47    Mendocino    Brett
3         31  Springfield    Sally
```
```
<script.py> output:
       branch_id_x         city  revenue  branch_id_y  manager
    0           10       Austin      100           10  Charles
    1           20       Denver       83           20     Joel
    2           30  Springfield        4           31    Sally
    3           47    Mendocino      200           47    Brett
       branch_id     city_x  revenue     city_y  manager
    0         10     Austin      100     Austin  Charles
    1         20     Denver       83     Denver     Joel
    2         47  Mendocino      200  Mendocino    Brett
```

#### Comment:
```
Well done! Notice that when you merge on 'city', the resulting DataFrame has a peculiar result: In row 2, the city Springfield has two different branch IDs. This is because there are actually two different cities named Springfield - one in the State of Illinois, and the other in Missouri. The revenue DataFrame has the one from Illinois, and the managers DataFrame has the one from Missouri. Consequently, when you merge on 'branch_id', both of these get dropped from the merged DataFrame.
```

## 03. Merging on columns with non-matching labels
You continue working with the revenue & managers DataFrames from before. This time, someone has changed the field name 'city' to 'branch' in the managers table. Now, when you attempt to merge DataFrames, an exception is thrown:
```
>>> pd.merge(revenue, managers, on='city')
Traceback (most recent call last):
    ... <text deleted> ...
    pd.merge(revenue, managers, on='city')
    ... <text deleted> ...
KeyError: 'city'
```
Given this, it will take a bit more work for you to join or merge on the city/branch name. You have to specify the left_on and right_on parameters in the call to pd.merge().

As before, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace. They have been printed in the IPython Shell so you can examine the columns prior to merging.

Are you able to merge better than in the last exercise? How should the rows with Springfield be handled?

### Instructions:
* Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.
** In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
* Print the new DataFrame combined.

#### Script:
```
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, left_on='city', right_on='branch')

# Print combined
print(combined)
```
#### Output:
```
<script.py> output:
       branch_id_x         city  revenue state_x       branch  branch_id_y  \
    0           10       Austin      100      TX       Austin           10   
    1           20       Denver       83      CO       Denver           20   
    2           30  Springfield        4      IL  Springfield           31   
    3           47    Mendocino      200      CA    Mendocino           47   
    
        manager state_y  
    0  Charlers      TX  
    1      Joel      CO  
    2     Sally      MO  
    3     Brett      CA
```
#### Comment:
Great work! It is important to pay attention to how columns are named in different DataFrames.

## 04. Merging on multiple columns
Another strategy to disambiguate cities with identical names is to add information on the states in which the cities are located. To this end, you add a column called state to both DataFrames from the preceding exercises. Again, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace.

Your goal in this exercise is to use pd.merge() to merge DataFrames using multiple columns (using 'branch_id', 'city', and 'state' in this case).

Are you able to match all your company's branches correctly?

### Instructions:
* Create a column called 'state' in the DataFrame revenue, consisting of the list ['TX','CO','IL','CA'].
* Create a column called 'state' in the DataFrame managers, consisting of the list ['TX','CO','CA','MO'].
* Merge the DataFrames revenue and managers using three columns :'branch_id', 'city', and 'state'. Pass them in as a list to the on paramater of pd.merge().

#### Script:
```
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers, on = ['branch_id', 'city', 'state'])

# Print combined
print(combined)
```
#### Output:
```
In [2]: revenue
Out[2]: 
   branch_id         city  revenue state
0         10       Austin      100    TX
1         20       Denver       83    CO
2         30  Springfield        4    IL
3         47    Mendocino      200    CA

In [3]: managers
Out[3]: 
   branch_id         city   manager state
0         10       Austin  Charlers    TX
1         20       Denver      Joel    CO
2         47    Mendocino     Brett    CA
3         31  Springfield     Sally    MO

<script.py> output:
       branch_id       city  revenue state   manager
    0         10     Austin      100    TX  Charlers
    1         20     Denver       83    CO      Joel
    2         47  Mendocino      200    CA     Brett
```
#### Comment:
Excellent work! You've matched all the branches correctly!

## 05. Joining by Index
The DataFrames revenue and managers are displayed in the IPython Shell. Here, they are indexed by 'branch_id'.

Choose the function call below that will join the DataFrames on their indexes and return 5 rows with index labels [10, 20, 30, 31, 47]. Explore each of them in the IPython Shell to get a better understanding of their functionality.

### Possible Answers
* pd.merge(revenue, managers, on='branch_id').
press 1
* pd.merge(managers, revenue, how='left').
press 2
* revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer').
press 3
* managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left').
press 4

#### Script & Output:
```
                 city  revenue state
branch_id                            
10              Austin      100    TX
20              Denver       83    CO
30         Springfield        4    IL
47           Mendocino      200    CA

                branch   manager state
branch_id                             
10              Austin  Charlers    TX
20              Denver      Joel    CO
47           Mendocino     Brett    CA
31         Springfield     Sally    MO

In [1]: revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer')
Out[1]: 
                  city  revenue state_rev       branch   manager state_mng
branch_id                                                                 
10              Austin    100.0        TX       Austin  Charlers        TX
20              Denver     83.0        CO       Denver      Joel        CO
30         Springfield      4.0        IL          NaN       NaN       NaN
31                 NaN      NaN       NaN  Springfield     Sally        MO
47           Mendocino    200.0        CA    Mendocino     Brett        CA
```
#### Answer:
3

#### Comment:
Correct! This function call does indeed return 5 rows with index labels [10, 20, 30, 31, 47]

## 06. Choosing a joining strategy
Suppose you have two DataFrames: students (with columns 'StudentID', 'LastName', 'FirstName', and 'Major') and midterm_results (with columns 'StudentID', 'Q1', 'Q2', and 'Q3' for their scores on midterm questions).

You want to combine the DataFrames into a single DataFrame grades, and be able to easily spot which students wrote the midterm and which didn't (their midterm question scores 'Q1', 'Q2', & 'Q3' should be filled with NaN values).

You also want to drop rows from midterm_results in which the StudentID is not found in students.

Which of the following strategies gives the desired result?

### Possible Answers
* A left join: grades = pd.merge(students, midterm_results, how='left').
press 1
* A right join: grades = pd.merge(students, midterm_results, how='right').
press 2
* An inner join: grades = pd.merge(students, midterm_results, how='inner').
press 3
* An outer join: grades = pd.merge(students, midterm_results, how='outer').
press 4

#### Answer:
1

#### Comment:
Correct! A left join is indeed the right strategy here.
