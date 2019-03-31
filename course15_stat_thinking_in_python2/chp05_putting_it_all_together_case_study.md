# Chapter 05: Putting It All Together: Case Study

## 01. EDA of beak depths of Darwin's finches
For your first foray into the Darwin finch data, you will study how the beak depth (the distance, top to bottom, of a closed beak) of the finch species Geospiza scandens has changed over time. The Grants have noticed some changes of beak geometry depending on the types of seeds available on the island, and they also noticed that there was some interbreeding with another major species on Daphne Major, Geospiza fortis. These effects can lead to changes in the species over time.

In the next few problems, you will look at the beak depth of G. scandens on Daphne Major in 1975 and in 2012. To start with, let's plot all of the beak depth measurements in 1975 and 2012 in a bee swarm plot.

The data are stored in a pandas DataFrame called df with columns 'year' and 'beak_depth'. The units of beak depth are millimeters (mm).

### Instructions:
* Create the beeswarm plot.
* Label the axes.
* Show the plot.

#### Script:
```
# Create bee swarm plot
_ = sns.swarmplot(x = 'year', y = 'beak_depth', data = df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()
```

#### Output:
```
In [5]: type(df)
Out[5]: pandas.core.frame.DataFrame
```
```
In [2]: df.columns
Out[2]: Index(['beak_depth', 'year'], dtype='object')
```
```
In [1]: df.head(7)
Out[1]: 
   beak_depth  year
0         8.4  1975
1         8.8  1975
2         8.4  1975
3         8.0  1975
4         7.9  1975
5         8.9  1975
6         8.6  1975
```
![Alt text](./year_beak_depth.svg)

#### Comment:
It is kind of hard to see if there is a clear difference between the 1975 and 2012 data set. Eyeballing it, it appears as though the mean of the 2012 data set might be slightly higher, and it might have a bigger variance.

## 02. ECDFs of beak depths
While bee swarm plots are useful, we found that ECDFs are often even better when doing EDA. Plot the ECDFs for the 1975 and 2012 beak depth measurements on the same plot.

For your convenience, the beak depths for the respective years has been stored in the NumPy arrays bd_1975 and bd_2012.

### Instructions:
* Compute the ECDF for the 1975 and 2012 data.
* Plot the two ECDFs.
* Set a 2% margin and add axis labels and a legend to the plot.
* Hit 'Submit Answer' to view the plot!

#### Script:
```
# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('beak depth (mm)')
_ = plt.ylabel('ECDF')
_ = plt.legend(('1975', '2012'), loc='lower right')

# Show the plot
plt.show()
```

#### Output:
```
In [1]: type(bd_1975)
Out[1]: numpy.ndarray

In [2]: bd_1975.shape
Out[2]: (87,)
```
```
In [4]: bd_1975[:7]
Out[4]: array([8.4, 8.8, 8.4, 8. , 7.9, 8.9, 8.6])
```
```
In [5]: bd_2012[:7]
Out[5]: array([ 9.4,  8.9,  9.5, 11. ,  8.7,  8.4,  9.1])
```
![Alt text](./bd_1975_2012.svg)

#### Comment:
The differences are much clearer in the ECDF. The mean is larger in the 2012 data, and the variance does appear larger as well.
