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
