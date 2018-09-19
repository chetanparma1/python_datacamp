# Chapter 03. Rearranging and Reshaping Data

## 01. Pivoting and the index
Prior to using .pivot(), you need to set the index of the DataFrame somehow. Is this statement True or False?

### Possible Answers
* True.
press 1
* False.
press 2

#### Answer:
2

##### Comment:
Correct!

## 02. Pivoting a single variable
Suppose you started a blog for a band, and you would like to log how many visitors you have had, and how many signed-up for your newsletter. To help design the tours later, you track where the visitors are. A DataFrame called users consisting of this information has been pre-loaded for you.

Inspect users in the IPython Shell and make a note of which variable you want to use to index the rows ('weekday'), which variable you want to use to index the columns ('city'), and which variable will populate the values in the cells ('visitors'). Try to visualize what the result should be.

For example, in the video, Dhavide used 'treatment' to index the rows, 'gender' to index the columns, and 'response' to populate the cells. Prior to pivoting, the DataFrame looked like this:
```
   id treatment gender  response
0   1         A      F         5
1   2         A      M         3
2   3         B      F         8
3   4         B      M         9
```
After pivoting:
```
gender     F  M
treatment      
A          5  3
B          8  9
```
In this exercise, your job is to pivot users so that the focus is on 'visitors', with the columns indexed by 'city' and the rows indexed by 'weekday'.

### Instructions:
* Pivot the users DataFrame with the rows indexed by 'weekday', the columns indexed by 'city', and the values populated with 'visitors'.
* Print the pivoted DataFrame. This has been done for you, so hit 'Submit Answer' to view the result.

#### Script:
```
# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday', columns='city', values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)
```
##### Output:
```
In [1]: users
Out[1]: 
  weekday    city  visitors  signups
0     Sun  Austin       139        7
1     Sun  Dallas       237       12
2     Mon  Austin       326        3
3     Mon  Dallas       456        5

<script.py> output:
    city     Austin  Dallas
    weekday                
    Mon         326     456
    Sun         139     237
```

##### Comment:
Well done! Notice how in the pivoted DataFrame, the index is labeled 'weekday', the columns are labeled 'city', and the values are populated by the number of visitors.

## 03. Pivoting all variables
If you do not select any particular variables, all of them will be pivoted. In this case - with the users DataFrame - both 'visitors' and 'signups' will be pivoted, creating hierarchical column labels.

You will explore this for yourself now in this exercise.

### Instructions
* Pivot the users DataFrame with the 'signups' indexed by 'weekday' in the rows and 'city' in the columns.
* Print the new DataFrame. This has been done for you.
* Pivot the users DataFrame with both 'signups' and 'visitors' pivoted - that is, all the variables. This will happen automatically if you do not specify an argument for the values parameter of .pivot().
* Print the pivoted DataFrame. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
<script.py> output:
    city     Austin  Dallas
    weekday                
    Mon           3       5
    Sun           7      12
            visitors        signups       
    city      Austin Dallas  Austin Dallas
    weekday                               
    Mon          326    456       3      5
    Sun          139    237       7     12
```
##### Comment:
Great work! Notice how in the second DataFrame, both 'signups' and 'visitors' were pivoted by default since you didn't provide an argument for the values parameter.

## 04. Stacking & unstacking I
You are now going to practice stacking and unstacking DataFrames. The users DataFrame you have been working with in this chapter has been pre-loaded for you, this time with a MultiIndex. Explore it in the IPython Shell to see the data layout. Pay attention to the index, and notice that the index levels are ['city', 'weekday']. So 'weekday' - the second entry - has position 1. This position is what corresponds to the level parameter in .stack() and .unstack() calls. Alternatively, you can specify 'weekday' as the level instead of its position.

Your job in this exercise is to unstack users by 'weekday'. You will then use .stack() on the unstacked DataFrame to see if you get back the original layout of users.

### Instructions:
* Define a DataFrame byweekday with the 'weekday' level of users unstacked.
* Print the byweekday DataFrame to see the new data layout. This has been done for you.
* Stack byweekday by 'weekday' and print it to check if you get the same layout as the original users DataFrame.

#### Script:
```
# unstack = move the index column as a subcolumn in each existing column. 
# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))
```

##### Output:
```
In [1]: users
Out[1]: 
                visitors  signups
city   weekday                   
Austin Mon           326        3
       Sun           139        7
Dallas Mon           456        5
       Sun           237       12

<script.py> output:
            visitors      signups    
    weekday      Mon  Sun     Mon Sun
    city                             
    Austin       326  139       3   7
    Dallas       456  237       5  12
                    visitors  signups
    city   weekday                   
    Austin Mon           326        3
           Sun           139        7
    Dallas Mon           456        5
           Sun           237       12
```
##### Comment:
Great work! By stacking and then unstacking users, you ended up with the same layout as the original DataFrame.

## 05. Stacking & unstacking II
You are now going to continue working with the users DataFrame. As always, first explore it in the IPython Shell to see the layout and note the index.

Your job in this exercise is to unstack and then stack the 'city' level, as you did previously for 'weekday'. Note that you won't get the same DataFrame.

### Instructions:
* Define a DataFrame bycity with the 'city' level of users unstacked.
* Print the bycity DataFrame to see the new data layout. This has been done for you.
* Stack bycity by 'city' and print it to check if you get the same layout as the original users DataFrame.

#### Script:
```
# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))
```
##### Output:
```
<script.py> output:
            visitors        signups       
    city      Austin Dallas  Austin Dallas
    weekday                               
    Mon          326    456       3      5
    Sun          139    237       7     12
                    visitors  signups
    weekday city                     
    Mon     Austin       326        3
            Dallas       456        5
    Sun     Austin       139        7
            Dallas       237       12
