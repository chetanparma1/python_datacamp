# Chapter 04: Analyzing Time Series and Images

## 01. Multiple time series on common axes
For this exercise, you will construct a plot showing four time series stocks on the same axes. The time series in question are represented in the session using the identifiers `aapl`, `ibm`, csco, and msft. You'll generate a single plot showing all the time series on common axes with a legend.

### Instructions:
* Plot the `aapl` time series in blue with a label of 'AAPL'.
* Plot the `ibm` time series in green with a label of 'IBM'.
* Plot the csco time series in red with a label of 'CSCO'.
* Plot the msft time series in magenta with a label of 'MSFT'.
* Specify a rotation of 60 for the xticks with plt.xticks().
* Add a legend in the 'upper left' corner of the plot.

#### Script:
```
# Import matplotlib.pyplot
from matplotlib import pyplot as plt

# Plot the aapl time series in blue
plt.plot(aapl, color='blue', label='AAPL')

# Plot the ibm time series in green
plt.plot(ibm, color='green', label='IBM')

# Plot the csco time series in red
plt.plot(csco, color='red', label='CSCO')

# Plot the msft time series in magenta
plt.plot(msft, color='magenta', label='MSFT')

# Add a legend in the top left corner of the plot
plt.legend(loc='upper left')

# Specify the orientation of the xticks
plt.xticks(rotation=60)

# Display the plot
plt.show()

```

#### Output:
```
In [1]: aapl.head()
Out[1]: 
Date
2000-01-03    111.937502
2000-01-04    102.500003
2000-01-05    103.999997
2000-01-06     94.999998
2000-01-07     99.500001
Name: AAPL, dtype: float64

In [2]: ibm.head()
Out[2]: 
Date
2000-01-03    116.0000
2000-01-04    112.0625
2000-01-05    116.0000
2000-01-06    114.0000
2000-01-07    113.5000
Name: IBM, dtype: float64

In [3]: csco.head()
Out[3]: 
Date
2000-01-03    108.0625
2000-01-04    102.0000
2000-01-05    101.6875
2000-01-06    100.0000
2000-01-07    105.8750
Name: CSCO, dtype: float64

In [4]: msft.head()
Out[4]: 
Date
2000-01-03    116.5625
2000-01-04    112.6250
2000-01-05    113.8125
2000-01-06    110.0000
2000-01-07    111.4375
Name: MSFT, dtype: float64

In [5]: 
```
![Alt text](./timeseries.svg)

#### Comment:
Great work! It looks like 'AAPL' has done particularly well in recent years!

## 02. Multiple time series slices (1)
You can easily slice subsets corresponding to different time intervals from a time series. In particular, you can use strings like `'2001:2005'`, `'2011-03:2011-12'`, or '2010-04-19:2010-04-30' to extract data from time intervals of length 5 years, 10 months, or 12 days respectively.

* Unlike slicing from standard Python lists, tuples, and strings, when slicing time series by labels (and other pandas Series & DataFrames by labels), the slice includes the right-most portion of the slice. That is, extracting my_time_series['1990':'1995'] extracts data from my_time_series corresponding to 1990, 1991, 1992, 1993, 1994, and 1995 inclusive.
* You can use partial strings or datetime objects for indexing and slicing from time series.
For this exercise, you will use time series slicing to plot the time series aapl over its full 11-year range and also over a shorter 2-year range. You'll arrange these plots in a 2×1 grid of subplots

### Instructions:
* Plot the series `aapl` in `'blue'` in the top subplot of a vertically-stacked pair of subplots, with the xticks rotated to 45 degrees.
* Extract a slice named view from the series aapl containing data from the years 2007 to 2008 (inclusive). This has been done for you.
* Plot the slice view in black in the bottom subplot.

#### Script:
```
# Plot the series in the top subplot in blue
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(aapl, color='blue')

# Slice aapl from '2007' to '2008' inclusive: view
view = aapl['2007':'2008']

# Plot the sliced data in the bottom subplot in black
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()

```
#### Output:
![Alt text](./aapl.svg)

#### Comment:
Fantastic! Plotting time series at different intervals can provide you with deeper insight into your data. Here, for example, you can see that the AAPL stock price rose and fell a great amount between 2007 and 2008.

## 03. Multiple time series slices (2)
In this exercise, you will use the same time series aapl from the previous exercise and plot tighter views of the data.

* Partial string indexing works without slicing as well. For instance, using `my_time_series['1995']`, `my_time_series['1999-05']`, and my_time_series['2000-11-04'] respectively extracts views of the time series my_time_series corresponding to the entire year 1995, the entire month May 1999, and the entire day November 4, 2000.

