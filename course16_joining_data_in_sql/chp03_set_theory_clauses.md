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

## 08. Semi-join
You are now going to use the concept of a semi-join to identify languages spoken in the Middle East.

### Instructions & Script 1:
Flash back to our <a href="https://www.datacamp.com/courses/intro-to-sql-for-data-science">Intro to SQL for Data Science</a> course and begin by selecting all country codes in the Middle East as a single field result using SELECT, FROM, and WHERE.
```
-- Select code
SELECT code
  -- From countries
  FROM countries
-- Where region is Middle East
WHERE region = 'Middle East';
```
### Instructions & Script 2:
* Comment out the answer to the previous tab by surrounding it in /* and */. You'll come back to it!
* Below the commented code, select only unique languages by name appearing in the languages table.
* Order the resulting single field table by name in ascending order.
```
-- SELECT code
--   FROM countries
-- WHERE region = 'Middle East';

-- Select field
SELECT DISTINCT name
  -- From languages
  FROM languages
-- Order by name
ORDER BY name;
```
### Instructions & Script 3:
Now combine the previous two queries into one query:

* Add a WHERE IN statement to the SELECT DISTINCT query, and use the commented out query from the first instruction in there. That way, you can determine the unique languages spoken in the Middle East.

<br /> Carefully review this result and its code after completing it. It serves as a great example of subqueries, which are the focus of Chapter 4.

```
SELECT DISTINCT name
  FROM languages
  WHERE code IN (
    SELECT code FROM countries WHERE region = 'Middle East')
ORDER BY name;
```
#### Comment:
Your first subquery is a fact! Let's dive a little deeper into the concept.

## 09. Relating semi-join to a tweaked inner join
Let's revisit the code from the previous exercise, which retrieves languages spoken in the Middle East.
```
SELECT DISTINCT name
FROM languages
WHERE code IN
  (SELECT code
   FROM countries
   WHERE region = 'Middle East')
ORDER BY name;
```
Sometimes problems solved with semi-joins can also be solved using an inner join.
```
SELECT languages.name AS language
FROM languages
INNER JOIN countries
ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;
```
This inner join isn't quite right. What is missing from this second code block to get it to match with the correct answer produced by the first block?

### Possible Answers
* HAVING instead of WHERE
* DISTINCT
* UNIQUE

#### Answer:
2

#### Comment:
Correct! There's no use on retrieving 'Arabic' multiple times; you only care about DISTINCT languages here.

## 10. Diagnosing problems using anti-join
Another powerful join in SQL is the anti-join. It is particularly useful in identifying which records are causing an incorrect number of records to appear in join queries.

You will also see another example of a subquery here, as you saw in the first exercise on semi-joins. Your goal is to identify the currencies used in Oceanian countries!

### Instruction & Script 1:
Begin by determining the number of countries in countries that are listed in Oceania using SELECT, FROM, and WHERE.

```
-- Select statement
select count(code)
  -- From countries
  from countries
-- Where continent is Oceania
where continent = 'Oceania';
```
### Instruction & Script 2:
* Complete an inner join with countries AS c1 on the left and currencies AS c2 on the right to get the different currencies used in the countries of Oceania.
* Match ON the code field in the two tables.
* Include the country code, country name, and basic_unit AS currency.
Observe query result and make note of how many different countries are listed here.

```
-- 5. Select fields (with aliases)
SELECT c1.code, c1.name, c2.basic_unit as currency 
  -- 1. From countries (alias as c1)
  FROM countries as c1
  	-- 2. Join with currencies (alias as c2)
  	INNER JOIN currencies as c2
    -- 3. Match on code
    on c1.code = c2.code
-- 4. Where continent is Oceania
where continent = 'Oceania';
```
### Instruction & Script 3:
Note that not all countries in Oceania were listed in the resulting inner join with currencies. Use an anti-join to determine which countries were not included!

* Use NOT IN and (SELECT code FROM currencies) as a subquery to get the country code and country name for the Oceanian countries that are not included in the currencies table.
```
SELECT code, name FROM countries
  WHERE continent = 'Oceania' 
  AND code not in (SELECT code from currencies);
```
#### Output:
code	name
ASM	American Samoa
FJI	Fiji Islands
GUM	Guam
FSM	Micronesia, Federated States of
MNP	Northern Mariana Islands

#### Comment:
Nice! Can you tell which countries were not included now?

## 11. Set theory challenge
Congratulations! You've now made your way to the challenge problem for this third chapter. Your task here will be to incorporate two of UNION/UNION ALL/INTERSECT/EXCEPT to solve a challenge involving three tables.

In addition, you will use a subquery as you have in the last two exercises! This will be great practice as you hop into subqueries more in Chapter 4!

### Instructions:
* Identify the country codes that are included in either economies or currencies but not in populations.
* Use that result to determine the names of cities in the countries that match the specification in the previous instruction.

#### Script:
```
-- Select the city name
SELECT c1.name
  -- Alias the table where city name resides
  from cities AS c1
  -- Choose only records matching the result of multiple set theory clauses
  WHERE c1.country_code IN
(
    -- Select appropriate field from economies AS e
    SELECT e.code
    FROM economies AS e
    -- Get all additional (unique) values of the field from currencies AS c2  
    UNION
    SELECT c2.code
    FROM currencies AS c2
    -- Exclude those appearing in populations AS p
    EXCEPT
    SELECT p.country_code
    FROM populations AS p
);
```
#### Comment:
Success! Head over to the final chapter of this course to feel the power of subqueries at your fingertips!