```
##### Comment:
Fantastic work! Hopefully this exercise and the previous one have developed your intuition for how stacking and unstacking work.

## 06. Restoring the index order
Continuing from the previous exercise, you will now use .swaplevel(0, 1) to flip the index levels. Note they won't be sorted. To sort them, you will have to follow up with a .sort_index(). You will then obtain the original DataFrame. Note that an unsorted index leads to slicing failures.

To begin, print both users and bycity in the IPython Shell. The goal here is to convert bycity back to something that looks like users.

### Instructions:
* Define a DataFrame newusers with the 'city' level stacked back into the index of bycity.
* Swap the levels of the index of newusers.
* Print newusers and verify that the index is not sorted. This has been done for you.
* Sort the index of newusers.
* Print newusers and verify that the index is now sorted. This has been done for you.
* Assert that newusers equals users. This has been done for you, so hit 'Submit Answer' to see the result.

#### Script:
```
# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))
```
##### Output:
```
<script.py> output:
                    visitors  signups
    city   weekday                   
    Austin Mon           326        3
    Dallas Mon           456        5
    Austin Sun           139        7
    Dallas Sun           237       12
                    visitors  signups
    city   weekday                   
    Austin Mon           326        3
           Sun           139        7
    Dallas Mon           456        5
           Sun           237       12
    True
```
##### Comment:
Wonderful work! It's now time to learn about melting DataFrames!

## 07. Adding names for readability
You are now going to practice melting DataFrames. A DataFrame called visitors_by_city_weekday has been pre-loaded for you. Explore it in the IPython Shell and see that it is the users DataFrame from previous exercises with the rows indexed by 'weekday', columns indexed by 'city', and values populated with 'visitors'.

Recall from the video that the goal of melting is to restore a pivoted DataFrame to its original form, or to change it from a wide shape to a long shape. You can explicitly specify the columns that should remain in the reshaped DataFrame with id_vars, and list which columns to convert into values with value_vars. As Dhavide demonstrated, if you don't pass a name to the values in pd.melt(), you will lose the name of your variable. You can fix this by using the value_name keyword argument.

Your job in this exercise is to melt visitors_by_city_weekday to move the city names from the column labels to values in a single column called 'city'. If you were to use just pd.melt(visitors_by_city_weekday), you would obtain the following result:
```
      city value
0  weekday   Mon
1  weekday   Sun
2   Austin   326
3   Austin   139
4   Dallas   456
5   Dallas   237
```
Therefore, you have to specify the id_vars keyword argument to ensure that 'weekday' is retained in the reshaped DataFrame, and the value_name keyword argument to change the name of value to visitors.

### Instructions:
* Reset the index of visitors_by_city_weekday with .reset_index().
* Print visitors_by_city_weekday and verify that you have just a range index, 0, 1, 2, 3. This has been done for you.
* Melt visitors_by_city_weekday to move the city names from the column labels to values in a single column called visitors.
* Print visitors to check that the city values are in a single column now and that the dataframe is longer and skinnier.

#### Script:
```
# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index() 

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars=['weekday'], value_name='visitors')

# Print visitors
print(visitors)
```
##### Output:
```
<script.py> output:
    city weekday  Austin  Dallas
    0        Mon     326     456
    1        Sun     139     237
      weekday    city  visitors
    0     Mon  Austin       326
    1     Sun  Austin       139
    2     Mon  Dallas       456
    3     Sun  Dallas       237
```
##### Comment:
Well done! Notice how your melted DataFrame now has a 'city' column with Austin and Dallas as its values. In the original DataFrame, they were columns themselves. Also note how specifying the value_name parameter has renamed the 'value' column to 'visitors'.

## 08. Going from wide to long
You can move multiple columns into a single column (making the data long and skinny) by "melting" multiple columns. In this exercise, you will practice doing this.

The users DataFrame has been pre-loaded for you. As always, explore it in the IPython Shell and note the index.

### Instructions:
* Define a DataFrame skinny where you melt the 'visitors' and 'signups' columns of users into a single column.
* Print skinny to verify the results. Note the value column that had the cell values in users.

#### Script:
```
# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday', 'city'], value_vars=['visitors', 'signups'])

# Print skinny
print(skinny)
```
##### Output:
```
<script.py> output:
      weekday    city  variable  value
    0     Sun  Austin  visitors    139
    1     Sun  Dallas  visitors    237
    2     Mon  Austin  visitors    326
    3     Mon  Dallas  visitors    456
    4     Sun  Austin   signups      7
    5     Sun  Dallas   signups     12
    6     Mon  Austin   signups      3
    7     Mon  Dallas   signups      5
```
##### Comment:
Well done! Here, because you didn't specify the var_name or value_name parameters, the melted DataFrame has the default variable and value column names.
