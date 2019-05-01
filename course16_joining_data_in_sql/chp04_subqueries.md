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
