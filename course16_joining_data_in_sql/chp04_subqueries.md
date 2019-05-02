# Chapter 04: Subqueries

## 01. Subquery inside where
You'll now try to figure out which countries had high average life expectancies (at the country level) in 2015.

### Instructions & Script 1:
Begin by calculating the average life expectancy across all countries for 2015.
```
-- Select average life_expectancy
SELECT avg(life_expectancy)
  -- From populations
  FROM populations
-- Where year is 2015
WHERE year = 2015
```
#### Output 1:
```
avg
71.6763415481105
```

### Instructions & Script 2:
Recall that you can use SQL to do calculations for you. Suppose we wanted only records that were above 1.15 * 100 in terms of life expectancy for 2015:
```
SELECT *
  FROM populations
WHERE life_expectancy > 1.15 * 100
  AND year = 2015;
```
Select all fields from populations with records corresponding to larger than 1.15 times the average you calculated in the first task for 2015. In other words, change the 100 in the example above with a subquery.
```
-- Select fields
SELECT * FROM populations
-- Where life_expectancy is greater than
where life_expectancy > 1.15 * (
    select avg(life_expectancy) from populations where year = 2015)
  and year = 2015;
```
#### Output 2:
```
pop_id	country_code	year	fertility_rate	life_expectancy	size
21	AUS	2015	1.833	82.4512	23789800
376	CHE	2015	1.54	83.1976	8281430
356	ESP	2015	1.32	83.3805	46444000
134	FRA	2015	2.01	82.6707	66538400
170	HKG	2015	1.195	84.278	7305700
174	ISL	2015	1.93	82.861	330815
190	ITA	2015	1.37	83.4902	60730600
194	JPN	2015	1.46	83.8437	126958000
340	SGP	2015	1.24	82.5951	5535000
374	SWE	2015	1.88	82.5512	9799190
```
##### Comment:
Good work! Let's see how you do on a more high-level question in one go.

## 02. Subquery inside where (2)
Use your knowledge of subqueries in WHERE to get the urban area population for only capital cities.

### Instructions:
* Make use of the capital field in the countries table in your subquery.
* Select the city name, country code, and urban area population fields.

#### Script:
```
-- 2. Select fields
select name, country_code, urbanarea_pop
  -- 3. From cities
  from cities
-- 4. Where city name in the field of capital cities
where name IN
  -- 1. Subquery
  (select capital
   from countries)
ORDER BY urbanarea_pop DESC;
```
#### Comment:
Alright. You've got some practice on subqueries inside WHERE now. Time to see how you do when these subqueries are in the SELECT statement!

## 03. Subquery inside select
In this exercise, you'll see how some queries can be written using either a join or a subquery.

You have seen previously how to use GROUP BY with aggregate functions and an inner join to get summarized information from multiple tables.

The code given in query.sql selects the top nine countries in terms of number of cities appearing in the cities table. Recall that this corresponds to the most populous cities in the world. Your task will be to convert the commented out code to get the same result as the code shown.

### Instructions & Script 1:
Just Submit Answer here!
```
SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
    INNER JOIN countries
    ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;

/* 
SELECT ___ AS ___,
  (SELECT ___
   FROM ___
   WHERE countries.code = cities.country_code) AS cities_num
FROM ___
ORDER BY ___ ___, ___
LIMIT 9;
*/
```
### Instrutions & Script 2:
* Remove the comments around the second query and comment out the first query instead.
* Convert the GROUP BY code to use a subquery inside of SELECT, i.e. fill in the blanks to get a result that matches the one given using the GROUP BY code in the first query.
* Again, sort the result by cities_num descending and then by country ascending.
```
-- SELECT countries.name AS country, COUNT(*) AS cities_num
--   FROM cities
--     INNER JOIN countries
--     ON countries.code = cities.country_code
-- GROUP BY country
-- ORDER BY cities_num DESC, country
-- LIMIT 9;

SELECT countries.name AS country,
  (SELECT count(*) 
      FROM cities
      WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;
```
#### Output:
```
country	cities_num
China	36
India	18
Japan	11
Brazil	10
Pakistan	9
United States	9
Indonesia	7
Russian Federation	7
South Korea	7
```
#### Comment:
Great! The next video will introduce you to using subqueries in the FROM clause. Exciting stuff!

## 04. Subquery inside from
The last type of subquery you will work with is one inside of FROM.

You will use this to determine the number of languages spoken for each country, identified by the country's local name! (Note this may be different than the name field and is stored in the local_name field.)

### Instructions & Script 1:
* Begin by determining for each country code how many languages are listed in the languages table using SELECT, FROM, and GROUP BY.
* Alias the aggregated field as lang_num.
```
-- Select fields (with aliases)
select code, count(name) as lang_num
  -- From languages
  from languages
-- Group by code
group by code;
```
### Instructions & Script 2:
* Include the previous query (aliased as subquery) as a subquery in the FROM clause of a new query.
* Select the local name of the country from countries.
* Also, select lang_num from subquery.
* Make sure to use WHERE appropriately to match code in countries and in subquery.
* Sort by lang_num in descending order.
```
-- Select fields
select countries.local_name, subquery.lang_num
  -- From countries
  from countries, 
  	-- Subquery (alias as subquery)
  	(select code, count(name) as lang_num
      from languages
      group by code) AS subquery
  -- Where codes match
  WHERE countries.code = subquery.code
-- Order by descending number of languages
order by lang_num desc;
```
#### Comment:
This one wasn't easy!
