## 01. Connecting to a PostgreSQL Database
In these exercises, you will be working with real databases hosted on the cloud via Amazon Web Services (AWS)!

Let's begin by connecting to a PostgreSQL database. When connecting to a PostgreSQL database, many prefer to use the psycopg2 database driver as it supports practically all of PostgreSQL's features efficiently and is the standard dialect for PostgreSQL in SQLAlchemy.

You might recall from Chapter 1 that we use the create_engine() function and a connection string to connect to a database.

There are three components to the connection string in this exercise: the dialect and driver (`'postgresql+psycopg2://'`), followed by the username and password ('student:datacamp'), followed by the host and port (`'@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/'`), and finally, the database name ('census'). You will have to pass this string as an argument to create_engine() in order to connect to the database.

### Instructions:
* Import create_engine from sqlalchemy.
* Create an engine to the census database by concatenating the following strings:
** 'postgresql+psycopg2://'
** 'student:datacamp'
** '@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com'
** ':5432/census'
* Use the .table_names() method on engine to print the table names.

#### Script:
```
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())
```
#### Output:
```
<script.py> output:
    ['census', 'state_fact', 'data', 'users']
```
#### Comment:
Great work! Notice that this census database contains 4 tables: 'census', 'state_fact', 'data', and 'users'.

## 02. Filter data selected from a Table - Simple
Having connected to the database, it's now time to practice filtering your queries!

As mentioned in the video, a where() clause is used to filter the data that a statement returns. For example, to select all the records from the census table where the sex is Female (or 'F') we would do the following:

select([census]).where(census.columns.sex == 'F')

In addition to == we can use basically any python comparison operator (such as <=, !=, etc) in the where() clause.

### Instructions:
* Select all records from the census table by passing in census as a list to select().
* Append a where clause to stmt to return only the records with a state of 'New York'.
* Execute the statement stmt using .execute() and retrieve the results using .fetchall().
* Iterate over results and print the age, sex and pop2008 columns from each record. For example, you can print out the age of result with result.age.

#### Script:
```
# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == 'New York')

# Execute the query to retrieve all the data returned: results
results = connection.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)

```
#### Output:
```

<script.py> output:
    0 M 128088
    1 M 125649
    2 M 121615
    3 M 120580
    4 M 122482
    5 M 121205
    6 M 120089
    7 M 122355
    8 M 118653
    9 M 117369
    10 M 118810
    11 M 121121
    12 M 126338
    13 M 128713
    14 M 129812
    15 M 134463
    16 M 136569
    17 M 140114
    18 M 156892
    19 M 147556
    20 M 146611
    21 M 141932
    22 M 138557
    23 M 136150
    24 M 132383
    25 M 141850
    26 M 129603
    27 M 131419
    28 M 127224
    29 M 122449
    30 M 126404
    31 M 126124
    32 M 123362
    33 M 126486
    34 M 120030
    35 M 123017
    36 M 127076
    37 M 136270
    38 M 144715
    39 M 135027
    40 M 135355
    41 M 132905
    42 M 140025
    43 M 151555
    44 M 149030
    45 M 148147
    46 M 146692
    47 M 147648
    48 M 155155
    49 M 144287
    50 M 143466
    51 M 139630
    52 M 133939
    53 M 136723
    54 M 125953
    55 M 122478
    56 M 118070
    57 M 115823
    58 M 117177
    59 M 108293
    60 M 106825
    61 M 113681
    62 M 83763
    63 M 81226
    64 M 76961
    65 M 82242
    66 M 70423
    67 M 64117
    68 M 63657
    69 M 58801
    70 M 57609
    71 M 53231
    72 M 51132
    73 M 50696
    74 M 44822
    75 M 43592
    76 M 41900
    77 M 40417
    78 M 40241
    79 M 35941
    80 M 34659
    81 M 32022
    82 M 28890
    83 M 27217
    84 M 23879
    85 M 124478
    0 F 122194
    1 F 119661
    2 F 116413
    3 F 114877
    4 F 116936
    5 F 116051
    6 F 115186
    7 F 116951
    8 F 113279
    9 F 111919
    10 F 113891
    11 F 115607
    12 F 120156
    13 F 123797
    14 F 124343
    15 F 127635
    16 F 130769
    17 F 134311
    18 F 150772
    19 F 142871
    20 F 141831
    21 F 142302
    22 F 138703
    23 F 138084
    24 F 135339
    25 F 141601
    26 F 130002
    27 F 129600
    28 F 129868
    29 F 119821
    30 F 125047
    31 F 127486
    32 F 123742
    33 F 126908
    34 F 121824
    35 F 124485
    36 F 130377
    37 F 140890
    38 F 148408
    39 F 137936
    40 F 138561
    41 F 139720
    42 F 145307
    43 F 154437
    44 F 154805
    45 F 153651
    46 F 151107
    47 F 154997
    48 F 158855
    49 F 151022
    50 F 149883
    51 F 146988
    52 F 142566
    53 F 144121
    54 F 135180
    55 F 132338
    56 F 127500
    57 F 126450
    58 F 128713
    59 F 121743
    60 F 119540
    61 F 126847
    62 F 96462
    63 F 94667
    64 F 90185
    65 F 97321
    66 F 83336
    67 F 77404
    68 F 77802
    69 F 71850
    70 F 71451
    71 F 66625
    72 F 65037
    73 F 65719
    74 F 58818
    75 F 58722
    76 F 57584
    77 F 56907
    78 F 58456
    79 F 54136
    80 F 52932
    81 F 50693
    82 F 48206
    83 F 47777
    84 F 43454
    85 F 273476

In [1]: 
```
#### Comment:
Well done! Do you notice any interesting results? What was the most common age among males and females in New York in 2008?

