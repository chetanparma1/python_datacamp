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
