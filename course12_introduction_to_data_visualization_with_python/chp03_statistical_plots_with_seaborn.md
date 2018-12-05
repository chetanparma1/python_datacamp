# Chapter 03: Statistical Plots with Seaborn. 

## 01. Simple linear regressions
As you have seen, seaborn provides a convenient interface to generate complex and great-looking statistical plots. One of the simplest things you can do using seaborn is to fit and visualize a simple linear regression between two variables using `sns.lmplot()`.

One difference between seaborn and regular matplotlib plotting is that you can pass pandas DataFrames directly to the plot and refer to each column by name. For example, if you were to plot the column 'price' vs the column 'area' from a DataFrame df, you could call `sns.lmplot(x='area', y='price', data=df)`.

In this exercise, you will once again use the DataFrame auto containing the auto-mpg dataset. You will plot a linear regression illustrating the relationship between automobile weight and horse power.

### Instructions:
* Import `matplotlib.pyplot` and `seaborn using` the standard names plt and sns respectively.
* Plot a linear regression between the 'weight' column (on the x-axis) and the 'hp' column (on the y-axis) from the DataFrame auto.
* Display the plot as usual with plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot. 

#### Script:
```
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x = 'weight', y = 'hp', data=auto)

# Display the plot
plt.show()

```
#### Output:
```
In [4]: auto.head()
Out[4]: 
    mpg  cyl  displ   hp  weight  accel  yr  origin              name  color  \
0  18.0    6  250.0   88    3139   14.5  71      US      ford mustang    red   
1   9.0    8  304.0  193    4732   18.5  70      US          hi 1200d  green   
2  36.1    4   91.0   60    1800   16.4  78    Asia  honda civic cvcc   blue   
3  18.5    6  250.0   98    3525   19.0  77      US      ford granada    red   
4  34.3    4   97.0   78    2188   15.8  80  Europe         audi 4000   blue   

        size marker  
0  27.370336      o  
1  62.199511      o  
2   9.000000      x  
3  34.515625      o  
4  13.298178      s
```
![Alt text](./sns_auto.png)

#### Comment:
Fantastic work! Unsurprisingly, there is a strong correlation between 'hp' and 'weight', and a linear regression is easily able to capture this trend.

## 02. Plotting residuals of a regression
Often, you don't just want to see the regression itself but also see the residuals to get a better idea how well the regression captured the data. Seaborn provides `sns.residplot()` for that purpose, visualizing how far datapoints diverge from the regression line.

In this exercise, you will visualize the residuals of a regression between the `'hp'` column (horse power) and the 'mpg' column (miles per gallon) of the auto DataFrame used previously.

### Instructions:
* Import `matplotlib.pyplot` and `seaborn` using the standard names plt and sns respectively.
* Generate a green residual plot of the regression between 'hp' (on the x-axis) and 'mpg' (on the y-axis). You will need to specify the additional data and color parameters.
* Display the plot as usual using plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot.

#### Script:
```
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()
```
#### Output:
![Alt text](./residplot.svg)

#### Comment:
Excellent! Seaborn makes it very easy to quickly plot the residuals of regressions, as shown here.