## 03. Filter data selected from a Table - Expressions
In addition to standard Python comparators, we can also use methods such as in_() to create more powerful where() clauses. You can see a full list of expressions in the <a href="https://docs.sqlalchemy.org/en/latest/core/sqlelement.html#module-sqlalchemy.sql.expression">SQLAlchemy Documentation</a>.

We've already created a list of some of the most densely populated states.

### Instructions:
* Select all records from the census table by passing it in as a list to select().
* Append a where clause to return all the records with a state in the states list. Use in_(states) on census.columns.state to do this.
* Loop over the ResultProxy connection.execute(stmt) and print the state and pop2000 columns from each record.

#### Script
```
# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where((census.columns.state).in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for s in connection.execute(stmt):
    print(s['state'], s['pop2000'])
```

#### Output:
```
In [3]: states
Out[3]: ['New York', 'California', 'Texas'] 
```
```
In [9]: census.columns.keys()
Out[9]: ['state', 'sex', 'age', 'pop2000', 'pop2008']
```
```

<script.py> output:
    New York 126237
    New York 124008
    New York 124725
    New York 126697
    New York 131357
    New York 133095
    New York 134203
    New York 137986
    New York 139455
    New York 142454
    New York 145621
    New York 138746
    New York 135565
    New York 132288
    New York 132388
    New York 131959
    New York 130189
    New York 132566
    New York 132672
    New York 133654
    New York 132121
    New York 126166
    New York 123215
    New York 121282
    New York 118953
    New York 123151
    New York 118727
    New York 122359
    New York 128651
    New York 140687
    New York 149558
    New York 139477
    New York 138911
    New York 139031
    New York 145440
    New York 156168
    New York 153840
    New York 152078
    New York 150765
    New York 152606
    New York 159345
    New York 148628
    New York 147892
    New York 144195
    New York 139354
    New York 141953
    New York 131875
    New York 128767
    New York 125406
    New York 124155
    New York 125955
    New York 118542
    New York 118532
    New York 124418
    New York 95025
    New York 92652
    New York 90096
    New York 95340
    New York 83273
    New York 77213
    New York 77054
    New York 72212
    New York 70967
    New York 66461
    New York 64361
    New York 64385
    New York 58819
    New York 58176
    New York 57310
    New York 57057
    New York 57761
    New York 53775
    New York 53568
    New York 51263
    New York 48440
    New York 46702
    New York 43508
    New York 40730
    New York 37950
    New York 35774
    New York 32453
    New York 26803
    California 252494
    California 247978
    California 250644
    California 257443
    California 266855
    California 272801
    California 274899
    California 277580
    California 283553
    California 285478
    California 284518
    California 269009
    California 262671
    California 254889
    California 253023
    California 251962
    California 249220
    California 255482
    California 252607
    California 248356
    California 250156
    California 238235
    California 235718
    California 239698
    California 240655
    California 250964
    California 245324
    California 251413
    California 260869
    California 276142
    California 293816
    California 273159
    California 268484
    California 263472
    California 269607
    California 286895
    California 284414
    California 280861
    California 281214
    California 278802
    California 290332
    California 267684
    California 268045
    California 261885
    California 252175
    California 255340
    California 239126
    California 229057
    California 219293
    California 214700
    California 219017
    California 203068
    California 200466
    California 207237
    California 160674
    California 158483
    California 150235
    California 150046
    California 133017
    California 124106
    California 121984
    California 114331
    California 110491
    California 102859
    California 99345
    California 100052
    California 91053
    California 89634
    California 88258
    California 87840
    California 88575
    California 80843
    California 79376
    California 76365
    California 73697
    California 72885
    California 69738
    California 65865
    California 62867
    California 58012
    California 51806
    California 43254
    California 40083
    California 34144
    California 30384
    California 136442
    California 239605
    California 236543
    California 240010
    California 245739
    California 254522
    California 260264
    California 261296
    California 264083
    California 270447
    California 271482
    California 270567
    California 256656
    California 249887
    California 242724
    California 240752
    California 240170
    California 233186
    California 235767
    California 234949
    California 233477
    California 233532
    California 223990
    California 222035
    California 227742
    California 228401
    California 238602
    California 233133
    California 240008
    California 249185
    California 266010
    California 278894
    California 260916
    California 256168
    California 252784
    California 256283
    California 276234
    California 277592
    California 276277
    California 275129
    California 276094
    California 283554
    California 265614
    California 265895
    California 263355
    California 255016
    California 256779
    California 244172
    California 236211
    California 226391
    California 221928
    California 225414
    California 212545
    California 208500
    California 215228
    California 168388
    California 166675
    California 158368
    California 160423
    California 142287
    California 133235
    California 132033
    California 123328
    California 120982
    California 114959
    California 111942
    California 113547
    California 104910
    California 103883
    California 102061
    California 103181
    California 106514
    California 99453
    California 100574
    California 99772
    California 99390
    California 99277
    California 95046
    California 90193
    California 86911
    California 81990
    California 75849
    California 65410
    California 61518
    California 54748
    California 50746
    California 294583
    New York 25041
    New York 21687
    New York 18873
    New York 88366
    New York 120355
    New York 118219
    New York 119577
    New York 121029
    New York 125247
    New York 128227
    New York 128428
    New York 131161
    New York 133646
    New York 135746
    New York 138287
    New York 131904
    New York 129028
    New York 126571
    New York 125682
    New York 125409
    New York 122770
    New York 123978
    New York 125307
    New York 127956
    New York 129184
    New York 124575
    New York 123701
    New York 124108
    New York 122624
    New York 127474
    New York 123033
    New York 128125
    New York 134795
    New York 146832
    New York 152973
    New York 144001
    New York 143930
    New York 144653
    New York 151147
    New York 159228
    New York 159999
    New York 157911
    New York 156103
    New York 159284
    New York 163331
    New York 155353
    New York 153688
    New York 151615
    New York 146774
    New York 148318
    New York 139802
    New York 138062
    New York 134107
    New York 134399
    New York 136630
    New York 130843
    New York 130196
    New York 136064
    New York 106579
    New York 104847
    New York 101857
    New York 108406
    New York 94346
    New York 88584
    New York 88932
    New York 82899
    New York 82172
    New York 77171
    New York 76032
    New York 76498
    New York 70465
    New York 71088
    New York 70847
    New York 71377
    New York 74378
    New York 70611
    New York 70513
    New York 69156
    New York 68042
    New York 68410
    New York 64971
    New York 61287
    New York 58911
    New York 56865
    New York 54553
    New York 46381
    New York 45599
    New York 40525
    New York 37436
    New York 226378
    Texas 172223
    Texas 165635
    Texas 165337
    Texas 164292
    Texas 165785
    Texas 166278
    Texas 167170
    Texas 169210
    Texas 171199
    Texas 170521
    Texas 173734
    Texas 167859
    Texas 166474
    Texas 166014
    Texas 166081
    Texas 167257
    Texas 165881
    Texas 171567
    Texas 170011
    Texas 164671
    Texas 163295
    Texas 153946
    Texas 150839
    Texas 152673
    Texas 153769
    Texas 156739
    Texas 153181
    Texas 155480
    Texas 161048
    Texas 165852
    Texas 167982
    Texas 158505
    Texas 153855
    Texas 151149
    Texas 155095
    Texas 164514
    Texas 167136
    Texas 168668
    Texas 167261
    Texas 169195
    Texas 173212
    Texas 164647
    Texas 163690
    Texas 161774
    Texas 154542
    Texas 154603
    Texas 145891
    Texas 141254
    Texas 133710
    Texas 129998
    Texas 128278
    Texas 123298
    Texas 120815
    Texas 126031
    Texas 95701
    Texas 95537
    Texas 93337
    Texas 91482
    Texas 82603
    Texas 76614
    Texas 73441
    Texas 69422
    Texas 67820
    Texas 63502
    Texas 62593
    Texas 62994
    Texas 57324
    Texas 55581
    Texas 54657
    Texas 53235
    Texas 52902
    Texas 49046
    Texas 46608
    Texas 44784
    Texas 42390
    Texas 40487
    Texas 37785
    Texas 35332
    Texas 33199
    Texas 29635
    Texas 27357
    Texas 21864
    Texas 20249
    Texas 16946
    Texas 15033
    Texas 69392
    Texas 164724
    Texas 158669
    Texas 157386
    Texas 157374
    Texas 158236
    Texas 158722
    Texas 160506
    Texas 162126
    Texas 163788
    Texas 163500
    Texas 165717
    Texas 160176
    Texas 159167
    Texas 158693
    Texas 158580
    Texas 159654
    Texas 155841
    Texas 158372
    Texas 156767
    Texas 156778
    Texas 156625
    Texas 147729
    Texas 144433
    Texas 147865
    Texas 146961
    Texas 151098
    Texas 148823
    Texas 151810
    Texas 158452
    Texas 165252
    Texas 164600
    Texas 155658
    Texas 150518
    Texas 148996
    Texas 152593
    Texas 163350
    Texas 167597
    Texas 168463
    Texas 168421
    Texas 169355
    Texas 171412
    Texas 164244
    Texas 163809
    Texas 162822
    Texas 155226
    Texas 155427
    Texas 149105
    Texas 144081
    Texas 136873
    Texas 133610
    Texas 133121
    Texas 127211
    Texas 125058
    Texas 129694
    Texas 99379
    Texas 100403
    Texas 97778
    Texas 95755
    Texas 87189
    Texas 82764
    Texas 79048
    Texas 75160
    Texas 74358
    Texas 70332
    Texas 70089
    Texas 71266
    Texas 65074
    Texas 64383
    Texas 63639
    Texas 62713
    Texas 64996
    Texas 59894
    Texas 58527
    Texas 57708
    Texas 56446
    Texas 55989
    Texas 52656
    Texas 48993
    Texas 47681
    Texas 44609
    Texas 42132
    Texas 35378
    Texas 33852
    Texas 30076
    Texas 27961
    Texas 171538
```
#### Comment:
```
Great work! Along with in_, you can also use methods like and_ any_ to create more powerful where() clauses.
```
## 04. Filter data selected from a Table - Advanced
You're really getting the hang of this! SQLAlchemy also allows users to use conjunctions such as and_(), or_(), and not_() to build more complex filtering. For example, we can get a set of records for people in New York who are 21 or 37 years old with the following code:
```
select([census]).where(
  and_(census.columns.state == 'New York',
       or_(census.columns.age == 21,
          census.columns.age == 37
         )
      )
  )
 ```
 ### Instructions:
* Import and_ from the sqlalchemy module.
* Select all records from the census table.
* Append a where clause to filter all the records whose state is 'California', and whose sex is not 'M'.
* Iterate over the ResultProxy and print the age and sex columns from each record.

#### Script:
```
# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result['age'], result['sex'])
```
#### Output:
```
<script.py> output:
    0 F
    1 F
    2 F
    3 F
    4 F
    5 F
    6 F
    7 F
    8 F
    9 F
    10 F
    11 F
    12 F
    13 F
    14 F
    15 F
    16 F
    17 F
    18 F
    19 F
    20 F
    21 F
    22 F
    23 F
    24 F
    25 F
    26 F
    27 F
    28 F
    29 F
    30 F
    31 F
    32 F
    33 F
    34 F
    35 F
    36 F
    37 F
    38 F
    39 F
    40 F
    41 F
    42 F
    43 F
    44 F
    45 F
    46 F
    47 F
    48 F
    49 F
    50 F
    51 F
    52 F
    53 F
    54 F
    55 F
    56 F
    57 F
    58 F
    59 F
    60 F
    61 F
    62 F
    63 F
    64 F
    65 F
    66 F
    67 F
    68 F
    69 F
    70 F
    71 F
    72 F
    73 F
    74 F
    75 F
    76 F
    77 F
    78 F
    79 F
    80 F
    81 F
    82 F
    83 F
    84 F
    85 F
```
#### Comment:
Superb work - you're getting quite good at querying!

