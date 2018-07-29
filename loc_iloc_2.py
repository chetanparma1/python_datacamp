# loc and iloc (2)
# loc and iloc also allow you to select both rows and columns from a DataFrame. To experiment, try out the following commands in the IPython Shell. Again, paired commands produce the same result.

# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]

# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]

# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
drives_right = cars.loc[['MOR']]
print(drives_right)

# Print sub-DataFrame
subDF = cars.loc[['RU', 'MOR'], ['country', 'drives_right']]
print(subDF)
