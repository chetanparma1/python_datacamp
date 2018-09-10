# Chapter 04: Case Studies - Sunlight in Austin

## 01. What method should we use to read the data?
The first step in our analysis is to read in the data. Upon inspection with a certain system tool, we find that the data appears to be ASCII encoded with comma delimited columns, but has no header and no column labels. Which of the following is the best method to start with to read the data files?

### Possible Answers
* pd.read_csv()  &emsp;&emsp;  press 1
* pd.to_csv()   &emsp;&emsp;  press 2
* pd.read_hdf()   &emsp;&emsp; press 3
* np.load()       &emsp;&emsp; press 4

#### Answer:
1

##### Comment:
Correct! The read_csv() function will become second nature to you as you continue using pandas.

## 02. Reading in a data file
Now that you have identified the method to use to read the data, let's try to read one file. The problem with real data such as this is that the files are almost never formatted in a convenient way. In this exercise, there are several problems to overcome in reading the file. First, there is no header, and thus the columns don't have labels. There is also no obvious index column, since none of the data columns contain a full date or time.

Your job is to read the file into a DataFrame using the default arguments. After inspecting it, you will re-read the file specifying that there are no headers supplied.

The CSV file has been provided for you as the variable data_file.

### Instructions
* Import pandas as pd.
* Read the file data_file into a DataFrame called df.
* Print the output of df.head(). This has been done for you. Notice the formatting problems in df.
* Re-read the data using specifying the keyword argument header=None and assign it to df_headers.
* Print the output of df_headers.head(). This has already been done for you. Hit 'Submit Answer' and see how this resolves the formatting issues.

#### Script:
```
# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv(data_file)

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv(data_file, header=None)

# Print the output of df_headers.head()
print(df_headers.head())
```
##### Output:
```
<script.py> output:
       13904  ...    .24
    0  13904  ...       
    1  13904  ...       
    2  13904  ...       
    3  13904  ...       
    4  13904  ...       
    
    [5 rows x 44 columns]
          0  ...  43
    0  13904 ...    
    1  13904 ...    
    2  13904 ...    
    3  13904 ...    
    4  13904 ...    
    
    [5 rows x 44 columns]
```
##### Comment:
Well done! Note how the column names are not informative. You'll fix this in the next exercise!
