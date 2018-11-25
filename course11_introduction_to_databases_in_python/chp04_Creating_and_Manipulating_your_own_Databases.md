# Chapter 04: Creating and Manipulating your own Databases

## 01. Creating Tables with SQLAlchemy
Previously, you used the Table object to reflect a table from an existing database, but what if you wanted to create a new table? You'd still use the Table object; however, you'd need to replace the autoload and autoload_with parameters with Column objects.

The Column object takes a name, a SQLAlchemy type with an optional format, and optional keyword arguments for different constraints.

When defining the table, recall how in the video Jason passed in 255 as the maximum length of a String by using `Column('name', String(255))`. Checking out the slides from the video may help: you can download them by clicking on 'Slides' next to the IPython Shell.

After defining the table, you can create the table in the database by using the `.create_all()` method on metadata and supplying the engine as the only parameter. Go for it!

### Instructions:
* Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
* Build a new table called data with columns 'name' (String(255)), 'count' (Integer()), 'amount'(Float()), and 'valid' (Boolean()) columns. The second argument of Table() needs to be metadata, which has already been initialized.
* Create the table in the database by passing `engine` to `metadata.create_all()`.

#### Script:
```
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))
```
#### Output:
```
<script.py> output:
    Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>), schema=None)
```
#### Comment:
Well done! When creating a table, it's important to carefully think about what data types each column should be.
## 10. Creating Tables with SQLAlchemy
Previously, you used the Table object to reflect a table from an existing database, but what if you wanted to create a new table? You'd still use the Table object; however, you'd need to replace the autoload and autoload_with parameters with Column objects.

The Column object takes a name, a SQLAlchemy type with an optional format, and optional keyword arguments for different constraints.

When defining the table, recall how in the video Jason passed in 255 as the maximum length of a String by using `Column('name', String(255))`. Checking out the slides from the video may help: you can download them by clicking on 'Slides' next to the IPython Shell.

After defining the table, you can create the table in the database by using the `.create_all()` method on metadata and supplying the engine as the only parameter. Go for it!

### Instructions:
* Import Table, Column, String, Integer, Float, Boolean from sqlalchemy.
* Build a new table called data with columns 'name' (String(255)), 'count' (Integer()), 'amount'(Float()), and 'valid' (Boolean()) columns. The second argument of Table() needs to be metadata, which has already been initialized.
* Create the table in the database by passing `engine` to `metadata.create_all()`.

#### Script:
```
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))
```
#### Output:
```
<script.py> output:
    Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>), schema=None)
```
#### Comment:
Well done! When creating a table, it's important to carefully think about what data types each column should be.

## 02. Constraints and Data Defaults
You're now going to practice creating a table with some constraints! Often, you'll need to make sure that a column is unique, nullable, a positive value, or related to a column in another table. This is where constraints come in.

As Jason showed you in the video, in addition to constraints, you can also set a `default` value for the column if no data is passed to it via the default keyword on the column.

### Instructions:
* `Table`, `Column`, String, Integer, Float, Boolean are already imported from sqlalchemy.
* Build a new table called data with a unique name (String), count (Integer) defaulted to 1, amount (Float), and valid (Boolean) defaulted to False.
* Hit 'Submit Answer' to create the table in the database and to print the table details for data.

#### Script:
```
# Import Table, Column, String, Integer, Float, Boolean from sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print the table details
print(repr(metadata.tables['data']))
```
#### Output:
```
<script.py> output:
    Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>, default=ColumnDefault(1)), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>, default=ColumnDefault(False)), schema=None)
```
#### Comment:
Great work! Now that you know how to create tables, it's time to learn how to insert data into them!

## 03. Inserting a single row with an insert() statement
There are several ways to perform an insert with SQLAlchemy; however, we are going to focus on the one that follows the same pattern as the select statement.

It uses an `insert` statement where you specify the table as an argument, and supply the data you wish to insert into the value via the `.values()` method as keyword arguments.

Here, the name of the table is data.

### Instructions:
* Import `insert` and `select` from the sqlalchemy module.
* Build an insert statement for the data table to set name to 'Anna', count to 1, amount to 1000.00, and valid to True. Save the statement as stmt.
* Execute stmt with the connection and store the results.
* Print the rowcount attribute of results to see how many records were inserted.
* Build a select statement to query for the record with the name of 'Anna'.
* Hit 'Submit Answer' to print the results of executing the select statement.

#### Script:
```
# Import insert and select from sqlalchemy
from sqlalchemy import select, insert

# Build an insert statement to insert a record into the data table: stmt
stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)

# Execute the statement via the connection: results
results = connection.execute(stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(connection.execute(stmt).first())
```

#### Output:
```
In [1]: data
Out[1]: Table('data', MetaData(bind=None), Column('name', String(length=255), table=<data>), Column('count', Integer(), table=<data>), Column('amount', Float(), table=<data>), Column('valid', Boolean(), table=<data>), schema=None)
```
#### Comment:
Brilliant work! Often you'll want to insert multiple records at once, however - this is exactly what you'll practice doing in the next exercise!

## 04. Inserting Multiple Records at Once
It's time to practice inserting multiple records at once!

As Jason showed you in the video, you'll want to first build a list of dictionaries that represents the data you want to insert. Then, in the `.execute()` method, you can pair this list of dictionaries with an `insert` statement, which will insert all the records in your list of dictionaries.

### Instructions:
* Build a list of dictionaries called values_list with two dictionaries. In the first dictionary set name to 'Anna', count to 1, amount to 1000.00, and valid to True. In the second dictionary of the list, set name to 'Taylor', count to 1, amount to 750.00, and valid to False.
* Build an insert statement for the data table for a multiple insert, save it as stmt.
* Execute stmt with the values_list via connection and store the results. Make sure values_list is the second argument to .execute().
* Print the `rowcount` of the `results`.

