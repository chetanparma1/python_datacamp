# Chapter 02: Exploratory Data Analysis

## 01. pandas line plots
In the previous chapter, you saw that the .plot() method will place the Index values on the x-axis by default. In this exercise, you'll practice making line plots with specific columns on the x and y axes.

You will work with a dataset consisting of monthly stock prices in 2015 for AAPL, GOOG, and IBM. The stock prices were obtained from Yahoo Finance. Your job is to plot the 'Month' column on the x-axis and the AAPL and IBM prices on the y-axis using a list of column names.

All necessary modules have been imported for you, and the DataFrame is available in the workspace as df. Explore it using methods such as .head(), .info(), and .describe() to see the column names.

### Instructions:
* Create a list of y-axis column names called y_columns consisting of 'AAPL' and 'IBM'.
* Generate a line plot with x='Month' and y=y_columns as inputs.
* Give the plot a title of 'Monthly stock prices'.
* Specify the y-axis label.
* Display the plot.

#### Script
```
# Create a list of y-axis column names: y_columns
y_columns = ['AAPL', 'IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()
```
##### Output:
![Alt text](./monthly_stock_prices.svg)

##### Comment:
Wonderful work! It looks like the monthly stock prices of both AAPL and IBM peaked early in the year before falling.

## 02. pandas scatter plots
Pandas scatter plots are generated using the kind='scatter' keyword argument. Scatter plots require that the x and y columns be chosen by specifying the x and y parameters inside .plot(). Scatter plots also take an s keyword argument to provide the radius of each circle to plot in pixels.

In this exercise, you're going to plot fuel efficiency (miles-per-gallon) versus horse-power for 392 automobiles manufactured from 1970 to 1982 from the UCI Machine Learning Repository.

The size of each circle is provided as a NumPy array called sizes. This array contains the normalized 'weight' of each automobile in the dataset.

All necessary modules have been imported and the DataFrame is available in the workspace as df.

### Instructions:
* Generate a scatter plot with 'hp' on the x-axis and 'mpg' on the y-axis. Specify s=sizes.
* Add a title to the plot.
* Specify the x-axis and y-axis labels.

#### Script:
```
# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg', s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()
```
##### Output:
![Alt text](./fuel_horse.svg)

##### Comment:
Fantastic! As you would expect, automobiles with higher horsepower are less fuel efficient.

## 03. pandas box plots
While pandas can plot multiple columns of data in a single figure, making plots that share the same x and y axes, there are cases where two columns cannot be plotted together because their units do not match. The .plot() method can generate subplots for each column being plotted. Here, each plot will be scaled independently.

In this exercise your job is to generate box plots for fuel efficiency (mpg) and weight from the automobiles data set. To do this in a single figure, you'll specify subplots=True inside .plot() to generate two separate plots.

All necessary modules have been imported and the automobiles dataset is available in the workspace as df.

### Instructions:
* Make a list called cols of the column names to be plotted: 'weight' and 'mpg'.
* Call plot on df[cols] to generate a box plot of the two columns in a single figure. To do this, specify subplots=True.

#### Script
```
# Make a list of the column names to be plotted: cols
cols = ['weight', 'mpg']

# Generate the box plots
df[cols].plot(kind='box', subplots=True)

# Display the plot
plt.show()
```
##### Output:
![Alt text](./weight_mpg.svg)

##### Comment:
Excellent job! Box plots are a great way to visualize important summary statistics..

## 04. pandas hist, pdf and cdf
Pandas relies on the .hist() method to not only generate histograms, but also plots of probability density functions (PDFs) and cumulative density functions (CDFs).

In this exercise, you will work with a dataset consisting of restaurant bills that includes the amount customers tipped.

The original dataset is provided by the Seaborn package.

Your job is to plot a PDF and CDF for the fraction column of the tips dataset. This column contains information about what fraction of the total bill is comprised of the tip.

Remember, when plotting the PDF, you need to specify normed=True in your call to .hist(), and when plotting the CDF, you need to specify cumulative=True in addition to normed=True.

All necessary modules have been imported and the tips dataset is available in the workspace as df. Also, some formatting code has been written so that the plots you generate will appear on separate rows.

### Instructions:
* Plot a PDF for the values in fraction with 30 bins between 0 and 30%. The range has been taken care of for you. ax=axes[0] means that this plot will appear in the first row.
* Plot a CDF for the values in fraction with 30 bins between 0 and 30%. Again, the range has been specified for you. To make the CDF appear on the second row, you need to specify ax=axes[1].

#### Script:
```
# This formats the plots such that they appear on separate rows
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plot the PDF
df.fraction.plot(ax=axes[0], kind ='hist', bins=30, normed=True, range=(0,.3))
plt.show()

# Plot the CDF
df.fraction.plot(ax=axes[1], kind='hist', bins=30, normed=True, cumulative=True, range=(0,.3))
plt.show()
```
##### Output:
![Alt text](./hist_pdf_cdf.svg)

##### Comment:
Well done!

## 05. Fuel efficiency
From the automobiles data set, which value corresponds to the median value of the 'mpg' column? Your job is to select the 'mpg' column and call the .median() method on it. The automobile DataFrame has been provided as df.

