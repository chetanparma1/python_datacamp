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

\# Recall from the video that map() applies a function over an object, such as a list. Here, you can use lambda functions to define the function that map() will use to process the object. For example:
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
