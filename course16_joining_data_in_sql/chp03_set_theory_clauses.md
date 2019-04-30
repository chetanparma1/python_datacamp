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

## 03. Union all
As you saw, duplicates were removed from the previous two exercises by using UNION.

To include duplicates, you can use UNION ALL.

### Instructions:
* Determine all combinations (include duplicates) of country code and year that exist in either the economies or the populations tables. Order by code then year.
* The result of the query should only have two columns/fields. Think about how many records this query should result in.
* You'll use code very similar to this in your next exercise after the video. Make note of this code after completing it.

#### Script:
```
-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	UNION ALL
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code, year
ORDER BY code, year;
```
#### Comment:
Can you spot some duplicates in the query result?

## 04. Intersect
Repeat the previous UNION ALL exercise, this time looking at the records in common for country code and year for the economies and populations tables.

### Instructions:
* Again, order by code and then by year, both in ascending order.
* Note the number of records here (given at the bottom of query result) compared to the similar UNION ALL query result (814 records).

```
-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code and year
ORDER BY code, year;
```
#### Comment:
Boom!

## 05. Intersect (2)
As you think about major world cities and their corresponding country, you may ask which countries also have a city with the same name as their country name?

### Instructions:
Use INTERSECT to answer this question with countries and cities!

#### Script:
```
-- Select fields
SELECT name
  -- From countries
  FROM countries
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT name
  -- From cities
  FROM cities;
```
#### Comment:
Nice one! Hong Kong is part of China, but it appears separately here because it has its own ISO country code. Depending upon your analysis, treating Hong Kong separately could be useful or a mistake. Always check your dataset closely before you perform an analysis!

## 06. Except
Get the names of cities in cities which are not noted as capital cities in countries as a single field result.

Note that there are some countries in the world that are not included in the countries table, which will result in some cities not being labeled as capital cities when in fact they are.

### Instructions:
* Order the resulting field in ascending order.
* Can you spot the city/cities that are actually capital cities which this query misses?

#### Script:
```
-- Select field
SELECT name
  -- From cities
  FROM cities
	-- Set theory clause
	EXCEPT
-- Select field
SELECT capital
  -- From countries
  FROM countries
-- Order by result
ORDER BY name;
```
#### Comment:
EXCEPTional!

## 07.Except (2)
Now you will complete the previous query in reverse!

Determine the names of capital cities that are not listed in the cities table.

### Instructions:
* Order by capital in ascending order.
* The cities table contains information about 236 of the world's most populous cities. The result of your query may surprise you in terms of the number of capital cities that DO NOT appear in this list!

#### Script:
```
-- Select field
SELECT capital
  -- From countries
  from countries
	-- Set theory clause
	EXCEPT
-- Select field
SELECT name
  -- From cities
  from cities
-- Order by ascending capital
order by capital;
```
#### Comment:
Well done. Is this query surprising, as the instructions suggested?
