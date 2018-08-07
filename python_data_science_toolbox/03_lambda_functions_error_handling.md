# Pop quiz on lambda functions
In this exercise, you will practice writing a simple lambda function and calling this function. Recall what you know about lambda functions and answer the following questions:

How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?
How would you call add_bangs with the argument 'hello'?
You may use the IPython shell to test your code.

## Instructions
Possible Answers
The lambda function definition is: add_bangs = (a + '!!!'), and the function call is: add_bangs('hello').
press 1
The lambda function definition is: add_bangs = (lambda a: a + '!!!'), and the function call is: add_bangs('hello').
press 2
The lambda function definition is: (lambda a: a + '!!!') = add_bangs, and the function call is: add_bangs('hello').
press 3

### Answers:
3

# Writing a lambda function you already know
Some function definitions are simple enough that they can be converted to a lambda function. By doing this, you write less lines of code, which is pretty awesome and will come in handy, especially when you're writing and maintaining big programs. In this exercise, you will use what you know about lambda functions to convert a function that does a simple task into a lambda function. Take a look at this function definition:

```
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words
```
The function echo_word takes 2 parameters: a string value, word1 and an integer value, echo. It returns a string that is a concatenation of echo copies of word1. Your task is to convert this simple function into a lambda function.

## Instructions
* Define the lambda function echo_word using the variables word1 and echo. Replicate what the original function definition for echo_word() does above.
* Call echo_word() with the string argument 'hey' and the value 5, in that order. Assign the call to result.
```
# Define echo_word as a lambda function: echo_word
echo_word = (lambda x, y: x * y)

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)
```

### Output:
```
<script.py> output:
    heyheyheyheyhey
```

### Comments
Great work!

# Map() and lambda functions
So far, you've used lambda functions to write short, simple functions as well as to redefine functions with simple functionality. The best use case for lambda functions, however, are for when you want these simple functionalities to be anonymously embedded within larger expressions. What that means is that the functionality is not stored in the environment, unlike a function defined with def. To understand this idea better, you will use a lambda function in the context of the map() function.

Recall from the video that map() applies a function over an object, such as a list. Here, you can use lambda functions to define the function that map() will use to process the object. For example:
```
nums = [2, 4, 6, 8, 10]

result = map(lambda a: a ** 2, nums)
```
You can see here that a lambda function, which raises a value a to the power of 2, is passed to map() alongside a list of numbers, nums. The map object that results from the call to map() is stored in result. You will now practice the use of lambda functions with map(). For this exercise, you will map the functionality of the add_bangs() function you defined in previous exercises over a list of strings.

## Instructions
* In the map() call, pass a lambda function that concatenates the string '!!!' to a string item; also pass the list of strings, spells. Assign the resulting map object to shout_spells.
* Convert shout_spells to a list and print out the list.

```{python}
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda a: a + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)
```

### Output:
```
<script.py> output:
    ['protego!!!', 'accio!!!', 'expecto patronum!!!', 'legilimens!!!']
```

### Comments
Great work!

# Filter() and lambda functions
In the previous exercise, you used lambda functions to anonymously embed an operation within map(). You will practice this again in this exercise by using a lambda function with filter(), which may be new to you! The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria.

Your goal in this exercise is to use filter() to create, from an input list of strings, a new list that contains only strings that have more than 6 characters.

## Instructions
* In the filter() call, pass a lambda function and the list of strings, fellowship. The lambda function should check if the number of characters in a string member is greater than 6; use the len() function to do this. Assign the resulting filter object to result.
* Convert result to a list and print out the list.

```{python}
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda x: len(x) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)
```
### Output:
```
<script.py> output:
    ['samwise', 'aragorn', 'boromir', 'legolas', 'gandalf']
```

### Comments
Great work!

# Reduce() and lambda functions
You're getting very good at using lambda functions! Here's one more function to add to your repertoire of skills. The reduce() function is useful for performing some computation on a list and, unlike map() and filter(), returns a single value as a result. To use reduce(), you must import it from the functools module.

Remember gibberish() from a few exercises back?
```
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge
```
gibberish() simply takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings. In this exercise, you will replicate this functionality by using reduce() and a lambda function that concatenates strings together.

## Instructions
* Import the reduce function from the functools module.
* In the reduce() call, pass a lambda function that takes two string arguments item1 and item2 and concatenates them; also pass the list of strings, stark. Assign the result to result. The first argument to reduce() should be the lambda function and the second argument is the list stark.

```{python}
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce((lambda x, y: x + y), stark)

# Print the result
print(result)
```
### Output
```
<script.py> output:
    robbsansaaryabrandonrickon
```
### Comments
Great work!

# Pop quiz about errors
In the video, Hugo talked about how errors happen when functions are supplied arguments that they are unable to work with. In this exercise, you will identify which function call raises an error and what type of error is raised.

Take a look at the following function calls to len():
```
len('There is a beast in every man and it stirs when you put a sword in his hand.')

len(['robb', 'sansa', 'arya', 'eddard', 'jon'])

len(525600)

len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey'))  
```

Which of the function calls raises an error and what type of error is raised?
Possible Answers
* The call len('There is a beast in every man and it stirs when you put a sword in his hand.') raises a TypeError.
press 1
* The call len(['robb', 'sansa', 'arya', 'eddard', 'jon']) raises an IndexError.
press 2
* The call len(525600) raises a TypeError.
press 3
* The call len(('jaime', 'cersei', 'tywin', 'tyrion', 'joffrey')) raises a NameError.
press 4

### Answer: 3

# Error handling with try-except
A good practice in writing your own functions is also anticipating the ways in which other people (or yourself, if you accidentally misuse your own function) might use the function you defined.

As in the previous exercise, you saw that the len() function is able to handle input arguments such as strings, lists, and tuples, but not int type ones and raises an appropriate error and error message when it encounters invalid input arguments. One way of doing this is through exception handling with the try-except block.

In this exercise, you will define a function as well as use a try-except block for handling cases when incorrect input arguments are passed to the function.

Recall the shout_echo() function you defined in previous exercises; parts of the function definition are provided in the sample code. Your goal is to complete the exception handling code in the function definition and provide an appropriate error message when raising an error.

## Instructions
* Initialize the variables echo_word and shout_words to empty strings.
* Add the keywords try and except in the appropriate locations for the exception handling block.
* Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
* Concatenate the string '!!!' to echo_word. Assign the result to shout_words.

```{python}
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ""
    shout_words = ""
    
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")
```
### Output:
```
<script.py> output:
    word1 must be a string and echo must be an integer.
```

#### Comments:
Great work!

# Error handling by raising an error
Another way to raise an error is by using raise. In this exercise, you will add a raise statement to the shout_echo() function you defined before to raise an error message when the value supplied by the user to the echo argument is less than 0.

The call to shout_echo() uses valid argument values. To test and see how the raise statement works, simply change the value for the echo argument to a negative value. Don't forget to change it back to valid values to move on to the next exercise!

## Instructions
* Complete the if statement by checking if the value of echo is less than 0.
* In the body of the if statement, add a raise statement that raises a ValueError with message 'echo must be greater than 0' when the value supplied by the user to echo is less than 0.

```{python}
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)
```
### Comments
Great work!
