# Chapter 02: Outer Joins and Cross Joins

## 01. Left Join
Now you'll explore the differences between performing an inner join and a left join using the cities and countries tables.

You'll begin by performing an inner join with the cities table on the left and the countries table on the right. Remember to alias the name of the city field as city and the name of the country field as country.

You will then change the query to a left join. Take note of how many records are in each query here!

### Instructions & Script 1:
Fill in the code based on the instructions in the code comments to complete the inner join. Note how many records are in the result of the join in the query result tab.
```
-- Select the city name (with alias), the country code,
-- the country name (with alias), the region,
-- and the city proper population
SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
-- From left table (with alias)
FROM cities AS c1
  -- Join to right table (with alias)
  INNER JOIN countries AS c2
    -- Match on country code
    ON c1.country_code = c2.code
-- Order by descending country code
ORDER BY code DESC;
```

### Instructions & Script 2
Change the code to perform a LEFT JOIN instead of an INNER JOIN. After executing this query, note how many records the query result contains.
```
SELECT c1.name AS city, code, c2.name AS country,
       region, city_proper_pop
FROM cities AS c1
  -- 1. Join right table (with alias)
  LEFT JOIN countries AS c2
    -- 2. Match on country code
    ON c1.country_code = c2.code
-- 3. Order by descending country code
ORDER BY code DESC;
```
#### Comment:
Perfect! Notice that the INNER JOIN version resulted in 230 records. The LEFT JOIN version returned 236 rows.

## 02. Left join (2)
Next, you'll try out another example comparing an inner join to its corresponding left join. Before you begin though, take note of how many records are in both the countries and languages tables below.

You will begin with an inner join on the countries table on the left with the languages table on the right. Then you'll change the code to a left join in the next bullet.

Note the use of multi-line comments here using /* and */.

### Instruction & Script 1
* Perform an inner join. Alias the name of the country field as country and the name of the language field as language.
* Sort based on descending country name.

```
/*
5. Select country name AS country, the country's local name,
the language name AS language, and
the percent of the language spoken in the country
*/
SELECT c.name AS country, local_name, l.name AS language, percent
-- 1. From left table (alias as c)
FROM countries AS c
  -- 2. Join to right table (alias as l)
  INNER JOIN languages AS l
    -- 3. Match on fields
    ON c.code = l.code
-- 4. Order by descending country
ORDER BY country DESC;
```
### Instructions & Script 2:
* Perform a left join instead of an inner join. Observe the result, and also note the change in the number of records in the result.
* Carefully review which records appear in the left join result, but not in the inner join result.

```
/*
5. Select country name AS country, the country's local name,
the language name AS language, and
the percent of the language spoken in the country
*/
SELECT c.name AS country, local_name, l.name AS language, percent
-- 1. From left table (alias as c)
FROM countries AS c
  -- 2. Join to right table (alias as l)
  LEFT JOIN languages AS l
    -- 3. Match on fields
    ON c.code = l.code
-- 4. Order by descending country
ORDER BY country DESC;
```
#### Comment:
Perfect! Notice that the INNER JOIN version resulted in 914 records. The LEFT JOIN version returned 921 rows.

## 02. Left join (3)
You'll now revisit the use of the AVG() function introduced in our Intro to SQL for Data Science course. You will use it in combination with left join to determine the average gross domestic product (GDP) per capita by region in 2010.

### Instructions & Script 1
* Begin with a left join with the countries table on the left and the economies table on the right.
* Focus only on records with 2010 as the year.
```
-- 5. Select name, region, and gdp_percapita
SELECT c.name, region, e.gdp_percapita
-- 1. From countries (alias as c)
FROM countries AS c
  -- 2. Left join with economies (alias as e)
  LEFT JOIN economies AS e
    -- 3. Match on code fields
    ON c.code = e.code
-- 4. Focus on 2010
WHERE e.year = 2010;
```

### Instruction & Script 2
* Modify your code to calculate the average GDP per capita AS avg_gdp for each region in 2010.
* Select the region and avg_gdp fields.
```
-- Select fields
SELECT c.region, AVG(e.gdp_percapita) AS avg_gdp
-- From countries (alias as c)
FROM countries AS c
  -- Left join with economies (alias as e)
  LEFT JOIN economies AS e
    -- Match on code fields
    ON c.code = e.code
-- Focus on 2010
WHERE e.year = 2010
-- Group by region
GROUP BY c.region;
```
### Instructions & Script 3:
Arrange this data on average GDP per capita for each region in 2010 from highest to lowest average GDP per capita.
```
-- Select fields
SELECT region, AVG(gdp_percapita) AS avg_gdp
-- From countries (alias as c)
FROM countries as c
  -- Left join with economies (alias as e)
  LEFT JOIN economies as e
    -- Match on code fields
    ON c.code = e.code
-- Focus on 2010
WHERE e.year = 2010
-- Group by region
GROUP BY c.region
-- Order by descending avg_gdp
order by avg_gdp desc;
```
#### Comment:
Well done. Notice how gradually you're adding more and more building blocks to your SQL vocabulary. This enables you to answer questions of ever-increasing complexity!

