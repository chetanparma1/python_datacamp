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
# Functions that return single values
You're getting very good at this! Try your hand at another modification to the shout() function so that it now returns a single value instead of printing within the function. Recall that the return keyword lets you return values from functions. Parts of the function shout(), which you wrote earlier, are shown. Returning values is generally more desirable than printing them out because, as you saw earlier, a print() call assigned to a variable has type NoneType.

## Instructions
* In the function body, concatenate the string in word with '!!!' and assign to shout_word.
* Replace the print() statement with the appropriate return statement.
* Call the shout() function, passing to it the string, 'congratulations', and assigning the call to the variable, yell.
* To check if yell contains the value returned by shout(), print the value of yell.

```{python}
# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return shout_word

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)
```
### Comments
Great work! Here it made sense to assign the output of shout('congratulations') to a variable yell because the function shout actually returns a value, it does not merely print one.

# Functions with multiple parameters
Hugo discussed the use of multiple parameters in defining functions in the last lecture. You are now going to use what you've learned to modify the shout() function further. Here, you will modify shout() to accept two arguments. Parts of the function shout(), which you wrote earlier, are shown.

## Instructions
* Modify the function header such that it accepts two parameters, word1 and word2, in that order.
* Concatenate each of word1 and word2 with '!!!' and assign to shout1 and shout2, respectively.
* Concatenate shout1 and shout2 together, in that order, and assign to new_shout.
* Pass the strings 'congratulations' and 'you', in that order, to a call to shout(). Assign the return value to yell.

```{python}
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)
```

### Comments
Great work!

# A brief introduction to tuples
Alongside learning about functions, you've also learned about tuples! Here, you will practice what you've learned about tuples: how to construct, unpack, and access tuple elements. Recall how Hugo unpacked the tuple even_nums in the video:

a, b, c = even_nums

A three-element tuple named nums has been preloaded for this exercise. Before completing the script, perform the following:

Print out the value of nums in the IPython shell. Note the elements in the tuple.
In the IPython shell, try to change the first element of nums to the value 2 by doing an assignment: nums[0] = 2. What happens?

## Instructions
Unpack nums to the variables num1, num2, and num3.
Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.

```{python}
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums
even_nums = (2, num2, num3)
```
### Comments
Great work!
