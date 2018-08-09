# Write a basic list comprehension
In this exercise, you will practice what you've learned from the video about writing list comprehensions. You will write a list comprehension and identify the output that will be produced.

The following list has been pre-loaded in the environment.

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
How would a list comprehension that produces a list of the first character of each string in doctor look like? Note that the list comprehension uses doc as the iterator variable. What will the output be?

## Instructions:
Possible Answers  <br />
* The list comprehension is [for doc in doctor: doc[0]] and produces the list ['h', 'c', 'c', 't', 'w'].
press 1
* The list comprehension is [doc[0] for doc in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].
press 2
* The list comprehension is [doc[0] in doctor] and produces the list ['h', 'c', 'c', 't', 'w'].
press 3

### Answer: 
2

# List comprehension over iterables
You know that list comprehensions can be built over iterables. Given the following objects below, which of these can we build list comprehensions over?
```
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

range(50)

underwood = 'After all, we are nothing more or less than what we choose to reveal.'

jean = '24601'

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

valjean = 24601
```

### Instructions:
Possible Answers  <br />
* You can build list comprehensions over all the objects except the string of number characters jean.
** press 1
* You can build list comprehensions over all the objects except the string lists doctor and flash.
** press 2
* You can build list comprehensions over all the objects except range(50).
** press 3
* You can build list comprehensions over all the objects except the integer object valjean.
** press 4

### Answer: 4

# Writing list comprehensions
You now have all the knowledge necessary to begin writing list comprehensions! Your job in this exercise is to write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.

## Instructions
Using the range of numbers from 0 to 9 as your iterable and i as your iterator variable, write a list comprehension that produces a list of numbers consisting of the squared values of i.

```{python}
# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
```
### Comments:
Great work!

# Great! At this point, you have a good grasp of the basic syntax of list comprehensions. Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!

Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:
```
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
```
Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall list comprehension:

```
[[output expression] for iterator variable in iterable]
```

Note that here, the output expression is itself a list comprehension.

## Instructions
* In the inner list comprehension - that is, the output expression of the nested list comprehension - create a list of values from 0 to 4 using `range()`. Use col as the iterator variable.
* In the iterable part of your nested list comprehension, use `range()` to count 5 rows - that is, create a list of values from 0 to 4. Use row as the iterator variable; note that you won't be needing this to create values in the list of lists.

```{python}
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

# Print the matrix
for row in matrix:
    print(row)
```

### Output:
```
<script.py> output:
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
```

### Comments:
Great work!
