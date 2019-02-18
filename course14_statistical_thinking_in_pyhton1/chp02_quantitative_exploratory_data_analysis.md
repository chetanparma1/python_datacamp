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