## 03. Right join
Right joins aren't as common as left joins. One reason why is that you can always write a right join as a left join.

### Instructions:
The left join code is commented out here. Your task is to write a new query using rights joins that produces the same result as what the query using left joins produces. Keep this left joins code commented as you write your own query just below it using right joins to solve the problem.

Note the order of the joins matters in your conversion to using right joins!

#### Script:
```
-- convert this code to use RIGHT JOINs instead of LEFT JOINs
/*
SELECT cities.name AS city, urbanarea_pop, countries.name AS country,
       indep_year, languages.name AS language, percent
FROM cities
  LEFT JOIN countries
    ON cities.country_code = countries.code
  LEFT JOIN languages
    ON countries.code = languages.code
ORDER BY city, language;
*/

SELECT cities.name AS city, urbanarea_pop, countries.name AS country,
       indep_year, languages.name AS language, percent
FROM languages
  RIGHT JOIN countries
    ON countries.code = languages.code
  RIGHT JOIN cities
    ON cities.country_code = countries.code
ORDER BY city, language;
```
#### Comment:
Correct; everything should be reversed!

## 04. Full join
In this exercise, you'll examine how your results differ when using a full join versus using a left join versus using an inner join with the countries and currencies tables.

You will focus on the North American region and also where the name of the country is missing. Dig in to see what we mean!

Begin with a full join with countries on the left and currencies on the right. The fields of interest have been SELECTed for you throughout this exercise.

Then complete a similar left join and conclude with an inner join.

### Instructions & Script 1:
Choose records in which region corresponds to North America or is NULL.

```
SELECT name AS country, code, region, basic_unit
-- 3. From countries
FROM countries
  -- 4. Join to currencies
  FULL JOIN currencies
    -- 5. Match on code
    USING (code)
-- 1. Where region is North America or null
WHERE countries.region = 'North America' OR countries.region IS NULL
-- 2. Order by region
ORDER BY countries.region;
```
### Instructions & Script 2:
Repeat the same query as above but use a LEFT JOIN instead of a FULL JOIN. Note what has changed compared to the FULL JOIN result!
```
SELECT name AS country, code, region, basic_unit
-- 1. From countries
FROM countries
  -- 2. Join to currencies
  LEFT JOIN currencies
    -- 3. Match on code
    USING (code)
-- 4. Where region is North America or null
WHERE region = 'North America' OR region IS NULL
-- 5. Order by region
ORDER BY region;
```
### Instructions & Script 3:
Repeat the same query as above but use an INNER JOIN instead of a FULL JOIN. Note what has changed compared to the FULL JOIN and LEFT JOIN results!
```
SELECT name AS country, code, region, basic_unit
FROM countries
  -- 1. Join to currencies
  INNER JOIN currencies
    USING (code)
-- 2. Where region is North America or null
WHERE region = 'North America' OR region IS NULL
-- 3. Order by region
ORDER BY region;
```
#### Comment:
Have you kept an eye out on the different numbers of records these queries returned? The FULL JOIN query returned 17 rows, the OUTER JOIN returned 4 rows, and the INNER JOIN only returned 3 rows. Do these results make sense to you?

## 05. Full join (2)
You'll now investigate a similar exercise to the last one, but this time focused on using a table with more records on the left than the right. You'll work with the languages and countries tables.

Begin with a full join with languages on the left and countries on the right. Appropriate fields have been selected for you again here.

### Instructions & Script 1:
* Choose records in which countries.name starts with the capital letter 'V' or is NULL.
* Arrange by countries.name in ascending order to more clearly see the results.
```
SELECT countries.name, code, languages.name AS language
-- 3. From languages
FROM languages
  -- 4. Join to countries
  FULL JOIN countries
    -- 5. Match on code
    USING (code)
-- 1. Where countries.name starts with V or is null
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
-- 2. Order by ascending countries.name
ORDER BY countries.name;
```
### Instructions & Script 2:
Repeat the same query as above but use a left join instead of a full join. Note what has changed compared to the full join result!
```
SELECT countries.name, code, languages.name AS language
FROM languages
  -- 1. Join to countries
  LEFT JOIN countries
    -- 2. Match using code
    USING (code)
-- 3. Where countries.name starts with V or is null
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;
```
### Instructions & Script 3:
Repeat once more, but use an inner join instead of a left join. Note what has changed compared to the full join and left join results.
```
SELECT countries.name, code, languages.name AS language
FROM languages
  -- 1. Join to countries
  INNER JOIN countries
    USING (code)
-- 2. Where countries.name starts with V or is null
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;
```
#### Comment:
Well done. Again, make sure to compare the number of records the different types of joins return and try to verify whether the results make sense.
