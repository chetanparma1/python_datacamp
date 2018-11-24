# Chapter 03: Advanced SQLAlchemy Queries

## 01. Connecting to a MySQL Database
Before you jump into the calculation exercises, let's begin by connecting to our database. Recall that in the last chapter you connected to a PostgreSQL database. Now, you'll connect to a MySQL database, for which many prefer to use the pymysql database driver, which, like psycopg2 for PostgreSQL, you have to install prior to use.

This connection string is going to start with 'mysql+pymysql://', indicating which dialect and driver you're using to establish the connection. The dialect block is followed by the `'username:password'` combo. Next, you specify the host and port with the following `'@host:port/'`. Finally, you wrap up the connection string with the 'database_name'.

Now you'll practice connecting to a MySQL database: it will be the same census database that you have already been working with. One of the great things about SQLAlchemy is that, after connecting, it abstracts over the type of database it has connected to and you can write the same SQLAlchemy code, regardless!

### Instructions:
* Import the create_engine function from the sqlalchemy library.
* Create an engine to the census database by concatenating the following strings and passing them to create_engine():
** 'mysql+pymysql://' (the dialect and driver).
** 'student:datacamp' (the username and password).
** '@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/' (the host and port).
** 'census' (the database name).
* Use the .table_names() method on engine to print the table names.

#### Script
```
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
# mysql = dialect
# pymysql = driver
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

# Print the table names
print(engine.table_names())
```
#### Output:
```
<script.py> output:
    ['census', 'state_fact']
```
#### Comment:
Well done! This database, like the one you explored in Chapter 1, has two tables: 'census', and 'state_fact'.

## 02. Calculating a Difference between Two Columns
Often, you'll need to perform math operations as part of a query, such as if you wanted to calculate the change in population from 2000 to 2008. For math operations on numbers, the operators in SQLAlchemy work the same way as they do in Python.

You can use these operators to perform addition (`+`), subtraction (`-`), multiplication (*), division (/), and modulus (%) operations. Note: They behave differently when used with non-numeric column types.

Let's now find the top 5 states by population growth between 2000 and 2008.

### Instructions:
* Define a select statement called stmt to return:
** i) The state column of the census table (census.columns.state).
** ii) The difference in population count between 2008 (census.columns.pop2008) and 2000 (census.columns.pop2000) labeled as 'pop_change'.
* Group the statement by census.columns.state.
* Order the statement by population change ('pop_change') in descending order. Do so by passing it desc('pop_change').
* Use the .limit() method on the statement to return only 5 records.
* Execute the statement and fetchall() the records.
* The print statement has already been written for you. Hit 'Submit Answer' to view the results!

#### Script:
```
# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008 - census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt
stmt = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt
stmt = stmt.order_by(desc('pop_change'))

# Return only 5 results: stmt
stmt = stmt.limit(5)

# Use connection to execute the statement and fetch all results
results = connection.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
```

#### Output:
```
In [3]: census.columns.keys()
Out[3]: ['state', 'sex', 'age', 'pop2000', 'pop2008']
```
```
<script.py> output:
    California:105705
    Florida:100984
    Texas:51901
    New York:47098
    Pennsylvania:42387
```
#### Comment:
Excellent work! It looks like California grew the most between 2000 and 2008!

## 03. Determining the Overall Percentage of Females
It's possible to combine functions and operators in a single select statement as well. These combinations can be exceptionally handy when we want to calculate percentages or averages, and we can also use the `case()` expression to operate on data that meets specific criteria while not affecting the query as a whole. The `case()` expression accepts a list of conditions to match and the column to return if the condition matches, followed by an `else_ if` none of the conditions match. We can wrap this entire expression in any function or math operation we like.

Often when performing integer division, we want to get a float back. While some databases will do this automatically, you can use the `cast()` function to convert an expression to a particular type.

### Instructions:
* Import case, cast, and Float from sqlalchemy.
* Build an expression female_pop2000to calculate female population in 2000. To achieve this:
** Use case() inside func.sum().
** The first argument of case() is a list containing a tuple of
*** i) A boolean checking that census.columns.sex is equal to 'F'.
*** ii) The column census.columns.pop2000.
** The second argument is the else_ condition, which should be set to 0.
* Calculate the total population in 2000 and use cast() to convert it to Float.
* Build a query to calculate the percentage of females in 2000. To do this, divide female_pop2000 by total_pop2000 and multiply by 100.
* Execute the query and print percent_female.

