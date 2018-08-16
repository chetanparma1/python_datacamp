# Chapter 3: Working with Relational Databases in Python

## Pop quiz: The relational model
Which of the following is not part of the relational model?

### Possible Answers
* Each row or record in a table represents an instance of an entity type.  &emsp;&emsp; press 1
* Each column in a table represents an attribute or feature of an instance.  &emsp;&emsp;  press 2
* Every table contains a primary key column, which has a unique entry for each row. &emsp;&emsp;  press 3
* A database consists of at least 3 tables.  &emsp;&emsp; press 4
* There are relations between tables.   &emsp;&emsp;   press 5

#### Answer:
4

##### Comment:
Correct!

## Creating a database engine
Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database 'Chinook.sqlite', which is in your working directory. Remember that to create an engine to connect to 'Northwind.sqlite', Hugo executed the command
```
engine = create_engine('sqlite:///Northwind.sqlite')
```
Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite. A little bit of background on the Chinook database: the Chinook database contains information about a semi-fictional digital media store in which media data is real and customer, employee and sales data has been manually created.

Why the name Chinook, you ask? According to their website,
```
The name of this sample database was based on the Northwind database. Chinooks are winds in the interior West of North America, where the Canadian Prairies and Great Plains meet various mountain ranges. Chinooks are most prevalent over southern Alberta in Canada. Chinook is a good name choice for a database that intends to be an alternative to Northwind.
```

### Instructions:
* Import the function create_engine from the module sqlalchemy.
* Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.

```{python}
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
```

#### Comment:
Awesome.

## What are the tables in the database?
In this exercise, you'll once again create an engine to connect to 'Chinook.sqlite'. Before you can get any data out of the database, however, you'll need to know what tables it contains!

To this end, you'll save the table names to a list using the method table_names() on the engine and then you will print the list.

### Instructions:
* Import the function create_engine from the module sqlalchemy.
* Create an engine to connect to the SQLite database 'Chinook.sqlite' and assign it to engine.
* Using the method table_names() on the engine engine, assign the table names of 'Chinook.sqlite' to the variable table_names.
* Print the object table_names to the shell.

```{python}
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
```

#### Output:
```
<script.py> output:
    ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']
```

##### Comment: 
Great job!

## The Hello World of SQL Queries!
Now, it's time for liftoff! In this exercise, you'll perform the Hello World of SQL queries, SELECT, in order to retrieve all columns of the table Album in the Chinook database. Recall that the query SELECT * selects all columns.

### Instructions:
* Open the engine connection as con using the method connect() on the engine.
* Execute the query that selects ALL columns from the Album table. Store the results in rs.
* Store all of your query results in the DataFrame df by applying the fetchall() method to the results rs.
* Close the connection!

```{python}
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
```
#### Output
```
<script.py> output:
       0                                      1  2
    0  1  For Those About To Rock We Salute You  1
    1  2                      Balls to the Wall  2
    2  3                      Restless and Wild  2
    3  4                      Let There Be Rock  1
    4  5                               Big Ones  3
```
##### Comment:
Good job!

## Customizing the Hello World of SQL Queries
Congratulations on executing your first SQL query! Now you're going to figure out how to customize your query in order to:

Select specified columns from a table;
Select a specified number of rows;
Import column names from the database table.
Recall that Hugo performed a very similar query customization in the video:

```
engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT OrderID, OrderDate, ShipName FROM Orders")
    df = pd.DataFrame(rs.fetchmany(size=5))
    df.columns = rs.keys()
```
Packages have already been imported as follows:

```
from sqlalchemy import create_engine
import pandas as pd
```
The engine has also already been created:

```
engine = create_engine('sqlite:///Chinook.sqlite')
````

The engine connection is already open with the statement

```
with engine.connect() as con:
```
All the code you need to complete is within this context.

### Instructions:
* Execute the SQL query that selects the columns LastName and Title from the Employee table. Store the results in the variable rs.
* Apply the method fetchmany() to rs in order to retrieve 3 of the records. Store them in the DataFrame df.
* Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.

```{python}
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
```
#### Output:
```
<script.py> output:
    3
      LastName                Title
    0    Adams      General Manager
    1  Edwards        Sales Manager
    2  Peacock  Sales Support Agent
```
##### Comment:
Awesome

## Filtering your database records using SQL's WHERE
You can now execute a basic SQL query to select records from any table in your database and you can also perform simple query customizations to select particular columns and numbers of rows.

There are a couple more standard SQL query chops that will aid you in your journey to becoming an SQL ninja.

Let's say, for example that you wanted to get all records from the Customer table of the Chinook database for which the Country is 'Canada'. You can do this very easily in SQL using a SELECT statement followed by a WHERE clause as follows:

```
SELECT * FROM Customer WHERE Country = 'Canada'
```
In fact, you can filter any SELECT statement by any condition using a WHERE clause. This is called filtering your records.

In this interactive exercise, you'll select all records of the Employee table for which 'EmployeeId' is greater than or equal to 6.

Packages are already imported as follows:

```
import pandas as pd
from sqlalchemy import create_engine
```
Query away!

### Instructions:
* Complete the argument of create_engine() so that the engine for the SQLite database 'Chinook.sqlite' is created.
* Execute the query that selects all records from the Employee table where 'EmployeeId' is greater than or equal to 6. Use the >= operator and assign the results to rs.
* Apply the method fetchall() to rs in order to fetch all records in rs. Store them in the DataFrame df.
* Using the rs object, set the DataFrame's column names to the corresponding names of the table columns.

```{python}
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())
```
#### Output:
```
<script.py> output:
       EmployeeId  LastName FirstName       Title  ReportsTo            BirthDate  \
    0           6  Mitchell   Michael  IT Manager          1  1973-07-01 00:00:00   
    1           7      King    Robert    IT Staff          6  1970-05-29 00:00:00   
    2           8  Callahan     Laura    IT Staff          6  1968-01-09 00:00:00   
    
                  HireDate                      Address        City State Country  \
    0  2003-10-17 00:00:00         5827 Bowness Road NW     Calgary    AB  Canada   
    1  2004-01-02 00:00:00  590 Columbia Boulevard West  Lethbridge    AB  Canada   
    2  2004-03-04 00:00:00                  923 7 ST NW  Lethbridge    AB  Canada   
    
      PostalCode              Phone                Fax                    Email  
    0    T3B 0C5  +1 (403) 246-9887  +1 (403) 246-9899  michael@chinookcorp.com  
    1    T1K 5N8  +1 (403) 456-9986  +1 (403) 456-8485   robert@chinookcorp.com  
    2    T1H 1Y8  +1 (403) 467-3351  +1 (403) 467-8772    laura@chinookcorp.com
```
##### Comment:
Good job!