#### Script:
```
# Build a list of dictionaries: values_list
values_list = [
    {'name': 'Anna', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name':'Taylor', 'count':1, 'amount':750.00, 'valid':False}
]

# Build an insert statement for the data table: stmt
stmt = insert(data)

# Execute stmt with the values_list: results
results = connection.execute(stmt, values_list)

##### Alternative:
## stmt = insert(data).values(values_list)
## results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

```
#### Output:
```
<script.py> output:
    2
```
#### Comment:
Superb work - that's all there is to inserting multiple records at once!

## 05. Loading a CSV into a Table
You've done a great job so far at inserting data into tables! You're now going to learn how to load the contents of a CSV file into a table.

We have used the csv module to set up a csv_reader, which is just a reader object that can iterate over the lines in a given CSV file - in this case, a census CSV file. Using the enumerate() function, you can loop over the csv_reader to handle the results one at a time. Here, for example, the first line it would return is:
```
0 ['Illinois', 'M', '0', '89600', '95012']
```

0 is the idx - or line number - while `['Illinois', 'M', '0', '89600', '95012']` is the row, corresponding to the column names 'state' , 'sex', 'age', 'pop2000 'and 'pop2008'. 'Illinois' can be accessed with row[0], 'M' with row[1], and so on. You can create a dictionary containing this information where the keys are the column names and the values are the entries in each line. Then, by appending this dictionary to a list, you can combine it with an insert statement to load it all into a table!

### Instructions:
* Create a statement for bulk insert into the census table. To do this, just use insert() and census.
* Create an empty list called values_list and a variable called total_rowcount that is set to 0.
* Within the for loop:
** Complete the data dictionary by filling in the values for each of the keys. The values are contained in row. row[0] represents the value for 'state', row[1] represents the value for 'sex', and so on.
** Append data to values_list.
** If 51 cleanly divides into the current idx:
** Execute stmt with the values_list and save it as results.
* Hit 'Submit Answer' to print total_rowcount when done with all the records.

#### Script:
```
# Create a insert statement for census: stmt
stmt = insert(census)

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    #create data and append to values_list
    data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)
```

#### Output:
```
In [1]: for idx, row in enumerate(csv_reader):
...    print(idx, row)
...    if idx == 21:
...       break
0 ['Illinois', 'M', '0', '89600', '95012']
1 ['Illinois', 'M', '1', '88445', '91829']
2 ['Illinois', 'M', '2', '88729', '89547']
3 ['Illinois', 'M', '3', '88868', '90037']
4 ['Illinois', 'M', '4', '91947', '91111']
5 ['Illinois', 'M', '5', '93894', '89802']
6 ['Illinois', 'M', '6', '93676', '88931']
7 ['Illinois', 'M', '7', '94818', '90940']
8 ['Illinois', 'M', '8', '95035', '86943']
9 ['Illinois', 'M', '9', '96436', '86055']
10 ['Illinois', 'M', '10', '97280', '86565']
11 ['Illinois', 'M', '11', '94029', '86606']
12 ['Illinois', 'M', '12', '92402', '89596']
13 ['Illinois', 'M', '13', '89926', '91661']
14 ['Illinois', 'M', '14', '90717', '91256']
15 ['Illinois', 'M', '15', '92178', '92729']
16 ['Illinois', 'M', '16', '90587', '93083']
17 ['Illinois', 'M', '17', '92782', '94541']
18 ['Illinois', 'M', '18', '90997', '100253']
19 ['Illinois', 'M', '19', '89629', '96588']
20 ['Illinois', 'M', '20', '91040', '95460']
21 ['Illinois', 'M', '21', '85176', '91373']

```
```
<script.py> output:
    8722
```
#### Comment:
Great work! It looks like there are 8722 rows in this table.

## 06. Updating individual records
The `update` statement is very similar to an insert statement, except that it also typically uses a where clause to help us determine what data to update. You'll be using the FIPS state code using here, which is appropriated by the U.S. government to identify U.S. states and certain other associated areas. Recall that you can update all wages in the employees table as follows:
```
stmt = update(employees).values(wage=100.00)
```
For your convenience, the names of the tables and columns of interest in this exercise are: state_fact (Table), name (Column), and fips_state (Column).

### Instructions:
* Build a statement to select all columns from the `state_fact` table where the `name` column is New York. Call it select_stmt.
* Print the results of executing the select_stmt and fetching all records.
* Build an update statement to change the fips_state column code to 36, save it as stmt.
* Use a where clause to filter for states with the name of 'New York' in the state_fact table.
* Execute stmt via the connection and save the output as results.
* Hit 'Submit Answer' to print the rowcount of the results and the results of executing select_stmt. This will verify the fips_state code is now 36.

#### Script:
```
# Build a select statement: select_stmt
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(connection.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36: stmt
# note that when defining a value to a column, either in insert or update query, 
# we can directly write the column name without needing to mention the table.columns.column_name. 
stmt = update(state_fact).values(fips_state = 36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement: results
results = connection.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(connection.execute(select_stmt).fetchall())
```
#### Output:
```

<script.py> output:
    [('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '0', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
    1
    [('32', 'New York', 'NY', 'USA', 'state', '10', 'current', 'occupied', '', '36', 'N.Y.', 'II', '1', 'Northeast', '2', 'Mid-Atlantic', '2')]
```
#### Comment:
Well done! As you can see, after executing the update statement, the fips_state code gets updated to 36.
