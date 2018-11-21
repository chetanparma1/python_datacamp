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