#### Script:
```
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([female_pop2000 / total_pop2000* 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)
```

#### Output:
```
<script.py> output:
    51.0946743229
```
#### Comment:
Well done! It looks like there were slightly more females than males in the US population in 2000!

## 04. Automatic Joins with an Established Relationship
If you have two tables that already have an established relationship, you can automatically use that relationship by just adding the columns we want from each table to the select statement. Recall that Jason constructed the following query:
```
stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])
```
in order to join the census and state_fact tables and select the pop2008 column from the first and the abbreviation column from the second. In this case, the census and state_fact tables had a pre-defined relationship: the state column of the former corresponded to the name column of the latter.

In this exercise, you'll use the same predefined relationship to select the `pop2000` and `abbreviation` columns!

### Instructions:
* Build a statement to join the census and state_fact tables and select the pop2000 column from the first and the abbreviation column from the second.
* Execute the statement to get the first result and save it as result.
* Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!

#### Script:
```
# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))
```
#### Output:
```
<script.py> output:
    pop2000 89600
    abbreviation IL

In [1]: 
```
#### Comment:
Great work - it's always useful to take advantage of established relationships, like in this case.

## 05. Joins
If you aren't selecting columns from both tables or the two tables don't have a defined relationship, you can still use the .join() method on a table to join it with another table and get extra data related to our query. The join() takes the table object you want to join in as the first argument and a condition that indicates how the tables are related to the second argument. Finally, you use the .select_from() method on the select statement to wrap the join clause. For example, in the video, Jason executed the following code to join the census table to the state_fact table such that the state column of the census table corresponded to the name column of the `state_fact` table.
```
stmt = stmt.select_from(
    census.join(
        state_fact, census.columns.state == 
        state_fact.columns.name)
```
### Instructioons:
* Build a statement to select ALL the columns from the census and state_fact tables. To select ALL the columns from two tables employees and sales, for example, you would use stmt = select([employees, sales]).
* Append a select_from to stmt to join the census table to the state_fact table by the state column in census and the name column in the state_fact table.
* Execute the statement to get the first result and save it as result. This code is already written.
* Hit 'Submit Answer' to loop over the keys of the result object, and print the key and value for each!

#### Script
```
# Build a statement to select the census and state_fact tables: stmt
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))

```
#### Output:
```
In [1]: census.columns.keys()
Out[1]: ['state', 'sex', 'age', 'pop2000', 'pop2008']

In [2]: state_fact.columns.keys()
Out[2]: 
['id',
 'name',
 'abbreviation',
 'country',
 'type',
 'sort',
 'status',
 'occupied',
 'notes',
 'fips_state',
 'assoc_press',
 'standard_federal_region',
 'census_region',
 'census_region_name',
 'census_division',
 'census_division_name',
 'circuit_court']

In [3]: 
```
```
<script.py> output:
    state Illinois
    sex M
    age 0
    pop2000 89600
    pop2008 95012
    id 13
    name Illinois
    abbreviation IL
    country USA
    type state
    sort 10
    status current
    occupied occupied
    notes 
    fips_state 17
    assoc_press Ill.
    standard_federal_region V
    census_region 2
    census_region_name Midwest
    census_division 3
    census_division_name East North Central
    circuit_court 7

```
#### Comment:
Fantastic work! You'll get more practice with joins in the next exercise!

## 06. More Practice with Joins
You can use the same select statement you built in the last exercise, however, let's add a twist and only return a few columns and use the other table in a group_by() clause.

### Instructions:
* Build a statement to select:
** The state column from the census table.
** The sum of the pop2008 column from the census table.
** The census_division_name column from the state_fact table.
* Append a .select_from() to stmt in order to join the census and state_fact tables by the state and name columns.
* Group the statement by the name column of the state_fact table.
* Execute the statement to get all the records and save it as results.
* Hit 'Submit Answer' to loop over the results object and print each record.

