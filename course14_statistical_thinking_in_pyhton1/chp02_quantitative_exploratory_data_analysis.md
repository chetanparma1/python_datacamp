# Chapter 02: Quantitative Exploratory Data Analysis

## 01. Means and medians
Which one of the following statements is true about means and medians?

### Possible Answers
* An outlier can significantly affect the value of both the mean and the median.
** press 1
* An outlier can significantly affect the value of the mean, but not the median.
** press 2
* Means and medians are in general both robust to single outliers.
** press 3
* The mean and median are equal if there is an odd number of data points.
** press 4

#### Answer:
2

#### Comment:
Correct!

## 02. Computing means
The mean of all measurements gives an indication of the typical magnitude of a measurement. It is computed using np.mean().

### Instructions:
* Compute the mean petal length of Iris versicolor from Anderson's classic data set. The variable versicolor_petal_length is provided in your namespace. Assign the mean to mean_length_vers.
* Hit submit to print the result.

#### Script:
```
# Compute the mean: mean_length_vers
mean_length_vers = np.mean(versicolor_petal_length)

# Print the result with some nice formatting
print('I. versicolor:', mean_length_vers, 'cm')
# print("I. versicolor: {} cm".format(mean_length_vers))
```
#### Output:
```
<script.py> output:
    I. versicolor: 4.26 cm
```
#### Comment:
Great work!

## 03. Computing percentiles
In this exercise, you will compute the percentiles of petal length of Iris versicolor.

### Instructions:
* Create percentiles, a NumPy array of percentiles you want to compute. These are the 2.5th, 25th, 50th, 75th, and 97.5th. You can do so by creating a list containing these ints/floats and convert the list to a NumPy array using np.array(). For example, np.array([30, 50]) would create an array consisting of the 30th and 50th percentiles.
* Use np.percentile() to compute the percentiles of the petal lengths from the Iris versicolor samples. The variable versicolor_petal_length is in your namespace.
* Print the percentiles.

#### Script:
```
# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)
```
#### Output:
```
<script.py> output:
    [3.3    4.     4.35   4.6    4.9775]
```
#### Comment:
Great work!
