# Chapter 01: Customizing Plots

## 01. Multiple plots on single axis
It is time now to put together some of what you have learned and combine line plots on a common set of axes. The data set here comes from records of undergraduate degrees awarded to women in a variety of fields from 1970 to 2011. You can compare trends in degrees most easily by viewing two curves on the same set of axes.

Here, three NumPy arrays have been pre-loaded for you: year (enumerating years from 1970 to 2011 inclusive), physical_sciences (representing the percentage of Physical Sciences degrees awarded to women each in corresponding year), and computer_science (representing the percentage of Computer Science degrees awarded to women in each corresponding year).

You will issue two plt.plot() commands to draw line plots of different colors on the same set of axes. Here, year represents the x-axis, while `physical_sciences` and `computer_science` are the y-axes.

### Instructions:
* Import `matplotlib.pyplot` as its usual alias.
* Add a 'blue' line plot of the % of degrees awarded to women in the Physical Sciences (physical_sciences) from 1970 to 2011 (year). Note that the x-axis should be specified first.
* Add a 'red' line plot of the % of degrees awarded to women in Computer Science (computer_science) from 1970 to 2011 (year).
* Use `plt.show()` to display the figure with the curves on the same axes.

#### Script:
```
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()

```
#### Output:
```
In [2]: year
Out[2]: 
array([1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
       1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991,
       1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
       2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011])

In [3]: physical_sciences
Out[3]: 
array([13.8, 14.9, 14.8, 16.5, 18.2, 19.1, 20. , 21.3, 22.5, 23.7, 24.6,
       25.7, 27.3, 27.6, 28. , 27.5, 28.4, 30.4, 29.7, 31.3, 31.6, 32.6,
       32.6, 33.6, 34.8, 35.9, 37.3, 38.3, 39.7, 40.2, 41. , 42.2, 41.1,
       41.7, 42.1, 41.6, 40.8, 40.7, 40.7, 40.7, 40.2, 40.1])

In [4]: computer_science
Out[4]: 
array([13.6, 13.6, 14.9, 16.4, 18.9, 19.8, 23.9, 25.7, 28.1, 30.2, 32.5,
       34.8, 36.3, 37.1, 36.8, 35.7, 34.7, 32.4, 30.8, 29.9, 29.4, 28.7,
       28.2, 28.5, 28.5, 27.5, 27.1, 26.8, 27. , 28.1, 27.7, 27.6, 27. ,
       25.1, 22.2, 20.6, 18.6, 17.6, 17.8, 18.1, 17.6, 18.2])
```
![Alt text](./plot1.svg)

#### Comment:
Well done! It looks like, for the last 25 years or so, more women have been awarded undergraduate degrees in the Physical Sciences than in Computer Science.

## 02. Using axes()
Rather than overlaying line plots on common axes, you may prefer to plot different line plots on distinct axes. The command plt.axes() is one way to do this (but it requires specifying coordinates relative to the size of the figure).

Here, you have the same three arrays year, physical_sciences, and computer_science representing percentages of degrees awarded to women over a range of years. You will use plt.axes() to create separate sets of axes in which you will draw each line plot.

In calling `plt.axes([xlo, ylo, width, height])`, a set of axes is created and made active with lower corner at coordinates `(xlo, ylo)` of the specified width and height. Note that these coordinates can be passed to plt.axes() in the form of a list or a tuple.

The coordinates and lengths are values between 0 and 1 representing lengths relative to the dimensions of the figure. After issuing a plt.axes() command, plots generated are put in that set of axes.

### Instructions:
* Create a set of plot axes with lower corner xlo and ylo of 0.05 and 0.05, width of 0.425, and height of 0.9 (in units relative to the figure dimension).
** Note: Remember to pass these coordinates to plt.axes() in the form of a list: [xlo, ylo, width, height].
* Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active axes just created.
* Create a set of plot axes with lower corner xlo and ylo of 0.525 and 0.05, width of 0.425, and height of 0.9 (in units relative to the figure dimension).
* Plot the percentage of degrees awarded to women in Computer Science in red in the active axes just created.

#### Script:
```
# Create plot axes for the first line plot
# define a rect
plt.axes([0.05, 0.05, 0.425, 0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
# define another rect
plt.axes([0.525, 0.05, 0.425, 0.9])

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()
```
#### Output:
![Alt text](./plt_axes.svg)

#### Comment:
Great work! As you can see, not only are there now two separate plots with their own axes, but the axes for each plot are slightly different.

## 03. Using subplot() (1)
The command `plt.axes()` requires a lot of effort to use well because the coordinates of the axes need to be set manually. A better alternative is to use `plt.subplot()` to determine the layout automatically.

In this exercise, you will continue working with the same arrays from the previous exercises: year, physical_sciences, and computer_science. Rather than using plt.axes() to explicitly lay out the axes, you will use plt.subplot(m, n, k) to make the subplot grid of dimensions m by n and to make the kth subplot active (subplots are numbered starting from 1 row-wise from the top left corner of the subplot grid).