## 05. Ordering by a Single Column
To sort the result output by a field, we use the .order_by() method. By default, the .order_by() method sorts from lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to .order_by().

In the video, for example, Jason used stmt.order_by(census.columns.state) to sort the result output by the state column.

### Instructions:
* Select all records of the state column from the census table. To do this, pass census.columns.state as a list to select().
* Append an `.order_by()` to sort the result output by the state column.
* Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
* Print the first 10 rows of results.

#### Script:
```
# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])
```
#### Output:
```
<script.py> output:
    [('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',), ('Alabama',)]
```
#### Comment:
Well done! Unsurprisingly, when ordering the state column in ascending order, 'Alabama' is the first result.

## 06. Ordering in Descending Order by a Single Column
You can also use .order_by() to sort from highest to lowest by wrapping a column in the desc() function. Although you haven't seen this function in action, it generalizes what you have already learned.

Pass desc() (for "descending") inside an .order_by() with the name of the column you want to sort by. For instance, `stmt.order_by(desc(table.columns.column_name))` sorts column_name in descending order.

### Instructions:
* Import desc from the sqlalchemy module.
* Select all records of the state column from the census table.
* Append an `.order_by()` to sort the result output by the state column in descending order. Save the result as rev_stmt.
* Execute rev_stmt using connection.execute() and fetch all the results with .fetchall(). Save them as rev_results.
* Print the first 10 rows of rev_results.

