# Chapter 01: Analyzing Time Series and Images

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
