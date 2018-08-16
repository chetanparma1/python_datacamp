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