#### Script:
```
# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])
```
#### Output:
```
<script.py> output:
    [('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',), ('Wyoming',)]
```
#### Comment:
Well done - 'Wyoming' is the first result when ordering by state in descending order! Next, you'll practice ordering by multiple columns!

## 07. Ordering by Multiple Columns
We can pass multiple arguments to the .order_by() method to order by multiple columns. In fact, we can also sort in ascending or descending order for each individual column. Each column in the `.order_by()` method is fully sorted from left to right. This means that the first column is completely sorted, and then within each matching group of values in the first column, it's sorted by the next column in the .order_by() method. This process is repeated until all the columns in the .order_by() are sorted.

### Instructions
* Select all records of the state and age columns from the census table.
* Use `.order_by()` to sort the output of the state column in ascending order and age in descending order. (NOTE: desc is already imported).
* Execute stmt using the .execute() method on connection and retrieve all the results using .fetchall().
* Print the first 20 results.

#### Script:
```
# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])
```
#### Output:
```
<script.py> output:
    [('Alabama', 85), ('Alabama', 85), ('Alabama', 84), ('Alabama', 84), ('Alabama', 83), ('Alabama', 83), ('Alabama', 82), ('Alabama', 82), ('Alabama', 81), ('Alabama', 81), ('Alabama', 80), ('Alabama', 80), ('Alabama', 79), ('Alabama', 79), ('Alabama', 78), ('Alabama', 78), ('Alabama', 77), ('Alabama', 77), ('Alabama', 76), ('Alabama', 76)]
```
#### Comment:
Excellent work! In the next video, you'll learn how to count and group your data!