#### Script:
```
# Build a statement to select the state, sum of 2008 population and census
# division name: stmt
stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])

# Append select_from to join the census and state_fact tables by the census state and state_fact name columns
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name)
)

# Append a group by for the state_fact name column
stmt = stmt.group_by(state_fact.columns.name)

# Execute the statement and get the results: results
results = connection.execute(stmt).fetchall()

# Loop over the the results object and print each record.
for record in results:
    print(record)
```
#### Output:
```
<script.py> output:
    ('Alabama', 4649367, 'East South Central')
    ('Alaska', 664546, 'Pacific')
    ('Arizona', 6480767, 'Mountain')
    ('Arkansas', 2848432, 'West South Central')
    ('California', 36609002, 'Pacific')
    ('Colorado', 4912947, 'Mountain')
    ('Connecticut', 3493783, 'New England')
    ('Delaware', 869221, 'South Atlantic')
    ('Florida', 18257662, 'South Atlantic')
    ('Georgia', 9622508, 'South Atlantic')
    ('Hawaii', 1250676, 'Pacific')
    ('Idaho', 1518914, 'Mountain')
    ('Illinois', 12867077, 'East North Central')
    ('Indiana', 6373299, 'East North Central')
    ('Iowa', 3000490, 'West North Central')
    ('Kansas', 2782245, 'West North Central')
    ('Kentucky', 4254964, 'East South Central')
    ('Louisiana', 4395797, 'West South Central')
    ('Maine', 1312972, 'New England')
    ('Maryland', 5604174, 'South Atlantic')
    ('Massachusetts', 6492024, 'New England')
    ('Michigan', 9998854, 'East North Central')
    ('Minnesota', 5215815, 'West North Central')
    ('Mississippi', 2922355, 'East South Central')
    ('Missouri', 5891974, 'West North Central')
    ('Montana', 963802, 'Mountain')
    ('Nebraska', 1776757, 'West North Central')
    ('Nevada', 2579387, 'Mountain')
    ('New Hampshire', 1314533, 'New England')
    ('New Jersey', 8670204, 'Mid-Atlantic')
    ('New Mexico', 1974993, 'Mountain')
    ('New York', 19465159, 'Mid-Atlantic')
    ('North Carolina', 9121606, 'South Atlantic')
    ('North Dakota', 634282, 'West North Central')
    ('Ohio', 11476782, 'East North Central')
    ('Oklahoma', 3620620, 'West South Central')
    ('Oregon', 3786824, 'Pacific')
    ('Pennsylvania', 12440129, 'Mid-Atlantic')
    ('Rhode Island', 1046535, 'New England')
    ('South Carolina', 4438870, 'South Atlantic')
    ('South Dakota', 800997, 'West North Central')
    ('Tennessee', 6202407, 'East South Central')
    ('Texas', 24214127, 'West South Central')
    ('Utah', 2730919, 'Mountain')
    ('Vermont', 620602, 'New England')
    ('Virginia', 7648902, 'South Atlantic')
    ('Washington', 6502019, 'Pacific')
    ('West Virginia', 1812879, 'South Atlantic')
    ('Wisconsin', 5625013, 'East North Central')
    ('Wyoming', 529490, 'Mountain')
```
#### Comment:
Brilliant! The ability to join tables like this is what makes relational databases so powerful.

## 07. Using alias to handle same table joined queries
Often, you'll have tables that contain hierarchical data, such as employees and managers who are also employees. For this reason, you may wish to join a table to itself on different columns. The .alias() method, which creates a copy of a table, helps accomplish this task. Because it's the same table, you only need a where clause to specify the join condition.

Here, you'll use the `.alias()` method to build a query to join the `employees` table against itself to determine to whom everyone reports.

### Instructions:
* Save an alias of the employees table as managers. To do so, apply the method .alias() to employees.
* Build a query to select the employee name and their manager's name. The manager's name has already been selected for you. * Use label to label the name column of employees as 'employee'.
* Append a where clause to stmt to match where the id column of the managers table corresponds to the mgr column of the employees table.
* Order the statement by the name column of the managers table.
* Execute the statement and store all the results. This code is already written. Hit 'Submit Answer' to print the names of the managers and all their employees.

#### Script:
```
# finding who are the subordinate of each manager

# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select manager's and their employees names: stmt
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Match managers id with employees mgr: stmt
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Order the statement by the managers name: stmt
stmt = stmt.order_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt).fetchall()

# Print records
for record in results:
    print(record)
```

