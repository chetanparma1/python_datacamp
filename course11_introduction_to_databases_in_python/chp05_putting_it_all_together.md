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

## 06. Build a Query to Determine the Percentage of Population by Gender and State
In this exercise, you will write a query to determine the percentage of the population in 2000 that comprised of women. You will group this query by state.

### Instructions:
* Import case, cast and Float from sqlalchemy.
* Define a statement to select state and the percentage of females in 2000.
** Inside func.sum(), use case() to select females (using the sex column) from pop2000. Remember to specify else_=0 if the sex is not 'F'.
** To get the percentage, divide the number of females in the year 2000 by the overall population in 2000. Cast the divisor - census.columns.pop2000 - to Float before multiplying by 100.
* Group the query by state.
* Execute the query and store it as results.
* Print state and percent_female for each record. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build a query to calculate the percentage of females in 2000: stmt
stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

# Group By state
stmt = stmt.group_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the percentage
for result in results:
    print(result.state, result.percent_female)

```
#### Output:
```

<script.py> output:
    Alabama 51.8324077702
    Alaska 49.3014978935
    Arizona 50.2236130306
    Arkansas 51.2699284622
    California 50.3523321490
    Colorado 49.8476706030
    Connecticut 51.6681650713
    Delaware 51.6110973356
    District of Columbia 53.1296261417
    Florida 51.3648800117
    Georgia 51.1140835034
    Hawaii 51.1180118369
    Idaho 49.9897262390
    Illinois 51.1122423480
    Indiana 50.9548031330
    Iowa 50.9503983425
    Kansas 50.8218641078
    Kentucky 51.3268703693
    Louisiana 51.7535159655
    Maine 51.5057081342
    Maryland 51.9357554997
    Massachusetts 51.8430235713
    Michigan 50.9724651832
    Minnesota 50.4933294430
    Mississippi 51.9222948179
    Missouri 51.4688860264
    Montana 50.3220269073
    Nebraska 50.8584549336
    Nevada 49.3673636138
    New Hampshire 50.8580198450
    New Jersey 51.5171395613
    New Mexico 51.0471720798
    New York 51.8345386515
    North Carolina 51.4822623221
    North Dakota 50.5006936323
    Ohio 51.4655035002
    Oklahoma 51.1136245708
    Oregon 50.4294670362
    Pennsylvania 51.7404347305
    Rhode Island 52.0734339190
    South Carolina 51.7307212977
    South Dakota 50.5258358137
    Tennessee 51.4306896994
    Texas 50.5157216642
    Utah 49.9729527511
    Vermont 51.0185732099
    Virginia 51.6572524472
    Washington 50.5185650872
    West Virginia 51.4004231809
    Wisconsin 50.6148645265
    Wyoming 49.9459554265

In [1]: 
```
#### Comment:
Excellent work! Interestingly, the District of Columbia had the highest percentage of females in 2000, while Alaska had the highest percentage of males.