## 08. Counting Distinct Data
As mentioned in the video, SQLAlchemy's func module provides access to built-in SQL functions that can make operations like counting and summing faster and more efficient.

In the video, Jason used func.sum() to get a sum of the pop2008 column of census as shown below:

```select([func.sum(census.columns.pop2008)])```
If instead you want to count the number of values in pop2008, you could use func.count() like this:

```select([func.count(census.columns.pop2008)])```
Furthermore, if you only want to count the distinct values of pop2008, you can use the .distinct() method:

```
select([func.count(census.columns.pop2008.distinct())])
```
In this exercise, you will practice using `func.count()` and `.distinct()` to get a count of the distinct number of states in census.

So far, you've seen .fetchall() and .first() used on a ResultProxy to get the results. The ResultProxy also has a method called `.scalar()` for getting just the value of a query that returns only one row and column.

This can be very useful when you are querying for just a count or sum.

### Instructions:
* Build a select statement to count the distinct values in the state field of census.
* Execute stmt to get the count and store the results as distinct_state_count.
* Print the value of distinct_state_count.

#### Script
```
# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)
```
#### Output:
```
<script.py> output:
    51
```

#### Comment:
Well done! Notice the use of the .scalar() method: This is useful when you want to get just the value of a query that returns only one row and column, like in this case.

## 09. Count of Records by State
Often, we want to get a count for each record with a particular value in another column. The `.group_by()` method helps answer this type of query. You can pass a column to the .group_by() method and use in an aggregate function like sum() or count(). Much like the .order_by() method, .group_by() can take multiple columns as arguments.

### Instructions:
* Import func from sqlalchemy.
* Build a select statement to get the value of the state field and a count of the values in the age field, and store it as stmt.
* Use the .group_by() method to group the statement by the state column.
* Execute stmt using the connection to get the count and store the results as results.
* Print the keys/column names of the results returned using `results[0].keys()`.

#### Script:
```
# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
```
#### Output:
```
<script.py> output:
    [('Alabama', 172), ('Alaska', 172), ('Arizona', 172), ('Arkansas', 172), ('California', 172), ('Colorado', 172), ('Connecticut', 172), ('Delaware', 172), ('District of Columbia', 172), ('Florida', 172), ('Georgia', 172), ('Hawaii', 172), ('Idaho', 172), ('Illinois', 172), ('Indiana', 172), ('Iowa', 172), ('Kansas', 172), ('Kentucky', 172), ('Louisiana', 172), ('Maine', 172), ('Maryland', 172), ('Massachusetts', 172), ('Michigan', 172), ('Minnesota', 172), ('Mississippi', 172), ('Missouri', 172), ('Montana', 172), ('Nebraska', 172), ('Nevada', 172), ('New Hampshire', 172), ('New Jersey', 172), ('New Mexico', 172), ('New York', 172), ('North Carolina', 172), ('North Dakota', 172), ('Ohio', 172), ('Oklahoma', 172), ('Oregon', 172), ('Pennsylvania', 172), ('Rhode Island', 172), ('South Carolina', 172), ('South Dakota', 172), ('Tennessee', 172), ('Texas', 172), ('Utah', 172), ('Vermont', 172), ('Virginia', 172), ('Washington', 172), ('West Virginia', 172), ('Wisconsin', 172), ('Wyoming', 172)]
    ['state', 'count_1']
```
#### Comment:
Fantastic work! Notice that the the key for the count method just came out as `count_1`. This can make it hard in complex queries to tell what column is being referred to: In the next exercise, you'll practice assign more descriptive labels when performing such calculations.

## 10. Determining the Population Sum by State
To avoid confusion with query result column names like `count_1`, we can use the `.label()` method to provide a name for the resulting column. This gets appendedto the function method we are using, and its argument is the name we want to use.

We can pair `func.sum()` with `.group_by()` to get a sum of the population by State and use the label() method to name the output.