#### Output:
```
In [1]: employees.columns.keys()
Out[1]: ['id', 'name', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'dept']
```
```

<script.py> output:
    ('FILLMORE', 'GRANT')
    ('FILLMORE', 'ADAMS')
    ('FILLMORE', 'MONROE')
    ('GARFIELD', 'JOHNSON')
    ('GARFIELD', 'LINCOLN')
    ('GARFIELD', 'POLK')
    ('GARFIELD', 'WASHINGTON')
    ('HARDING', 'TAFT')
    ('HARDING', 'HOOVER')
    ('JACKSON', 'HARDING')
    ('JACKSON', 'GARFIELD')
    ('JACKSON', 'FILLMORE')
    ('JACKSON', 'ROOSEVELT')

In [1]: 
```
#### Comment:
Well done! It's important to be able to work with hierarchical tables.

## 08. Leveraging Functions and Group_bys with Hierarchical Data
It's also common to want to roll up data which is in a hierarchical table. Rolling up data requires making sure you're careful which alias you use to perform the group_bys and which table you use for the function.

Here, your job is to get a count of employees for each manager.

### Instructions:
* Save an alias of the `employees` table as `managers`.
* Build a query to select the name column of the managers table and the count of the number of their employees. The function func.count() has been imported and will be useful! Use it to count the id column of the employees table.
* Using a .where() clause, filter the records where the id column of the managers table and mgr column of the employees table are equal.
* Group the query by the name column of the managers table.
* Execute the statement and store all the results. Print the names of the managers and their employees. This code has already been written so hit 'Submit Answer' and check out the results!

#### Script:
```
# Make an alias of the employees table: managers
managers = employees.alias()

# Build a query to select managers and counts of their employees: stmt
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name
stmt = stmt.group_by(managers.columns.name)

# Execute statement: results
results = connection.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)


## My note:
# there's a problem when trying to select all rows from table employees. 
# ValueError: Couldn't parse datetime string
# need to find the way to handle this. 
```
#### Output:
```
In [2]: metadata.tables['employees']
Out[2]: Table('employees', MetaData(bind=None), Column('id', INTEGER(), table=<employees>, primary_key=True, nullable=False), Column('name', VARCHAR(length=20), table=<employees>), Column('job', VARCHAR(length=20), table=<employees>), Column('mgr', INTEGER(), table=<employees>), Column('hiredate', DATETIME(), table=<employees>), Column('sal', NUMERIC(precision=7, scale=2), table=<employees>), Column('comm', NUMERIC(precision=7, scale=2), table=<employees>), Column('dept', INTEGER(), table=<employees>), schema=None)
```
```
<script.py> output:
    ('FILLMORE', 3)
    ('GARFIELD', 4)
    ('HARDING', 2)
    ('JACKSON', 4)
```
##### Comment:
Great work- you're becoming a SQLAlchemy master! In the next video, you'll learn how to deal with large ResultSets.

## 09. Working on Blocks of Records
Fantastic work so far! As Jason discussed in the video, sometimes you may have the need to work on a large ResultProxy, and you may not have the memory to load all the results at once. To work around that issue, you can get blocks of rows from the ResultProxy by using the `.fetchmany()` method inside a loop. With `.fetchmany()`, give it an argument of the number of records you want. When you reach an empty list, there are no more rows left to fetch, and you have processed all the results of the query. Then you need to use the .close() method to close out the connection to the database.

You'll now have the chance to practice this on a large ResultProxy called results_proxy that has been pre-loaded for you to work with.

### Instructions:
* Use a `while` loop that checks if there are `more_results`.
* Inside the loop, apply the method .fetchmany() to results_proxy to get 50 records at a time and store those records as partial_results.
* After fetching the records, if partial_results is an empty list (that is, if it is equal to []), set more_results to False.
* Loop over the partial_results and, if row.state is a key in the state_count dictionary, increment state_count[row.state] by 1; otherwise set state_count[row.state] to 1.
* After the while loop, close the ResultProxy results_proxy using .close().
* Hit 'Submit Answer' to print state_count.

#### Script:
```
# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)
```

#### Output:
```
In [6]: results_proxy.fetchmany(50)[0].keys()
Out[6]: ['state', 'sex', 'age', 'pop2000', 'pop2008']
```
```
<script.py> output:
    {'Maryland': 49, 'New Jersey': 172, 'District of Columbia': 172, 'Illinois': 172, 'Massachusetts': 16, 'North Dakota': 75, 'Idaho': 172, 'Florida': 172}
```
#### Comment:
Wonderful work! As a data scientist, you'll inevitably come across huge databases, and being able to work on them in blocks is a vital skill.
