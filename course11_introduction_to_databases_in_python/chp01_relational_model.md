# Chapter 01: Relational Model

## 01. Relational Model
Which of the following is not part of the relational model?

### Possible Answers
* Tables
** press 1
* Columns
** press 2
* Rows
** press 3
* Dimensions
** press 4
* Relationships
press 5

#### Answer:
4

#### TComment:
hat is correct! Tables, Columns, Rows, and Relationships are all part of the relational model. Dimensions are not!

## 02. Engines and Connection Strings
Alright, it's time to create your first engine! An engine is just a common interface to a database, and the information it requires to connect to one is contained in a connection string, such as sqlite:///census_nyc.sqlite. Here, sqlite is the database driver, while census_nyc.sqlite is a SQLite file contained in the local directory.

You can learn a lot more about connection strings in the <a href="http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls">SQLAlchemy documentation</a>.

Your job in this exercise is to create an engine that connects to a local SQLite file named census.sqlite. Then, print the names of the tables it contains using the .table_names() method. Note that when you just want to print the table names, you do not need to use engine.connect() after creating the engine.

### Instructions:
* Import create_engine from the sqlalchemy module.
* Using the `create_engine()` function, create an engine for a local file named census.sqlite with sqlite as the driver. Be sure to enclose the connection string within quotation marks.
* Print the output from the `.table_names()` method on the engine.

#### Script:
```
# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())
```
#### Output:
```
<script.py> output:
    ['census', 'state_fact']
```
#### Comment:
Wonderful work! This database has two tables, as you can see: 'census' and 'state_fact'. You'll be exploring both of these and more throughout this course!

## 03. Autoloading Tables from a Database
SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information. It's the opposite of creating a Table by hand and is very useful for working with existing databases. To perform reflection, you need to import the Table object from the SQLAlchemy package. Then, you use this Table object to read your table from the engine and autoload the columns. Using the Table object in this manner is a lot like passing arguments to a function. For example, to autoload the columns with the engine, you have to specify the keyword arguments autoload=True and autoload_with=engine to Table().

In this exercise, your job is to reflect the census table available on your engine into a variable called `census`. The metadata has already been loaded for you using `MetaData()` and is available in the variable `metadata`.

### Instructions:
* Import the Table object from sqlalchemy.
* Reflect the census table by using the Table object with the arguments:
** The name of the table as a string ('census').
** The metadata, contained in the variable metadata.
autoload=True
** The engine to autoload with - in this case, engine.
* Print the details of census using the repr() function.

#### Script:
```
# Import Table
from sqlalchemy import Table

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))
```
#### Output:
```
<script.py> output:
    Table('census', MetaData(bind=None), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)
```
#### Comment:
Well done! Reflecting a table allows you to work with it in Python.

## 04. Viewing Table Details
Great job reflecting the census table! Now you can begin to learn more about the columns and structure of your table. It is important to get an understanding of your database by examining the column names. This can be done by using the .columns attribute and accessing the .keys() method. For example, census.columns.keys() would return a list of column names of the census table.

Following this, we can use the metadata container to find out more details about the reflected table such as the columns and their types. For example, table objects are stored in the metadata.tables dictionary, so you can get the metadata of your census table with metadata.tables['census']. This is similar to your use of the repr() function on the census table from the previous exercise.

### Instructions:
* Reflect the census table as you did in the previous exercise using the Table() function.
* Print a list of column names of the census table by applying the .keys() method to census.columns.
* Print the details of the census table using the metadata.tables dictionary along with the repr() function. To do this, first access the 'census' key of the metadata.tables dictionary, and place this inside the provided repr() function.
