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