### Instructions:
* Extract a slice named `view` from the series `aapl` containing data from November 2007 to April 2008 (inclusive). This has been done for you.
* Plot the slice view in 'red' in the top subplot of a vertically-stacked pair of subplots with the xticks rotated to 45 degrees.
* Reassign the slice view to contain data from the series aapl for January 2008. This has been done for you.
* Plot the slice view in 'green' in the bottom subplot with the xticks rotated to 45 degrees.

#### Script:
```
# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the sliced series in the top subplot in red
plt.subplot(2, 1, 1)
plt.plot(view, color='red')
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.xticks(rotation=45)

# Reassign the series by slicing the month January 2008
view = aapl['2008-01']

# Plot the sliced series in the bottom subplot in green
plt.subplot(2, 1, 2)
plt.plot(view, color='green')
plt.title('AAPL: Jan. 2008')
plt.xticks(rotation=45)

# Improve spacing and display the plot
plt.tight_layout()
plt.show()
```
#### Output:
![Alt text](./timeseries_slice.svg)

#### Comment:
Great work!

## 04. Plotting an inset view
Remember, rather than comparing plots with subplots or overlayed plots, you can generate an inset view directly using `plt.axes()`. In this exercise, you'll reproduce two of the time series plots from the preceding two exercises. Your figure will contain an inset plot to highlight the dramatic changes in AAPL stock price between November 2007 and April 2008 (as compared to the 11 years from 2001 to 2011).

### Instructions:
* Extract a slice of series `aapl` from November 2007 to April 2008 inclusive. This has been done for you.
* Plot the entire series `aapl`.
* Create a set of axes with lower left corner (0.25, 0.5), width 0.35, and height 0.35. Pass these coordinates to plt.axes() as a list (all in units relative to the figure dimensions).
* Plot the sliced view in the current axes in 'red'

#### Script:
```
# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the entire series 
plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

# Specify the axes
plt.axes([0.25, 0.5, 0.35, 0.35])

# Plot the sliced series in red using the current axes
plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()
```
#### Output:
![Alt text](./inset.svg)

#### Comment:
Well done! Inset views are a useful way of comparing time series data.

## 05. Plotting moving averages
In this exercise, you will plot pre-computed moving averages of AAPL stock prices in distinct subplots.

* The time series aapl is overlayed in black in each subplot for comparison.
* The time series `mean_30`, `mean_75`, mean_125, and mean_250 have been computed for you (containing the windowed averages of the series aapl computed over windows of width 30 days, 75 days, 125 days, and 250 days respectively).

### Instructions:
* In the top left subplot, plot the 30-day moving averages series `mean_30` in 'green'.
* In the top right subplot, plot the 75-day moving averages series `mean_75` in 'red'.
* In the bottom left subplot, plot the 125-day moving averages series mean_125 in 'magenta'.
* In the bottom right subplot, plot the 250-day moving averages series mean_250 in 'cyan'.

#### Script:
```
# read about moving average here: https://chrisalbon.com/python/data_wrangling/pandas_moving_average/
# Plot the 30-day moving average in the top left subplot in green
plt.subplot(2, 2, 1)
plt.plot(mean_30, color='green')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')

# Plot the 75-day moving average in the top right subplot in red
plt.subplot(2,2, 2)
plt.plot(mean_75, color='red')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

# Plot the 125-day moving average in the bottom left subplot in magenta
plt.subplot(2, 2, 3)
plt.plot(mean_125, color='magenta')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

# Plot the 250-day moving average in the bottom right subplot in cyan
plt.subplot(2, 2, 4)
plt.plot(mean_250, color='cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

# Display the plot
plt.show()
```
#### Output:
![Alt text](./moving_average.svg)

#### Comment:
Great work!

## 06. Plotting moving standard deviations
Having plotted pre-computed moving averages of AAPL stock prices on distinct subplots in the previous exercise, you will now plot pre-computed moving standard deviations of the same stock prices, this time together on common axes.

* The time series aapl is not plotted in this case; it is of a different length scale than the standard deviations.
* The time series `std_30`, `std_75`, stdn_125, & std_250 have been computed for you (containing the windowed standard deviations of the series aapl computed over windows of width 30 days, 75 days, 125 days, & 250 days respectively).

### Instructions:
* Produce a single plot with four curves overlayed:
* the series `std_30` in `'red'` (with corresponding label `'30d'`).
* the series std_75 in 'cyan' (with corresponding label '75d').
* the series std_125 in 'green' (with corresponding label '125d').
* the series std_250 in 'magenta' (with corresponding label '250d').
* Add a legend to the 'upper left' corner of the plot.

