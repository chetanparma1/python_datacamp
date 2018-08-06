# Pop quiz on understanding scope
In this exercise, you will practice what you've learned about scope in functions. The variable num has been predefined as 5, alongside the following function definitions:

def func1():
    num = 3
    print(num)

def func2():
    global num
    double_num = num * 2
    num = 6
    print(double_num)
Try calling func1() and func2() in the shell, then answer the following questions:

What are the values printed out when you call func1() and func2()?
What is the value of num in the global scope after calling func1() and func2()?

## Instructions
Possible Answers
func1() prints out 3, func2() prints out 6, and the value of num in the global scope is 3.
press 1
func1() prints out 3, func2() prints out 3, and the value of num in the global scope is 3.
press 2
func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 10.
press 3
func1() prints out 3, func2() prints out 10, and the value of num in the global scope is 6.
press 4

### Answer: 4

# The keyword global
Let's work more on your mastery of scope. In this exercise, you will use the keyword global within a function to alter the value of a variable defined in the global scope.

## Instructions
Use the keyword global to alter the object team in the global scope.
Change the value of team in the global scope to the string "justice league". Assign the result to team.
Hit the Submit button to see how executing your newly defined function change_team() changes the value of the name team!

```{python}
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
    
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
```
### Output
```
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
    
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
```

# Python's built-in scope
Here you're going to check out Python's built-in scope, which is really just a built-in module called builtins. However, to query builtins, you'll need to import builtins 'because the name builtins is not itself built in...No, I’m serious!' (Learning Python, 5th edition, Mark Lutz). After executing import builtins in the IPython Shell, execute dir(builtins) to print a list of all the names in the module builtins. Have a look and you'll see a bunch of names that you'll recognize! Which of the following names is NOT in the module builtins?
 
## Instructions
Possible Answers
'sum'
press 1
'range'
press 2
'array'
press 3
'tuple'
press 4

### Answer: 3

# Nested Functions I
You've learned in the last video about nesting functions within functions. One reason why you'd like to do this is to avoid writing out the same computations within functions repeatedly. There's nothing new about defining nested functions: you simply define it as you would a regular function with def and embed it inside another function!

In this exercise, inside a function three_shouts(), you will define a nested function inner() that concatenates a string object with !!!. three_shouts() then returns a tuple of three elements, each a string concatenated with !!! using inner(). Go for it!

## Instructions
* Complete the function header of the nested function with the function name inner() and a single parameter word.
* Complete the return value: each element of the tuple should be a call to inner(), passing in the parameters from three_shouts() as arguments to each call.

```{python}
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
```
### Output
```
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))
```
### Comments
Great work!

# Nested Functions II
Great job, you've just nested a function within another function. One other pretty cool reason for nesting functions is the idea of a closure. This means that the nested or inner function remembers the state of its enclosing scope when called. Thus, anything defined locally in the enclosing scope is available to the inner function even when the outer function has finished execution.

Let's move forward then! In this exercise, you will complete the definition of the inner function inner_echo() and then call echo() a couple of times, each with a different argument. Complete the exercise and see what the output will be!

## Instructions
* Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
* Complete the function echo() so that it returns inner_echo.
* We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
* Hit Submit to call twice() and thrice() and print the results.

```{python}
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))
```

### Output:
```
<script.py> output:
    hellohello hellohellohello
```

### Comment:
Great work!
