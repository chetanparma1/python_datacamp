# Iterators vs Iterables
Let's do a quick recall of what you've learned about iterables and iterators. Recall from the video that an iterable is an object that can return an iterator, while an iterator is an object that keeps state and produces the next value when you call next() on it. In this exercise, you will identify which object is an iterable and which is an iterator.

The environment has been pre-loaded with the variables flash1 and flash2. Try printing out their values with print() and next() to figure out which is an iterable and which is an iterator.

## Possible Answers
Click or Press Ctrl+1 to focus <br />
* Both flash1 and flash2 are iterators.
press 1
* Both flash1 and flash2 are iterables.
press 2
* flash1 is an iterable and flash2 is an iterator.
press 3

### Output:
```
In [1]: flash1
Out[1]: ['jay garrick', 'barry allen', 'wally west', 'bart allen']

In [2]: flash2
Out[2]: <list_iterator at 0x7f60790d8240>
```

### Answer:
3

### Comments:
Correct!
