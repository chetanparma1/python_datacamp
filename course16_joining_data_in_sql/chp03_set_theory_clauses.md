# Chapter 03: Set Theory Clauses

## 01. Union
Near query result to the right, you will see two new tables with names economies2010 and economies2015.

### Instructions:
* Combine these two tables into one table containing all of the fields in economies2010. The economies table is also included for reference.
* Sort this resulting single table by country code and then by year, both in ascending order.

#### Script:
```
-- Select fields from 2010 table
SELECT  *
  -- From 2010 table
  FROM economies2010
	-- Set theory clause
	UNION
-- Select fields from 2015 table
SELECT *
  -- From 2015 table
  FROM economies2015
-- Order by code and year
ORDER BY code, year;
```
#### Comment:
What a beauty!

## 02. Union (2)
UNION can also be used to determine all occurrences of a field across multiple tables. Try out this exercise with no starter code.

### Instructions:
* Determine all (non-duplicated) country codes in either the cities or the currencies table. The result should be a table with only one field called country_code.
* Sort by country_code in alphabetical order.

#### Script:
```
-- Select field
SELECT country_code 
  -- From cities
  FROM cities
	-- Set theory clause
	UNION
-- Select field
SELECT code
  -- From currencies
  FROM currencies
-- Order by country_code
ORDER BY country_code;
```
#### Comment:
Well done! Let's take it up a notch!
