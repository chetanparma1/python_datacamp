# Chapter 03: Combining Data for Analysis

## 01. Combining rows of data
The dataset you'll be working with here relates to NYC Uber data. The original dataset has all the originating Uber pickup locations by time and latitude and longitude. For didactic purposes, you'll be working with a very small portion of the actual data.

Three DataFrames have been pre-loaded: uber1, which contains data for April 2014, uber2, which contains data for May 2014, and uber3, which contains data for June 2014. Your job in this exercise is to concatenate these DataFrames together such that the resulting DataFrame has the data for all three months.

Begin by exploring the structure of these three DataFrames in the IPython Shell using methods such as .head().

### Instructions:
* Concatenate uber1, uber2, and uber3 together using pd.concat(). You'll have to pass the DataFrames in as a list.
* Print the shape and then the head of the concatenated DataFrame, row_concat.

#### Script
```
# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())
```
##### Output
```
<script.py> output:
    (297, 4)
              Date/Time      Lat      Lon    Base
    0  4/1/2014 0:11:00  40.7690 -73.9549  B02512
    1  4/1/2014 0:17:00  40.7267 -74.0345  B02512
    2  4/1/2014 0:21:00  40.7316 -73.9873  B02512
    3  4/1/2014 0:28:00  40.7588 -73.9776  B02512
    4  4/1/2014 0:33:00  40.7594 -73.9722  B02512
```

##### Comment:
Great work! You have successfully concatenated the three uber DataFrames! Notice that the head of row_concat is the same as the head of uber1, while the tail of row_concat is the same as the tail of uber3.
