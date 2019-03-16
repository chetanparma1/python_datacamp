# Chapter 03: Introduction to Hypothesis Testing

## 01. Generating a permutation sample
In the video, you learned that permutation sampling is a great way to simulate the hypothesis that two variables have identical probability distributions. This is often a hypothesis you want to test, so in this exercise, you will write a function to generate a permutation sample from two data sets.

Remember, a permutation sample of two arrays having respectively n1 and n2 entries is constructed by concatenating the arrays together, scrambling the contents of the concatenated array, and then taking the first n1 entries as the permutation sample of the first array and the last n2 entries as the permutation sample of the second array.

### Instructions:
* Concatenate the two input arrays into one using np.concatenate(). Be sure to pass in data1 and data2 as one argument (data1, data2).
* Use np.random.permutation() to permute the concatenated array.
* Store the first len(data1) entries of permuted_data as perm_sample_1 and the last len(data2) entries of permuted_data as perm_sample_2. In practice, this can be achieved by using :len(data1) and len(data1): to slice permuted_data.
* Return perm_sample_1 and perm_sample_2.

#### Script:
```
def permutation_sample(data1, data2):
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate([data1, data2])

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2
```
#### Comment:
Great work!

## 02. Visualizing permutation sampling
To help see how permutation sampling works, in this exercise you will generate permutation samples and look at them graphically.

We will use the Sheffield Weather Station data again, this time considering the monthly rainfall in July (a dry month) and November (a wet month). We expect these might be differently distributed, so we will take permutation samples to see how their ECDFs would look if they were identically distributed.

The data are stored in the Numpy arrays rain_june and rain_november.

As a reminder, permutation_sample() has a function signature of permutation_sample(data_1, data_2) with a return value of permuted_data[:len(data_1)], permuted_data[len(data_1):], where `permuted_data = np.random.permutation(np.concatenate((data_1, data_2)))`.

### Instructions:
* Write a for loop to 50 generate permutation samples, compute their ECDFs, and plot them.
** Generate a permutation sample pair from rain_june and rain_november using your permutation_sample() function.
** Generate the x and y values for an ECDF for each of the two permutation samples for the ECDF using your ecdf() function.
** Plot the ECDF of the first permutation sample (x_1 and y_1) as dots. Do the same for the second permutation sample (x_2 and y_2).
* Generate x and y values for ECDFs for the rain_june and rain_november data and plot the ECDFs using respectively the keyword arguments color='red' and color='blue'.
* Label your axes, set a 2% margin, and show your plot. This has been done for you, so just hit 'Submit Answer' to view the plot!

#### Script:
```
for i in range(50):
    # Generate permutation samples
    perm_sample_1, perm_sample_2 = permutation_sample(rain_june, rain_november)


    # Compute ECDFs
    x_1, y_1 = ecdf(perm_sample_1)
    x_2, y_2 = ecdf(perm_sample_2)

    # Plot ECDFs of permutation sample
    _ = plt.plot(x_1, y_1, marker='.', linestyle='none',
                 color='red', alpha=0.02)
    _ = plt.plot(x_2, y_2, marker='.', linestyle='none',
                 color='blue', alpha=0.02)

# Create and plot ECDFs from original data
x_1, y_1 = ecdf(rain_june)
x_2, y_2 = ecdf(rain_november)
_ = plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
_ = plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')

# Label axes, set margin, and show plot
plt.margins(0.02)
_ = plt.xlabel('monthly rainfall (mm)')
_ = plt.ylabel('ECDF')
plt.show()
```

#### Output:
```
In [1]: rain_june[:5]
Out[1]: array([66.2, 39.7, 76.4, 26.5, 11.2])

In [2]: len(rain_june)
Out[2]: 133

In [3]: rain_november[:5]
Out[3]: array([83.6, 30.9, 62.2, 37. , 41. ])

In [4]: len(rain_november)
Out[4]: 133
```
##### ECDF plot for 133 permuted samples (1 iteration) 
![Alt text](./ecdf_permutation1.svg)

##### ECDF plot for 133 permuted samples (5 iterations) 
![Alt text](./ecdf_permutation.svg)

##### ECDF plot for 133 permuted samples (50 iterations) 
![Alt text](./ecdf_permutation.svg)

##### ECDF Plot for the original data
![Alt text](./ecdf_original_data.svg)

##### ECDF plot for 133 samples, both the original and the permuted samples (50 iterations)
![Alt text](./ecdf_permutation_original.svg)

#### Comment:
Great work! Notice that the permutation samples ECDFs overlap and give a purple haze. None of the ECDFs from the permutation samples overlap with the observed data, suggesting that the hypothesis is not commensurate with the data. July and November rainfall are not identically distributed.

## 03. Test statistics
When performing hypothesis tests, your choice of test statistic should be:

### Possible Answers
* something well-known, like the mean or median.
** press 1
* be a parameter that can be estimated.
** press 2
* be pertinent to the question you are seeking to answer in your hypothesis test.
** press 3

#### Answer:
3

#### Comment:
Yes! The most important thing to consider is: What are you asking?

## 04. What is a p-value?
The p-value is generally a measure of:

### Possible Answers
* the probability that the hypothesis you are testing is true.
** press 1
* the probability of observing your data if the hypothesis you are testing is true.
** press 2
* the probability of observing a test statistic equally or more extreme than the one you observed, given that the null hypothesis is true.
** press 3

#### Answer:
3

#### Comment:
Correct!
