# Chapter 01: Introduction to Inner Join

## 01. Inner join
PostgreSQL was mentioned in the slides but you'll find that these joins and the material here applies to different forms of SQL as well.

Throughout this course, you'll be working with the countries database containing information about the most populous world cities as well as country-level economic data, population data, and geographic data. This countries database also contains information on languages spoken in each country.

You can see the different tables in this database by clicking on the tabs on the bottom right below query.sql. Click through them to get a sense for the types of data that each table contains before you continue with the course! Take note of the fields that appear to be shared across the tables.

Recall from the video the basic syntax for an INNER JOIN, here including all columns in both tables:
```
SELECT *
FROM left_table
INNER JOIN right_table
ON left_table.id = right_table.id;
```
You'll start off with a SELECT statement and then build up to an inner join with the cities and countries tables. Let's get to it!

### Instructions & Script 1:
Begin by selecting all columns from the cities table.
 
```
-- Select all columns from cities
SELECT * FROM cities
```
### Instructions & Script 2:
* Inner join the cities table on the left to the countries table on the right, keeping all of the fields in both tables.
* You should match the tables on the country_code field in cities and the code field in countries.
* Do not alias your tables here or in the next step. Using cities and countries is fine for now.

```
SELECT * 
FROM cities
  -- 1. Inner join to countries
  INNER JOIN countries
    -- 2. Match on the country codes
    ON cities.country_code = countries.code;
```
### Instructions & Script 3:
* Modify the SELECT statement to keep only the name of the city, the name of the country, and the name of the region the country resides in.
* Recall from our Intro to SQL for Data Science course that you can alias fields using AS. Alias the name of the city AS city and the name of the country AS country.

```
SELECT cities.name as city,  countries.name as country, countries.region
FROM cities
  -- 1. Inner join to countries
  INNER JOIN countries
    -- 2. Match on the country codes
    ON cities.country_code = countries.code;
```
#### Comment:
Great work! In the next exercise you'll explore how you can do more aliasing to limit the amount of writing.

## 02. Inner join (2)
Instead of writing the full table name, you can use table aliasing as a shortcut. For tables you also use AS to add the alias immediately after the table name with a space. Check out the aliasing of cities and countries below.
```
SELECT c1.name AS city, c2.name AS country
FROM cities AS c1
INNER JOIN countries AS c2
ON c1.country_code = c2.code;
```
Notice that to select a field in your query that appears in multiple tables, you'll need to identify which table/table alias you're referring to by using a . in your SELECT statement.

You'll now explore a way to get data from both the countries and economies tables to examine the inflation rate for both 2010 and 2015.

Sometimes it's easier to write SQL code out of order: you write the SELECT statement after you've done the JOIN.

### Instructions:
* Join the tables countries (left) and economies (right) aliasing countries AS c and economies AS e.
* Specify the field to match the tables ON.
* From this join, SELECT:
** c.code, aliased as country_code.
** name, year, and inflation_rate, not aliased.

#### Script:
```
-- 3. Select fields with aliases
SELECT c.code AS country_code, c.name, e.year, e.inflation_rate
FROM countries AS c
  -- 1. Join to economies (alias e)
  INNER JOIN economies AS e
    -- 2. Match on code
    ON c.code = e.code;
```
#### Comment:
Nicely done! Using this short aliases takes some getting used to, but it will save you a lot of typing.

## 03. Inner join (3)
The ability to combine multiple joins in a single query is a powerful feature of SQL, e.g:
```
SELECT *
FROM left_table
  INNER JOIN right_table
    ON left_table.id = right_table.id
  INNER JOIN another_table
    ON left_table.id = another_table.id;
```
As you can see here it becomes tedious to continually write long table names in joins. This is when it becomes useful to alias each table using the first letter of its name (e.g. countries AS c)! It is standard practice to alias in this way and, if you choose to alias tables or are asked to specifically for an exercise in this course, you should follow this protocol.

Now, for each country, you want to get the country name, its region, and the fertility rate and unemployment rate for both 2010 and 2015.

Note that results should work throughout this course with or without table aliasing unless specified differently.

### Instructions & Script 1
* Inner join countries (left) and populations (right) on the code and country_code fields respectively.
* Alias countries AS c and populations AS p.
* Select code, name, and region from countries and also select year and fertility_rate from populations (5 fields in total).

```
-- 4. Select fields
SELECT c.code, c.name, c.region, p.year, p.fertility_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join with populations (as p)
  INNER JOIN populations  AS p
    -- 3. Match on country code
    ON c.code = p.country_code
```
### Instructions & Script 2
* Add an additional inner join with economies to your previous query by joining on code.
* Include the unemployment_rate column that became available through joining with economies.
* Note that year appears in both populations and economies, so you have to explicitly use e.year instead of year as you did before.

```
-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, e.unemployment_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to populations (as p)
  INNER JOIN populations AS p
    -- 3. Match on country code
    ON c.code = p.country_code
  -- 4. Join to economies (as e)
  INNER JOIN economies AS e
    -- 5. Match on country code
    ON c.code = e.code;
```
### Instructions & Script 3:
* Scroll down the query result and take a look at the results for Albania from your previous query. Does something seem off to you?
* The trouble with doing your last join on c.code = e.code and not also including year is that e.g. the 2010 value for fertility_rate is also paired with the 2015 value for unemployment_rate.
* Fix your previous query: in your last ON clause, use AND to add an additional joining condition. In addition to joining on code in c and e, also join on year in e and p.
```
-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, e.unemployment_rate
  -- 1. From countries (alias as c)
  FROM countries AS c
  -- 2. Join to populations (as p)
  INNER JOIN populations AS p
    -- 3. Match on country code
    ON c.code = p.country_code
  -- 4. Join to economies (as e)
  INNER JOIN economies AS e
    -- 5. Match on country code
    ON c.code = e.code AND e.year = p.year;
```
#### Comment:
Good work! Time to learn something new!

