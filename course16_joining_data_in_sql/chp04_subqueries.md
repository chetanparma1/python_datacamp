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

## 05. Advanced subquery
You can also nest multiple subqueries to answer even more specific questions.

In this exercise, for each of the six continents listed in 2015, you'll identify which country had the maximum inflation rate (and how high it was) using multiple subqueries. The table result of your query in Task 3 should look something like the following, where anything between < > will be filled in with appropriate values:
```
+------------+---------------+-------------------+
| name       | continent     | inflation_rate    |
|------------+---------------+-------------------|
| <country1> | North America | <max_inflation1>  |
| <country2> | Africa        | <max_inflation2>  |
| <country3> | Oceania       | <max_inflation3>  |
| <country4> | Europe        | <max_inflation4>  |
| <country5> | South America | <max_inflation5>  |
| <country6> | Asia          | <max_inflation6>  |
+------------+---------------+-------------------+
```
Again, there are multiple ways to get to this solution using only joins, but the focus here is on showing you an introduction into advanced subqueries.

### Instructions & Script 1:
* Create an inner join with countries on the left and economies on the right with USING. Do not alias your tables or columns.
* Retrieve the country name, continent, and inflation rate for 2015.
```
-- Select fields
select countries.name, countries.continent, economies.inflation_rate
  -- From countries
  from countries
  	-- Join to economies
  	inner join economies
    -- Match on code
    using(code) 
-- Where year is 2015
where year = 2015;
```
### Instructions & Script 2:
* Determine the maximum inflation rate for each continent in 2015 using the previous query as a subquery called subquery in the FROM clause.
* Select the maximum inflation rate AS max_inf grouped by continent.
This will result in the six maximum inflation rates in 2015 for the six continents as one field table. (Don't include continent in the outer SELECT statement.)
```
-- Select fields
select max(inflation_rate) as max_inf
  -- Subquery using FROM (alias as subquery)
  FROM (
      select name, continent, inflation_rate
      -- From countries
      from countries
      	-- Join to economies
      	inner join economies
        -- Match on code
        using(code) 
    -- Where year is 2015
    where year = 2015) AS subquery
-- Group by continent
group by continent;
```
### Instructions & Script 3:
* Append the second part's query to the first part's query using WHERE, AND, and IN to obtain the name of the country, its continent, and the maximum inflation rate for each continent in 2015. Revisit the sample output in the assignment text at the beginning of the exercise to see how this matches up.
* For the sake of practice, change all joining conditions to use ON instead of USING.

This code works since each of the six maximum inflation rate values occur only once in the 2015 data. Think about whether this particular code involving subqueries would work in cases where there are ties for the maximum inflation rate values.

```
-- Select fields
select c.name, c.continent, e.inflation_rate
  -- From countries
  from countries c
  	-- Join to economies
  	inner join economies e
    -- Match on code
    on c.code = e.code
-- Where year is 2015
where e.year = 2015 AND e.inflation_rate IN (
    select max(inflation_rate) as max_inf
      -- Subquery using FROM (alias as subquery)
      FROM (
          select name, continent, inflation_rate
          -- From countries
          from countries
          	-- Join to economies
          	inner join economies
            -- Match on code
            using(code) 
        -- Where year is 2015
        where year = 2015) AS subquery
    -- Group by continent
    group by continent
    );
```
```
name	continent	inflation_rate
Haiti	North America	7.524
Malawi	Africa	21.858
Nauru	Oceania	9.784
Ukraine	Europe	48.684
Venezuela	South America	121.738
Yemen	Asia	39.403
```
#### Comment:
Wow! Take a step back and look back at what you did!

## 06. Subquery challenge
Let's test your understanding of the subqueries with a challenge problem! Use a subquery to get 2015 economic data for countries that do not have

* gov_form of 'Constitutional Monarchy' or
* 'Republic' in their gov_form.
Here, gov_form stands for the form of the government for each country. Review the different entries for gov_form in the countries table.

### Instructions:
* Select the country code, inflation rate, and unemployment rate.
* Order by inflation rate ascending.
* Do not use table aliasing in this exercise.

#### Script:
```
-- Select fields
SELECT e.code, e.inflation_rate, e.unemployment_rate
  -- From economies
  FROM economies e
  -- Where year is 2015 and code is not in
  WHERE year = 2015 AND code NOT IN
  	-- Subquery
  	(SELECT c.code
  	 FROM countries c
  	 WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic%'))
-- Order by inflation rate
ORDER BY e.inflation_rate;
```
#### Comment:
Superb! Let's review subqueries before you head off to the last video of this course!

## 07. Subquery review
Within which SQL clause are subqueries most frequently found?

### Possible Answers
* WHERE --> press 1
* FROM --> press 2
* SELECT --> press 3
* IN --> press 4

#### Answer:
1

#### Comment:
Correct!

## 07. Final challenge
Welcome to the end of the course! The next three exercises will test your knowledge of the content covered in this course and apply many of the ideas you've seen to difficult problems. Good luck!

Read carefully over the instructions and solve them step-by-step, thinking about how the different clauses work together.

In this exercise, you'll need to get the country names and other 2015 data in the economies table and the countries table for Central American countries with an official language.

### Instructions:
* Select unique country names. Also select the total investment and imports fields.
* Use a left join with countries on the left. (An inner join would also work, but please use a left join here.)
* Match on code in the two tables AND use a subquery inside of ON to choose the appropriate languages records.
* Order by country name ascending.
* Use table aliasing but not field aliasing in this exercise.

#### Script:
```
-- Select fields
SELECT DISTINCT c.name, e.total_investment, e.imports
  -- From table (with alias)
  FROM countries AS c
    -- Join with table (with alias)
    LEFT JOIN economies AS e
      -- Match on code
      ON (c.code = e.code
      -- and code in Subquery
        AND c.code IN (
          SELECT l.code
          FROM languages AS l
          WHERE official = 'true'
        ) )
  -- Where region and year are correct
  WHERE region = 'Central America' AND year = 2015
-- Order by field
ORDER BY c.name;
```
#### Output:
```
name	total_investment	imports
Belize	22.014	6.743
Costa Rica	20.218	4.629
El Salvador	13.983	8.193
Guatemala	13.433	15.124
Honduras	24.633	9.353
Nicaragua	31.862	11.665
Panama	46.557	5.898
```
#### Comment:
One down, two to go!

## 08. Final challenge (2)
Whoofta! That was challenging, huh?

Let's ease up a bit and calculate the average fertility rate for each region in 2015.

### Instructions:
* Include the name of region, its continent, and average fertility rate aliased as avg_fert_rate.
* Sort based on avg_fert_rate ascending.
* Remember that you'll need to GROUP BY all fields that aren't included in the aggregate function of SELECT.

#### Script:
```
-- Select fields
SELECT c.region, c.continent, avg(p.fertility_rate) AS avg_fert_rate
  -- From left table
  FROM countries AS c
    -- Join to right table
    INNER JOIN populations AS p
      -- Match on join condition
      ON c.code = p.country_code
  -- Where specific records matching some condition
  WHERE year = 2015
-- Group appropriately
GROUP BY c.region, c.continent
-- Order appropriately
ORDER BY avg_fert_rate;
```
#### Output:
```
region	continent	avg_fert_rate
Southern Europe	Europe	1.42610000371933
Eastern Europe	Europe	1.49088890022702
Baltic Countries	Europe	1.60333331425985
Eastern Asia	Asia	1.62071430683136
Western Europe	Europe	1.6325000077486
North America	North America	1.76575002074242
British Islands	Europe	1.875
Nordic Countries	Europe	1.89333335558573
Australia and New Zealand	Oceania	1.91149997711182
Caribbean	North America	1.95057143483843
Southeast Asia	Asia	2.15600001811981
South America	South America	2.27475001414617
Central America	North America	2.32637499272823
Middle East	Asia	2.54705556895998
Southern and Central Asia	Asia	2.63414285864149
Micronesia	Oceania	2.86475002765656
Northern Africa	Africa	2.9081666469574
Southern Africa	Africa	2.99079999923706
Melanesia	Oceania	3.13579998016357
Polynesia	Oceania	3.24433326721191
Eastern Africa	Africa	4.38670586838442
Western Africa	Africa	4.96012498438358
Central Africa	Africa	4.96788883209229
```
#### Comment:
Interesting. It seems that the average fertility rate is lowest in Southern Europe and highest in Central Africa. Two down, one to go!