### Possible Answers
* 29.0  &emsp;&emsp  press 1
* 23.45 &emsp;&emsp  press 2
* 22.75 &emsp;&emsp  press 3
* 32    &emsp;&emsp  press 4

#### Script:
```
In [1]: df.mpg.median()
Out[1]: 22.75
```

##### Answer:
3

##### Comment:
Exactly - great work! The median is a very useful statistic, especially in the presence of outliers, when it is more robust than the mean.

## 06. Bachelor's degrees awarded to women
In this exercise, you will investigate statistics of the percentage of Bachelor's degrees awarded to women from 1970 to 2011. Data is recorded every year for 17 different fields. This data set was obtained from the Digest of Education Statistics.

Your job is to compute the minimum and maximum values of the 'Engineering' column and generate a line plot of the mean value of all 17 academic fields per year. To perform this step, you'll use the .mean() method with the keyword argument axis='columns'. This computes the mean across all columns per row.

The DataFrame has been pre-loaded for you as df with the index set to 'Year'.

### Instructions:
* Print the minimum value of the 'Engineering' column.
* Print the maximum value of the 'Engineering' column.
* Construct the mean percentage per year with .mean(axis='columns'). Assign the result to mean.
* Plot the average percentage per year. Since 'Year' is the index of df, it will appear on the x-axis of the plot. No keyword arguments are needed in your call to .plot().

#### Script:
```
# Print the minimum value of the Engineering column
print(df.Engineering.min())

# Print the maximum value of the Engineering column
print(df.Engineering.max())

# Construct the mean percentage per year: mean
mean = df.mean(axis='columns')

# Plot the average percentage per year
# the result will be the same with if we use plt.plot(mean) instead
mean.plot()

# Display the plot
plt.show()
```
##### Output:
![Alt text](./output.svg)

```
<script.py> output:
    0.8
    19.0
```
##### Comment:
Well done! It looks like there has generally been an upward trend since 1970.

## 07. Median vs mean
In many data sets, there can be large differences in the mean and median value due to the presence of outliers.

In this exercise, you'll investigate the mean, median, and max fare prices paid by passengers on the Titanic and generate a box plot of the fare prices. This data set was obtained from <a href="http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.html">Vanderbilt University </a>.
 
All necessary modules have been imported and the DataFrame is available in the workspace as df. 

### Instructions
* Print summary statistics of the 'fare' column of df with .describe() and print(). Note: df.fare and df['fare'] are equivalent.
* Generate a box plot of the 'fare' column.

#### Script
```
# Print summary statistics of the fare column with .describe()
print(df.fare.describe())

# Generate a box plot of the fare column
df.fare.plot(kind='box')

# Show the plot
plt.show()
```
##### Output:
![Alt text](./fare_boxplot.svg)

```
<script.py> output:
    count    1308.000000
    mean       33.295479
    std        51.758668
    min         0.000000
    25%         7.895800
    50%        14.454200
    75%        31.275000
    max       512.329200
    Name: fare, dtype: float64
```
##### Comment:
Excellent job! Here you can see why the median is a more informative statistic in the presence of outliers.

## 08. Quantiles
In this exercise, you'll investigate the probabilities of life expectancy in countries around the world. This dataset contains life expectancy for persons born each year from 1800 to 2015. Since country names change or results are not reported, not every country has values. This dataset was obtained from <a href="https://docs.google.com/a/continuum.io/spreadsheets/d/1dgOdlUEq6_V55OHZCxz5BG_0uoghJTeA6f83br5peNs/pub?range=A1:D70&gid=1&output=html#">Gapminder</a>.

First, you will determine the number of countries reported in 2015. There are a total of 260 unique countries in the entire dataset. Then, you will compute the 5th and 95th percentiles of life expectancy over the entire dataset. Finally, you will make a box plot of life expectancy every 50 years from 1800 to 2000. Notice the large change in the distributions over this period.

The dataset has been pre-loaded into a DataFrame called df.

### Instructions
* Print the number of countries reported in 2015. To do this, use the .count() method on the '2015' column of df.
* Print the 5th and 95th percentiles of df. To do this, use the .quantile() method with the list [0.05, 0.95].
* Generate a box plot using the list of columns provided in years. This has already been done for you, so click on 'Submit Answer' to view the result!

#### Script
```
# Print the number of countries reported in 2015
print(df['2015'].count())

# Print the 5th and 95th percentiles
print(df.quantile([0.05, 0.95]))

# Generate a box plot
years = ['1800','1850','1900','1950','2000']
df[years].plot(kind='box')
plt.show()
```
##### Output:
![Alt text](./quantile_boxplot.svg)

```
<script.py> output:
    208
          Unnamed: 0   ...        2016
    0.05       12.95   ...     59.2555
    0.95      246.05   ...     82.1650
    
    [2 rows x 218 columns]
```
##### Comment:
Fantastic work! It looks like overall, life expectancy has steadily increased since 1900.

## 09. Filtering and counting
How many automobiles were manufactured in Asia in the automobile dataset? The DataFrame has been provided for you as df. Use filtering and the .count() member method to determine the number of rows where the 'origin' column has the value 'Asia'.

As an example, you can extract the rows that contain 'US' as the country of origin using df[df['origin'] == 'US'].