We can also create the func.sum() expression before using it in the select statement. We do it the same way we would inside the select statement and store it in a variable. Then we use that variable in the select statement where the func.sum() would normally be.

### Instructions:
* Import func from sqlalchemy.
* Build an expression to calculate the sum of the values in the pop2008 field labeled as 'population'.
* Build a select statement to get the value of the state field and the sum of the values in pop2008.
* Group the statement by state using a `.group_by()` method.
* Execute stmt using the connection to get the count and store the results as results.
* Print the keys/column names of the results returned using `results[0].keys()`.

#### Script:
```
# Import func
from sqlalchemy import func

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
```
#### Output:
```
<script.py> output:
    [('Alabama', 4649367), ('Alaska', 664546), ('Arizona', 6480767), ('Arkansas', 2848432), ('California', 36609002), ('Colorado', 4912947), ('Connecticut', 3493783), ('Delaware', 869221), ('District of Columbia', 588910), ('Florida', 18257662), ('Georgia', 9622508), ('Hawaii', 1250676), ('Idaho', 1518914), ('Illinois', 12867077), ('Indiana', 6373299), ('Iowa', 3000490), ('Kansas', 2782245), ('Kentucky', 4254964), ('Louisiana', 4395797), ('Maine', 1312972), ('Maryland', 5604174), ('Massachusetts', 6492024), ('Michigan', 9998854), ('Minnesota', 5215815), ('Mississippi', 2922355), ('Missouri', 5891974), ('Montana', 963802), ('Nebraska', 1776757), ('Nevada', 2579387), ('New Hampshire', 1314533), ('New Jersey', 8670204), ('New Mexico', 1974993), ('New York', 19465159), ('North Carolina', 9121606), ('North Dakota', 634282), ('Ohio', 11476782), ('Oklahoma', 3620620), ('Oregon', 3786824), ('Pennsylvania', 12440129), ('Rhode Island', 1046535), ('South Carolina', 4438870), ('South Dakota', 800997), ('Tennessee', 6202407), ('Texas', 24214127), ('Utah', 2730919), ('Vermont', 620602), ('Virginia', 7648902), ('Washington', 6502019), ('West Virginia', 1812879), ('Wisconsin', 5625013), ('Wyoming', 529490)]
    ['state', 'population']
```
#### Comment:
Well done! With the column now labeled as population, it is far easier to make sense of the results. Do the populations of any states surprise you?

## 11. SQLAlchemy ResultsProxy and Pandas Dataframes
We can feed a ResultProxy directly into a pandas DataFrame, which is the workhorse of many Data Scientists in PythonLand. Jason demonstrated this in the video. In this exercise, you'll follow exactly the same approach to convert a ResultProxy into a DataFrame.

### Instructions:
* Import `pandas` as `pd`.
* Create a DataFrame df using pd.DataFrame() on the ResultProxy results.
* Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
* Print the DataFrame.

#### Script
```
# import pandas
import pandas as pd

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)
```
#### Output:
```
<script.py> output:
            state  population
    0  California    36609002
    1       Texas    24214127
    2    New York    19465159
    3     Florida    18257662
    4    Illinois    12867077
```
#### Comment:
Brilliant work! If you enjoy using pandas for your data scientific needs, you'll want to always feed ResultProxies into pandas DataFrames!

## 12. From SQLAlchemy results to a Graph
We can also take advantage of pandas and Matplotlib to build figures of our data. Remember that data visualization is essential for both exploratory data analysis and communication of your data!

### Instructions:
* Import matplotlib.pyplot as plt.
* Create a DataFrame df using pd.DataFrame() on the provided results.
* Set the columns of the DataFrame df.columns to be the columns from the first result object results[0].keys().
* Print the DataFrame df.
* Use the plot.bar() method on df to create a bar plot of the results.
* Display the plot with plt.show().

#### Script:
```
# Import pyplot as plt from matplotlib
from matplotlib import pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set Column names
df.columns = results[0].keys()

# Print the DataFrame
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()

```
#### Output:
![Alt text](./sqlalchemy_graph.png)

#### Comment:
Well done! You're ready to learn about more advanced SQLAlchemy Queries!
