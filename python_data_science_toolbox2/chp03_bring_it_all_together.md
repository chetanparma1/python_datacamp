# Dictionaries for data science
For this exercise, you'll use what you've learned about the zip() function and combine two lists into a dictionary.

These lists are actually extracted from a bigger dataset file of world development indicators from the World Bank. For pedagogical purposes, we have pre-processed this dataset into the lists that you'll be working with.

The first list feature_names contains header names of the dataset and the second list row_vals contains actual values of a row from the dataset, corresponding to each of the header names.

## Instructions
* Create a zip object by calling zip() and passing to it feature_names and row_vals. Assign the result to zipped_lists.
* Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists. Assign the resulting dictionary to rs_dict.

```{python}
# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)

```

### Output
```
<script.py> output:
    {'CountryName': 'Arab World', 'IndicatorCode': 'SP.ADO.TFRT', 'CountryCode': 'ARB', 'Value': '133.56090740552298', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'Year': '1960'}

```

### Comments:
Great work!

# Writing a function to help you
Suppose you needed to repeat the same process done in the previous exercise to many, many rows of data. Rewriting your code again and again could become very tedious, repetitive, and unmaintainable.

In this exercise, you will create a function to house the code you wrote earlier to make things easier and much more concise. Why? This way, you only need to call the function and supply the appropriate lists to create your dictionaries! Again, the lists feature_names and row_vals are preloaded and these contain the header names of the dataset and actual values of a row from the dataset, respectively.

## Instructions
* Define the function lists2dict() with two parameters: first is list1 and second is list2.
* Return the resulting dictionary rs_dict in lists2dict().
* Call the lists2dict() function with the arguments feature_names and row_vals. Assign the result of the function call to rs_fxn.

```{python}
# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)
```
### Output:
```
<script.py> output:
    {'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'Value': '133.56090740552298', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'CountryCode': 'ARB', 'CountryName': 'Arab World'}
```
### Comments:
Great work!

# Using a list comprehension
This time, you're going to use the lists2dict() function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.

The lists2dict() function has already been preloaded, together with a couple of lists, feature_names and row_lists. feature_names contains the header names of the World Bank dataset and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.

Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries.

## Instructions:
* Inspect the contents of row_lists by printing the first two lists in row_lists.
* Create a list comprehension that generates a dictionary using lists2dict() for each sublist in row_lists. The keys are from the feature_names list and the values are the row entries in row_lists. Use sublist as your iterator variable and assign the resulting list of dictionaries to list_of_dicts.
* Look at the first two dictionaries in list_of_dicts by printing them out.

```{python}
# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])
```
### Output:
```
<script.py> output:
    ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']
    ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547']
    {'Year': '1960', 'CountryName': 'Arab World', 'CountryCode': 'ARB', 'Value': '133.56090740552298', 'IndicatorCode': 'SP.ADO.TFRT', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)'}
    {'Year': '1960', 'CountryName': 'Arab World', 'CountryCode': 'ARB', 'Value': '87.7976011532547', 'IndicatorCode': 'SP.POP.DPND', 'IndicatorName': 'Age dependency ratio (% of working-age population)'}
```
#### Comments:
Great work!
