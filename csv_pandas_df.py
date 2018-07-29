# Import pandas as pd
import pandas as pd

# Fix import by including index_col
# set the first column as the row labels. 
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out cars
print(cars)