## 04. Review inner join using on
Why does the following code result in an error?
```
SELECT c.name AS country, l.name AS language
FROM countries AS c
  INNER JOIN languages AS l;
```
### Possible Answers
* The languages table has more rows than the countries table.
* There are multiple languages spoken in many countries.
* INNER JOIN requires a specification of the key field (or fields) in each table.
* Join queries may not be followed by a semi-colon.

#### Answer:
3

#### Comment:
Correct!

## 05. Inner join with using
When joining tables with a common field name, e.g.
```
SELECT *
FROM countries
  INNER JOIN economies
    ON countries.code = economies.code
```
You can use USING as a shortcut:

```
SELECT *
FROM countries
  INNER JOIN economies
    USING(code)
```
You'll now explore how this can be done with the countries and languages tables.

### Instructions:
* Inner join countries on the left and languages on the right with USING(code).
* Select the fields corresponding to:
** country name AS country,
** continent name,
** language name AS language, and
** whether or not the language is official.
Remember to alias your tables using the first letter of their names.

#### Script:
```
-- 4. Select fields
SELECT c.name AS country, c.continent, l.name as language, l.official
  -- 1. From countries (alias as c)
  FROM countries as c
  -- 2. Join to languages (as l)
  INNER JOIN languages as l
    -- 3. Match using code
    on c.code = l.code;
```
#### Comment:
Well done! Another technique to save you some typing!

## 06. Self-join
In this exercise, you'll use the populations table to perform a self-join to calculate the percentage increase in population from 2010 to 2015 for each country code!

Since you'll be joining the populations table to itself, you can alias populations as p1 and also populations as p2. This is good practice whenever you are aliasing and your tables have the same first letter. Note that you are required to alias the tables with self-joins.

### Instructions & Script 1:
* Join populations with itself ON country_code.
* Select the country_code from p1 and the size field from both p1 and p2. SQL won't allow same-named fields, so alias p1.size as size2010 and p2.size as size2015.

```
-- 4. Select fields with aliases
SELECT p1.country_code, p1.size as size2010, p2.size as size2015 
-- 1. From populations (alias as p1)
    FROM populations as p1
    -- 2. Join to itself (alias as p2)
    INNER JOIN populations p2
    -- 3. Match on country code
    ON p1.country_code = p2.country_code
```
### Instructions & Script 2:
Notice from the result that for each country_code you have four entries laying out all combinations of 2010 and 2015.

* Extend the ON in your query to include only those records where the p1.year (2010) matches with p2.year - 5 (2015 - 5 = 2010). This will omit the three entries per country_code that you aren't interested in.

```
-- 5. Select fields with aliases
SELECT p1.country_code,
       p1.size AS size2010,
       p2.size AS size2015
-- 1. From populations (alias as p1)
FROM populations as p1
  -- 2. Join to itself (alias as p2)
  INNER JOIN populations as p2
    -- 3. Match on country code
    ON p1.country_code = p2.country_code
        -- 4. and year (with calculation)
        AND p1.year = p2.year - 5
```
### Instructions & Script 3
As you just saw, you can also use SQL to calculate values like p2.year - 5 for you. With two fields like size2010 and size2015, you may want to determine the percentage increase from one field to the next:

With two numeric fields A and B, the percentage growth from A to B can be calculated as (B−A)/A∗100.0.

Add a new field to SELECT, aliased as growth_perc, that calculates the percentage population growth from 2010 to 2015 for each country, using p2.size and p1.size
```
SELECT p1.country_code,
       p1.size AS size2010, 
       p2.size AS size2015,
       -- 1. calculate growth_perc
       ((p2.size - p1.size)/p1.size * 100.0) AS growth_perc
-- 2. From populations (alias as p1)
FROM populations AS p1
  -- 3. Join to itself (alias as p2)
  INNER JOIN populations AS p2
    -- 4. Match on country code
    ON p1.country_code = p2.country_code
        -- 5. and year (with calculation)
        AND p1.year = p2.year - 5;
```
#### Comment:
Nice!

## 07. Case when and then
Often it's useful to look at a numerical field not as raw data, but instead as being in different categories or groups.

You can use CASE with WHEN, THEN, ELSE, and END to define a new grouping field.

### Instructions:
Using the countries table, create a new field AS geosize_group that groups the countries into three groups:

* If surface_area is greater than 2 million, geosize_group is 'large'.
* If surface_area is greater than 350 thousand but not larger than 2 million, geosize_group is 'medium'.
* Otherwise, geosize_group is 'small'.

#### Script:
```
SELECT name, continent, code, surface_area,
    -- 1. First case
    CASE WHEN surface_area > 2000000 THEN 'large'
        -- 2. Second case
        WHEN surface_area > 350000 THEN 'medium'
        -- 3. Else clause + end
        ELSE 'small' END
        -- 4. Alias name
        AS geosize_group
-- 5. From table
FROM countries;
```
#### Comment:
Well done! Time for the last exercise of this chapter!
