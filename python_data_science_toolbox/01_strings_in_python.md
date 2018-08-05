# Strings in Python
In the video, you learned of another standard Python datatype, strings. Recall that these represent textual data. To assign the string 'DataCamp' to a variable company, you execute:

company = 'DataCamp'
You've also learned to use the operations + and * with strings. Unlike with numeric types such as ints and floats, the + operator concatenates strings together, while the * concatenates multiple copies of a string together. In this exercise, you will use the + and * operations on strings to answer the question below. Execute the following code in the shell:

object1 = "data" + "analysis" + "visualization"
object2 = 1 * 3
object3 = "1" * 3
What are the values in object1, object2, and object3, respectively?

## Possible Answers
object1 contains "data + analysis + visualization", object2 contains "1*3", object3 contains 13.
press 1
object1 contains "data+analysis+visualization", object2 contains 3, object3 contains "13".
press 2
object1 contains "dataanalysisvisualization", object2 contains 3, object3 contains "111".
press 3

# Recapping built-in functions
In the video, Hugo briefly examined the return behavior of the built-in functions print() and str(). Here, you will use both functions and examine their return values. A variable x has been preloaded for this exercise. Run the code below in the console. Pay close attention to the results to answer the question that follows.

Assign str(x) to a variable y1: y1 = str(x)
Assign print(x) to a variable y2: y2 = print(x)
Check the types of the variables x, y1, and y2.
What are the types of x, y1, and y2?

## Instructions
Possible Answers
They are all str types.
press 1
x is a float, y1 is an float, and y2 is a str.
press 2
x is a float, y1 is a str, and y2 is a NoneType.
press 3
They are all NoneType types.
press 4

# Write a simple function
In the last video, Hugo described the basics of how to define a function. You will now write your own function!

Define a function, shout(), which simply prints out a string with three exclamation marks '!!!' at the end. The code for the square() function that we wrote earlier is found below. You can use it as a pattern to define shout().

```
def square():
    new_value = 4 ** 2
    return new_value
```
Note that the function body is indented 4 spaces already for you. Function bodies need to be indented by a consistent number of spaces and the choice of 4 is common.

## Instructions
* Complete the function header by adding the appropriate function name, shout.
* In the function body, concatenate the string, 'congratulations' with another string, '!!!'. Assign the result to `shout_word`.
* Print the value of shout_word.
* Call the shout function.

```{python}
# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()
```

# Single-parameter functions
Congratulations! You have successfully defined and called your own function! That's pretty cool.

In the previous exercise, you defined and called the function shout(), which printed out a string concatenated with '!!!'. You will now update shout() by adding a parameter so that it can accept and process any string argument passed to it. Also note that shout(word), the part of the header that specifies the function name and parameter(s), is known as the signature of the function. You may encounter this term in the wild!

## Instructions
* Complete the function header by adding the parameter name, word.
* Assign the result of concatenating word with '!!!' to shout_word.
* Print the value of shout_word.
* Call the shout() function, passing to it the string, 'congratulations'.

```{python}
# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

### Comments
Great work!
```