#### Script:
```
# Plot std_30 in red
plt.plot(std_30, color='red', label='30d')

# Plot std_75 in cyan
plt.plot(std_75, color='cyan', label='75d')

# Plot std_125 in green
plt.plot(std_125, color='green', label='125d')

# Plot std_250 in magenta
plt.plot(std_250, color='magenta', label='250d')

# Add a legend to the upper left
plt.legend(loc='upper left')

# Add a title
plt.title('Moving standard deviations')

# Display the plot
plt.show()
```
#### Output:
![Alt text](./moving_sd.svg)

#### Comment:
Great work!

## 07. Interpreting moving statistics
In the previous exercise, you generated the plot below.

![Alt text](./moving_sd.svg)

What length is the moving window that most consistently produces the greatest variance (standard deviation) in the AAPL stock price over the time interval shown?

### Possible Answers
* 30 days
* 75 days
* 125 days
* 250 days

#### Answer:
4

#### Comment:
Exactly! Wider moving windows admit greater variability!


## 08. Extracting a histogram from a grayscale image
For grayscale images, various image processing algorithms use an image histogram. Recall that an image is a two-dimensional array of numerical intensities. An image histogram, then, is computed by counting the occurences of distinct pixel intensities over all the pixels in the image.

For this exercise, you will load <a href="https://commons.wikimedia.org/wiki/File:Unequalized_Hawkes_Bay_NZ.jpg">an unequalized low contrast image of Hawkes Bay, New Zealand</a> (originally by Phillip Capper, modified by User:Konstable, via Wikimedia Commons, <a href="http://creativecommons.org/licenses/by/2.0>"CC BY 2.0</a>). You will plot the image and use the pixel intensity values to plot a normalized histogram of pixel intensities.

### Instructions:
* Load data from the file '640px-Unequalized_Hawkes_Bay_NZ.jpg' into an array.
* Display image with a color map of 'gray' in the top subplot.
* Flatten image into a 1-D array using the .flatten() method.
* Display a histogram of pixels in the bottom subplot.
* Use histogram options bins=64, range=(0,256), and normed=True to control numerical binning and the vertical scale.
* Use plotting options `color='red'` and `alpha=0.4` to tailor the color and transparency.

#### Script:
```
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, range=(0, 256), normed=True, color='red', alpha=0.4)

# Display the plot
plt.show()
```
#### Output:
![Alt text](./imghist.svg)

#### Comment:
Well done! Image histograms are an important component of many image processing algorithms.

## 09. Cumulative Distribution Function from an image histogram
A histogram of a continuous random variable is sometimes called a Probability Distribution Function (or PDF). The area under a PDF (a definite integral) is called a Cumulative Distribution Function (or CDF). The CDF quantifies the probability of observing certain pixel intensities.

Your task here is to plot the PDF and CDF of pixel intensities from a grayscale image. You will use the <a href="https://commons.wikimedia.org/wiki/File:Unequalized_Hawkes_Bay_NZ.jpg">grayscale image of Hawkes Bay, New Zealand</a> (originally by Phillip Capper, modified by User:Konstable, via Wikimedia Commons, <a href="http://creativecommons.org/licenses/by/2.0">CC BY 2.0</a>). This time, the 2D array image will be pre-loaded and pre-flattened into the 1D array pixels for you.

* The histogram option cumulative=True permits viewing the CDF instead of the PDF.
* Notice that `plt.grid('off')` switches off distracting grid lines.
* The command `plt.twinx()` allows two plots to be overlayed sharing the x-axis but with different scales on the y-axis.

### Instructions:
* First, use `plt.hist()` to plot the histogram of the 1-D array `pixels` in the bottom subplot.
* Use the histogram options bins=64, range=(0,256), and normed=False.
* Use the plotting options alpha=0.4 and color='red' to make the overlayed plots easier to see.
* Second, use plt.twinx() to overlay plots with different vertical scales on a common horizontal axis.
* Third, call plt.hist() again to overlay the CDF in the bottom subplot.
* Use the histogram options bins=64, range=(0,256), and normed=True.
* This time, also use cumulative=True to compute and display the CDF.
* Also, use alpha=0.4 and color='blue' to make the overlayed plots easier to see.

#### Script:
```
# Load the image into an array: image
image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

# Display image in top subplot using color map 'gray'
plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')

# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Display a histogram of the pixels in the bottom subplot
plt.subplot(2,1,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False, color='red', alpha=0.4)
plt.grid('off')

# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()

# Display a cumulative histogram of the pixels
cdf = plt.hist(pixels, bins=64, range=(0,256),
               normed=True, cumulative=True,
               color='blue', alpha=0.4)
               
# Specify x-axis range, hide axes, add title and display plot
plt.xlim((0,256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()
```
#### Output:
![Alt text](./twingx.svg)

#### Comment:
Great work! Notice that the histogram is not well centered over the range of possible pixel intensies. The CDF rises sharply near the middle (that relates to the overall grayness of the image).
