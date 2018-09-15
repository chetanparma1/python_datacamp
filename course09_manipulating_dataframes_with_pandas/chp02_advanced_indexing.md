# Chapter 02: Advanced Indexing

## 01. Index values and names
Which one of the following index operations does not raise an error?

The sales DataFrame which you have seen in the videos of the previous chapter has been pre-loaded for you and is available for exploration in the IPython Shell.

```
     eggs  salt  spam
month                  
Jan      47  12.0    17
Feb     110  50.0    31
Mar     221  89.0    72
Apr      77  87.0    20
May     132   NaN    52
Jun     205  60.0    55
```

### Possible Answers
* sales.index[0] = 'JAN'.
press 1
* sales.index[0] = sales.index[0].upper().
press 2
* sales.index = range(len(sales)).
press 3

#### Script & Output:
```
In [1]: sales
Out[1]: 
       eggs  salt  spam
month                  
Jan      47  12.0    17
Feb     110  50.0    31
Mar     221  89.0    72
Apr      77  87.0    20
May     132   NaN    52
Jun     205  60.0    55

In [2]: sales.index[0]='JAN'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sales.index[0]='JAN'
  File "<stdin>", line 2050, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations

In [3]: sales.index[0] = sales.index[0].upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sales.index[0] = sales.index[0].upper()
  File "<stdin>", line 2050, in __setitem__
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations

In [4]: sales.index = range(len(sales))
```
##### Answer: 
3

##### Comment:
Well done!
