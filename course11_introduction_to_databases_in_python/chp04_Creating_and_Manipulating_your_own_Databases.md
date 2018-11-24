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