### Instructions:
* Use plt.subplot() to create a figure with 1x2 subplot layout & make the first subplot active.
* Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active subplot.
* Use plt.subplot() again to make the second subplot active in the current 1x2 subplot grid.
* Plot the percentage of degrees awarded to women in Computer Science in red in the active subplot.

#### Script:
```
# Create a figure with 1x2 subplot and make the left subplot active
plt.subplot(1, 2, 1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt.subplot(1, 2, 2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()
```
#### Output:
![Alt text](./plt_subplot.svg)

#### Comment:
Excellent work! Using subplots like this is a better alternative to using plt.axes().

## 04. Using subplot() (2)
Now you have some familiarity with `plt.subplot()`, you can use it to plot more plots in larger grids of subplots of the same figure.

Here, you will make a 2×2 grid of subplots and plot the percentage of degrees awarded to women in Physical Sciences (using `physical_sciences`), in Computer Science (using computer_science), in Health Professions (using health), and in Education (using education).

### Instructions:
* Create a figure with 2×2 subplot layout, make the top, left subplot active, and plot the % of degrees awarded to women in Physical Sciences in blue in the active subplot.
* Make the top, right subplot active in the current 2×2 subplot grid and plot the % of degrees awarded to women in Computer Science in red in the active subplot.
* Make the bottom, left subplot active in the current 2×2 subplot grid and plot the % of degrees awarded to women in Health Professions in green in the active subplot.
* Make the bottom, right subplot active in the current 2×2 subplot grid and plot the % of degrees awarded to women in Education in yellow in the active subplot.

#### Script:
```
# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2, 2, 1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Make the top right subplot active in the current 2x2 subplot grid 
plt.subplot(2, 2, 2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2, 2, 3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2, 2, 4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()
```

#### Output:
```
In [1]: health
Out[1]: 
array([77.1, 75.5, 76.9, 77.4, 77.9, 78.9, 79.2, 80.5, 81.9, 82.3, 83.5,
       84.1, 84.4, 84.6, 85.1, 85.3, 85.7, 85.5, 85.2, 84.6, 83.9, 83.5,
       83. , 82.4, 81.8, 81.5, 81.3, 81.9, 82.1, 83.5, 83.5, 85.1, 85.8,
       86.5, 86.5, 86. , 85.9, 85.4, 85.2, 85.1, 85. , 84.8])

In [2]: education
Out[2]: 
array([74.53532758, 74.14920369, 73.55451996, 73.50181443, 73.33681143,
       72.80185448, 72.16652471, 72.45639481, 73.19282134, 73.82114234,
       74.98103152, 75.84512345, 75.84364914, 75.95060123, 75.86911601,
       75.92343971, 76.14301516, 76.96309168, 77.62766177, 78.11191872,
       78.86685859, 78.99124597, 78.43518191, 77.26731199, 75.81493264,
       75.12525621, 75.03519921, 75.1637013 , 75.48616027, 75.83816206,
       76.69214284, 77.37522931, 78.64424394, 78.54494815, 78.65074774,
       79.06712173, 78.68630551, 78.72141311, 79.19632674, 79.5329087 ,
       79.61862451, 79.43281184])
```
![Alt text](./subplot4.svg)

#### Comment:
Great work! You can use this approach to create subplots in any layout of your choice.

## 05. Using xlim(), ylim()
In this exercise, you will work with the matplotlib.pyplot interface to quickly set the x- and y-limits of your plots.

You will now create the same figure as in the previous exercise using plt.plot(), this time setting the axis extents using `plt.xlim()` and `plt.ylim()`. These commands allow you to either zoom or expand the plot or to set the axis ranges to include important values (such as the origin).

In this exercise, as before, the percentage of women graduates in Computer Science and in the Physical Sciences are held in the variables computer_science and physical_sciences respectively over year.

After creating the plot, you will use plt.savefig() to export the image produced to a file.

### Instructions:
* Use `plt.xlim()` to set the x-axis range to the period between the years 1990 and 2010.
* Use `plt.ylim()` to set the y-axis range to the interval between 0% and 50% of degrees awarded.
* Display the final figure with plt.show() and save the output to 'xlim_and_ylim.png'.

#### Script:
```
# Plot the % of degrees awarded to women in Computer Science and the Physical Sciences
plt.plot(year,computer_science, color='red') 
plt.plot(year, physical_sciences, color='blue')

# Add the axis labels
plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')

# Set the x-axis range
plt.xlim([1990, 2010])

# Set the y-axis range
plt.ylim([0, 50])

# Add a title and display the plot
plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')
plt.show()

# Save the image as 'xlim_and_ylim.png'
plt.savefig('xlim_and_ylim.png')
```
#### Output:
![Alt text](./xylim.svg)

#### Comment:
Fantastic! This plot effectively captures the difference in trends between 1990 and 2010.

## 06. Using axis()
Using `plt.xlim()` and `plt.ylim()` are useful for setting the axis limits individually. In this exercise, you will see how you can pass a 4-tuple to plt.axis() to set limits for both axes at once. For example, plt.axis((1980,1990,0,75)) would set the extent of the x-axis to the period between 1980 and 1990, and would set the y-axis extent from 0 to 75% degrees award.

