# Chapter 05: Putting It All Together

## 01. Setup the Engine and MetaData
In this exercise, your job is to create an engine to the database that will be used in this chapter. Then, you need to initialize its metadata.

Recall how you did this in Chapter 1 by leveraging `create_engine()` and `MetaData`.

### Instructions:
* Import `create_engine` and `MetaData` from sqlalchemy.
* Create an engine to the chapter 5 database by using 'sqlite:///chapter5.sqlite' as the connection string.
* Create a MetaData object as metadata.

#### Script:
```
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData()

```
#### Comment:
Well done! Setting up the engine and metadata should be second nature to you by this point!

## 02. Create the Table to the Database
Having setup the engine and initialized the metadata, you will now define the census table object and then create it in the database using the `metadata` and `engine` from the previous exercise. To create it in the database, you will have to use the `.create_all()` method on the metadata with engine as the argument.

It may help to refer back to the Chapter 4 exercise in which you learned how to create a table.

### Instructions:
* Import Table, Column, String, and Integer from sqlalchemy.
* Define a census table with the following columns:
** 'state' - String - length of 30
** 'sex' - String - length of 1
** 'age' - Integer
** 'pop2000' - Integer
** 'pop2008' - Integer
* Create the table in the database using the metadata and engine.

#### Script:
```
# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))

# Create the table in the database
metadata.create_all(engine)

```
#### Comment:
Wonderful work! When creating columns of type String(), it's important to spend some time thinking about what their maximum lengths should be.


## 03. Reading the Data from the CSV
Leverage the Python CSV module from the standard library and load the data into a list of dictionaries.

It may help to refer back to the <a href="https://campus.datacamp.com/courses/introduction-to-relational-databases-in-python/creating-and-manipulating-your-own-databases?ex=7">Chapter 4</a> exercise in which you did something similar.

### Instructions:
* Create an empty list called values_list.
*Iterate over the rows of csv_reader with a for loop, creating a dictionary called data for each row and append it to values_list.
** Within the for loop, row will be a list whose entries are 'state' , 'sex', 'age', 'pop2000' and 'pop2008' (in that order).

#### Script:
```
# Create an empty list: values_list
values_list = []

# Iterate over the rows
for row in csv_reader:
    # Create a dictionary with the values
    data = {'state': row[0], 'sex': row[1], 'age':row[2], 'pop2000': row[3],
            'pop2008': row[4]}
    # Append the dictionary to the values list
    values_list.append(data)

```
#### Comment:
Marvelous! Next, you'll practice how to load data from a list into the table!

## 04. Load Data from a list into the Table
Using the multiple insert pattern, in this exercise, you will load the data from values_list into the table.

### Instructions:
* Import insert from sqlalchemy.
* Build an insert statement for the census table.
* Execute the statement stmt along with values_list. You will need to pass them both as arguments to connection.execute().
* Print the rowcount attribute of results.

#### Script:
```
# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)

```
#### Output:
```
<script.py> output:
    8772
```
#### Comment:
Amazing work! It's time to begin wrapping everything up by building some interesting queries!

## 05. Build a Query to Determine the Average Age by Population
In this exercise, you will use the `func.sum()` and group_by() methods to first determine the average age weighted by the population in 2008, and then group by sex.

As Jason discussed in the video, a weighted average is calculated as the sum of the product of the weights and averages divided by the sum of all the weights.

For example, the following statement determines the average age weighted by the population in 2000:
```
stmt = select([census.columns.sex,
               (func.sum(census.columns.pop2000 * census.columns.age) /
                func.sum(census.columns.pop2000)).label('average_age')
               ])
```

### Instructions:
* Import select from sqlalchemy.
* Build a statement to:
** Select sex from the census table.
** Select the average age weighted by the population in 2008 (pop2008). See the example given in the assignment text to see how you can do this. Label this average age calculation as 'average_age'.
* Group the query by sex.
* Execute the query and store it as results.
* Loop over results and print the sex and average_age for each record.

#### Script:
```
# Import select
from sqlalchemy import select

# Calculate weighted average age: stmt
stmt = select([census.columns.sex,
               (func.sum(census.columns.age * census.columns.pop2008) /
                func.sum(census.columns.pop2008)).label('average_age')
               ])

# Group by sex
stmt = stmt.group_by(census.columns.sex)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the average age by sex
for r in results:
    print(r[0], r[1])
```
#### Output:
```
<script.py> output:
    F 38
    M 35
```
#### Comment:
Well done! It seems like, in the US in 2008, the average age of females in was higher than males.
