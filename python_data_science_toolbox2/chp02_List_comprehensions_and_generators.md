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