Once again, the percentage of women graduates in Computer Science and in the Physical Sciences are held in the variables computer_science and physical_sciences where each value was measured at the corresponding year held in the year variable.

### Instructions:
* Use `plt.axis()` to select the time period between 1990 and 2010 on the x-axis as well as the interval between 0 and 50% awarded on the y-axis.
* Save the resulting plot as `'axis_limits.png'`.

#### Script:
```
# Plot in blue the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color='blue')

# Plot in red the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences,color='red')

# Set the x-axis and y-axis limits
plt.axis([1990, 2010, 0, 50])

# Show the figure
plt.show()

# Save the figure as 'axis_limits.png'
plt.savefig('axis_limits.png')

```
#### Output:
![Alt text](./pltaxis.svg)

#### Comment:
Superb! Using plt.axis() allows you to set limits for both axes at once, as opposed to setting them individually with `plt.xlim()` and `plt.ylim()`.

## 07. Using legend()
Legends are useful for distinguishing between multiple datasets displayed on common axes. The relevant data are created using specific line colors or markers in various plot commands. Using the keyword argument label in the plotting function associates a string to use in a legend.

For example, here, you will plot enrollment of women in the Physical Sciences and in Computer Science over time. You can label each curve by passing a label argument to the plotting call, and request a legend using `plt.legend()`. Specifying the keyword argument `loc` determines where the legend will be placed.

### Instructions:
* Modify the plot command provided that draws the enrollment of women in Computer Science over time so that the curve is labelled 'Computer Science' in the legend.
* Modify the plot command provided that draws the enrollment of women in the Physical Sciences over time so that the curve is labelled 'Physical Sciences' in the legend.
* Add a legend at the lower center (i.e., loc='lower center').

#### Script:
```
# Specify the label 'Computer Science'
plt.plot(year, computer_science, color='red', label='Computer Science') 

# Specify the label 'Physical Sciences' 
plt.plot(year, physical_sciences, color='blue', label='Physical Science')

# Add a legend at the lower center
plt.legend(loc='best')

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
```
#### Output:
![Alt text](./plt_legend.svg)

#### Comment:
Excellent work! You should always use axes labels and legends to help make your plots more readable.

## 08. Using annotate()
It is often useful to annotate a simple plot to provide context. This makes the plot more readable and can highlight specific aspects of the data. Annotations like text and arrows can be used to emphasize specific observations.

Here, you will once again plot enrollment of women in the Physical Sciences and Computer science over time. The legend is set up as before. Additionally, you will mark the inflection point when enrollment of women in Computer Science reached a peak and started declining using `plt.annotate()`.

To enable an arrow, set `arrowprops=dict(facecolor='black')`. The arrow will point to the location given by xy and the text will appear at the location given by xytext.

### Instructions:
* Compute the maximum enrollment of women in Computer Science using the .max() method.
* Calculate the year in which there was maximum enrollment of women in Computer Science using the .argmax() method.
* Annotate the plot with an arrow at the point of peak women enrolling in Computer Science.
** Label the arrow 'Maximum'. The parameter for this is s, but you don't have to specify it.
** Pass in the arguments to xy and xytext as tuples.
** For xy, use the yr_max and cs_max that you computed.
** For xytext, use (yr_max+5, cs_max+5) to specify the displacement of the label from the tip of the arrow.
** Draw the arrow by specifying the keyword argument arrowprops=dict(facecolor='black'). The single letter shortcut for `'black'` is `'k'`.

#### Script:
```
# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum', xy = (yr_max, cs_max), xytext = (yr_max+5, cs_max+5), arrowprops = dict(facecolor = 'black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
```
#### Output:
![Alt text](./annotation.svg)

#### Comment:
Great work! Annotations are extremely useful to help make more complicated plots easier to understand.

## 09. Modifying styles
Matplotlib comes with a number of different stylesheets to customize the overall look of different plots. To activate a particular stylesheet you can simply call `plt.style.use()` with the name of the style sheet you want. To list all the available style sheets you can execute:`print(plt.style.available)`.

### Instructions:
* Import matplotlib.pyplot as its usual alias.
* Activate the `'ggplot'` style sheet with `plt.style.use()`.

#### Script:
```
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Set the style to 'ggplot'
plt.style.use('ggplot')

# Create a figure with 2x2 subplot layout
plt.subplot(2, 2, 1) 

# Plot the enrollment % of women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

# Plot the enrollment % of women in Computer Science
plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Add annotation
cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))

# Plot the enrollmment % of women in Health professions
plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Plot the enrollment % of women in Education
plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve spacing between subplots and display them
plt.tight_layout()
plt.show()
```
#### Output:
![Alt text](./ggplot_style.svg)

#### Comment:
Fantastic! The 'ggplot' style is a popular one. You've reached the end of Chapter 1 - well done, and see you in Chapter 2, where you'll learn all about plotting 2D arrays!
